# -*- coding:utf-8 -*-
import logging
import os
import subprocess
import tempfile
import json
import webob.exc

from pecan.rest import RestController
from wsmeext.pecan import wsexpose

from imagehub.controllers.version1.types import image


LOG = logging.getLogger(__name__)


class PushImageController(RestController):

    @wsexpose(unicode, body=image.PushPayload, status_code=202)
    def post(self, payload):

        data = payload.to_dict()
        # TODO: check repository is ip:port style

        tarfile = data.get("filepath")
        images = data.get("images")

        username = os.environ.get("USERNAME")
        password = os.environ.get("PASSWORD")
        registry = os.environ.get("REGISTRY")
        timeout = os.environ.get("TIMEOUT")

        if registry is None:
            raise webob.exc.HTTPBadRequest(
                "Registry can not be None"
            )

        fd, tmp_file = tempfile.mkstemp(
            prefix="image_conf", dir="/tmp"
        )
        os.close(fd)

        if timeout is None:
            timeout = 60

        images_registry = {}
        for key, value in images.iteritems():
            if value.startswith('/'):
                value = value[1:]
            images_registry[key] = registry + '/app-prophet-ee/'  + value

        image_conf = {
            "root" : "/root/tmp/docker",
            "images" : images_registry,
            "insecure-registries" : [registry],
            "auth" : { "username":username, "password":password, "serveraddress":registry },
            "timeout": timeout
        }

        with open(tmp_file, "w") as f:
            json.dump(image_conf, f)


        try:
            push_task = subprocess.Popen('/app/client -i {} -c {}'.format(tarfile, tmp_file),
                                         shell=True,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            out_bytes = e.output
            code = e.returncode
            LOG.error(out_bytes)
            LOG.error(code)
            raise webob.exc.HTTPBadRequest(
                "Execute push image client error"
            )

        res =  push_task.stdout.read()
        LOG.info(res)
        return {"result": res}
