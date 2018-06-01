import six
import wsme

from imagehub import model


class PushPayload(model.Base):
    filepath = wsme.wsattr(six.text_type, mandatory=True)
    images = wsme.wsattr({six.text_type:six.text_type}, mandatory=False)
    username = wsme.wsattr(six.text_type, mandatory=False)
    password = wsme.wsattr(six.text_type, mandatory=False)
    registry = wsme.wsattr(six.text_type, mandatory=False)

