import logging
#import datetime
#import time

from pylons import config as pylonsconfig
from ckan.lib.cli import CkanCommand
import ckan.model as model

import dbutil

#log = logging.getLogger(__name__)

class InitDB(CkanCommand):
    """Initialise the local stats database tables
    """
    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 0
    min_args = 0

    def command(self):
        self._load_config()
        # funny dance we need to do to make sure we've got a
        # configured session
        model.Session.remove()
        model.Session.configure(bind=model.meta.engine)
        dbutil.init_tables()
        #log.info("Set up countapicalls table (api_package_stats) in main database")
