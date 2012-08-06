import os
import logging

import pylons
from pylons import request

from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IPackageController

import dbutil

log = logging.getLogger(__name__)

class CountAPICallsPlugin(SingletonPlugin):
    implements(IPackageController, inherit=True)
    
    def read(self, entity):
        #call dbutil and update stats if we're reading from the API
        routes = pylons.request.environ.get('pylons.routes_dict')
        action = routes.get('action')
        controller = routes.get('controller')

        if(action == 'show' and controller == 'api'):    
            id = routes.get('id')
            dbutil.update_visits(id)
            log.debug('CountAPICallsPlugin logged api call for item %s', id)
        
        #log.debug('IPackageController entity : %s', entity)
        #log.debug('IPackageController request : %s', request)
        #log.debug('IPackageController routes : %s', routes)
        #log.debug('IPackageController action : %s', action)
        #log.debug('IPackageController controller : %s', controller)