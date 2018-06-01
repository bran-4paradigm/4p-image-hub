import wsme
from wsme.rest import json as wsme_json


def init_model():
    """
    This is a stub method which is called at application startup time.

    If you need to bind to a parsed database configuration, set up tables or
    ORM classes, or perform any database initialization, this is the
    recommended place to do it.

    For more information working with databases, and some common recipes,
    see https://pecan.readthedocs.io/en/latest/databases.html
    """
    pass


class Base(wsme.types.Base):

    def to_dict(self):
        return wsme_json.tojson(self.__class__, self)

    @classmethod
    def to_obj(cls, values):
        wsme_dict = {}
        for attribute in wsme.types.list_attributes(cls):
            value = values.get(attribute.name, wsme.types.Unset)
            wsme_dict[attribute.name] = value
        return cls(**wsme_dict)

    @classmethod
    def to_wsme_model(cls, obj):
        wsme_dict = {}
        for attribute in wsme.types.list_attributes(cls):
            value = getattr(obj, attribute.name, None)
            wsme_dict[attribute.name] = value
        return cls(**wsme_dict)
