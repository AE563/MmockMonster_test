import docker
import os


config_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                           ''))

client = docker.from_env()
container = client.containers.run("jordimartin/mmock",
                                  detach=True,
                                  volumes={config_path: {'bind': '/config'}},
                                  ports={'8082': 8082, '8083': 8083})
# container.stop()
# container.remove()
