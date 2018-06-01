from pecan.rest import RestController
from imagehub.controllers import v_1


class ImageHubController(RestController):
    v1 = v_1.APIController()