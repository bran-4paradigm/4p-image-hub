import pecan

from imagehub.controllers import hub


class RootController(object):
    pass


pecan.route(RootController, 'image-hub', hub.ImageHubController())