import docker

class dockerClient():
    def __init__(self):
        self.client = docker.from_env()

    def get_client(self):
        if self.client is not None:
            return docker.from_env()
        return self.client