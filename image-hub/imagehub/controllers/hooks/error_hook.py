import json
import sys
import webob
import wsme

import pecan
from pecan.hooks import PecanHook


class JSONErrorHook(PecanHook):
    """A pecan hook that translates webob HTTP errors into a JSON format."""

    def on_error(self, state, exc):
        exc_info = sys.exc_info()
        data = wsme.api.format_exception(
            exc_info,
            pecan.conf.get('wsme', {}).get('debug', False)
        )
        if isinstance(exc, webob.exc.HTTPError):
            status = exc.status
            header_list = exc.headerlist
        else:
            status = 500
            header_list = None
            # Reset fault string so not to expose internal error messages on
            # API response. However, the actual error message is logged by
            # wsme.api.format_exception.
            data['faultstring'] = "Internal Server Error"
        return webob.Response(
            body=json.dumps(data),
            status=status,
            headerlist=header_list,
            content_type='application/json'
        )
