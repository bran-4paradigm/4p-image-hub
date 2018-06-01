from pecan.rest import RestController
from imagehub.controllers.version1 import image


class APIController(RestController):

    pushimage = image.PushImageController()