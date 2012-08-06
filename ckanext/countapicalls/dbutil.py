from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select, text
from sqlalchemy import func

import ckan.model as model
from ckan.lib.base import *

from logging import getLogger

log = logging.getLogger(__name__)
cached_tables = {}

def init_tables():
    metadata = MetaData()
    package_stats = Table('api_package_stats', metadata,
                          Column('package_id', String(60),
                                 primary_key=True),
                          Column('visits', Integer))
    metadata.create_all(model.meta.engine)


def get_table(name):
    if name not in cached_tables:
        meta = MetaData()
        meta.reflect(bind=model.meta.engine)
        table = meta.tables[name]
        cached_tables[name] = table
    return cached_tables[name]


def update_visits(item_id):
    stats = get_table('api_package_stats')
    id_col_name = 'package_id'
    id_col = getattr(stats.c, id_col_name)
    s = stats.select(id_col == item_id)    
    connection = model.Session.connection()
    result = connection.execute(s).fetchone()
    log.debug("Result : %s", result)
    # we have results, let's update
    if result and result[0]:
        connection.execute(stats.update()\
            .where(id_col == item_id)\
            .values(visits=result[1]+1))
    # we dont have results, let's insert
    else:
        values = {id_col_name: item_id, 'visits': 1}
        res = connection.execute(stats.insert().values(**values))
        result = connection.execute(s).fetchone()
        #log.debug("Inserted result : %s", res.rowcount)

    model.Session.commit()


