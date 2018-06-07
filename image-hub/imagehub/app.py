from pecan import make_app
from imagehub import model

from imagehub.controllers.hooks import error_hook


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        hooks=[error_hook.JSONErrorHook()],
        **app_conf
    )
