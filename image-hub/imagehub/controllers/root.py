import pecan

from imagehub.controllers import hub
from pecan import expose

class RootController(object):

    @expose(template='json')
    def _default(self):
        return 'url path is wrong'



pecan.route(RootController, 'image-hub', hub.ImageHubController())