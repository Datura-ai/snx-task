import docker 
from docker.errors import ContainerError, ImageNotFound, APIError

from app.models import Task, TaskStatusEnum
from app.core.config import settings


class DockerService:
    """Service for docker containers."""

    def create_task_container(self, task: Task):
        """Create docker container for given task."""
        client = docker.from_env()

        # status code for docker container output
        # 1: failed, 0: success
        status_code: int = 1
        output: str = ""
        container_id = None

        try:
            resources: dict = {
                "cpus": task.cpu,
                "memory": task.ram,
                "storage_opt": {
                    "size": task.storage,
                }
            }

            gpu_config: dict = {
                "device_requests": [
                    {
                        "Driver": "nvidia",
                        "Count": task.gpu,
                        "Capabilities": [["gpu"]]
                    }
                ]
            }

            kwargs: dict = {
                "image": settings.TASK_EXECUTOR_DOCKER_IMAGE,
                "detach": True,
                "cpu_count": resources["cpus"],
                "mem_limit": resources["memory"],
                # "storage_opt": resources["storage_opt"],
                "environment": {
                    "PYTHON_CODE": task.code
                },
                **gpu_config
            }

            if settings.EXCLUDE_STORAGE_OPTION is not True:
                kwargs["storage_opt"] = resources["storage_opt"]

            # Run the command in a new container
            container = client.containers.run(**kwargs)

            # Wait for the container to finish and capture the output
            response = container.wait()
            output = container.logs()

            # Clean up - remove the container
            container.remove()

            status_code = response['StatusCode']
            output = output.decode('utf-8')
            container_id = container.id
        except ImageNotFound as e:
            status_code = 1
            output = "Docker image not found."
        except ContainerError as e:
            status_code = 1
            output = f"Container error: {e}"
        except APIError as e:
            status_code = 1
            output = f"Docker API error: {e}"
        finally:
            client.close()

        return {
            "task_status":  TaskStatusEnum.completed if status_code == 0 else TaskStatusEnum.failed,
            "output": output,
            "container_id": container_id
        }
