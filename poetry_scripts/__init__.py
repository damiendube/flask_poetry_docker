import docker

DOCKER_IMAGE_NAME = "poetry_demo:latest"


def run():
    docker_client = docker.from_env()
    run_image(docker_client)


def stop():
    docker_client = docker.from_env()
    stop_container(docker_client)


def build():
    docker_client = docker.from_env()
    build_image(docker_client)


def clean():
    docker_client = docker.from_env()
    remove_image(docker_client)


def run_image(docker_client: docker.APIClient):
    try:
        docker_client.containers.run(DOCKER_IMAGE_NAME, ["wsgi"], ports={5000: 5000}, auto_remove=True, detach=True)
    except docker.errors.APIError as err:
            print("Error running the image", err)

def stop_container(docker_client: docker.APIClient):
    print(f"Stoping all containers from image {DOCKER_IMAGE_NAME}")
    for container in docker_client.containers.list(filters={'ancestor': DOCKER_IMAGE_NAME}):
        try:
            container.stop()
        except docker.errors.APIError as err:
            print("Error stoping the container", err)


def remove_containers(docker_client: docker.APIClient):
    print(f"Removing all containers from image {DOCKER_IMAGE_NAME}")
    stop_container(docker_client)

    for container in docker_client.containers.list(filters={'ancestor': DOCKER_IMAGE_NAME}):
        try:
            container.remove(force=True)
        except docker.errors.APIError as err:
            print("Error removing the container", err)


def remove_image(docker_client: docker.APIClient):
    remove_containers(docker_client)

    print(f"Removing image {DOCKER_IMAGE_NAME}")
    try:
        docker_client.images.remove(image=DOCKER_IMAGE_NAME, force=True)
    except docker.errors.APIError as err:
            print("Error removing the image", err)


def build_image(docker_client: docker.APIClient):
    try:
        docker_client.images.build(path='.', tag=DOCKER_IMAGE_NAME)
    except docker.errors.APIError as err:
            print("Error building the image", err)
