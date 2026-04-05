import os
import subprocess

service = os.getenv("INPUT_SERVICE_NAME")
path = os.getenv("INPUT_SERVICE_PATH")
docker_username = os.getenv("INPUT_DOCKER_USERNAME")
docker_token = os.getenv("INPUT_DOCKER_TOKEN")
image_tag = os.getenv("INPUT_IMAGE_TAG")

image_name = f"{docker_username}/{service}:{image_tag}"

print("Running custom Docker build action...")
print(f"Building image: {image_name}")

#login to docker hub
subprocess.run(
    f"echo {docker_token} | docker login -u {docker_username} --password-stdin",
     shell=True, check=True)

#build the docker image
subprocess.run(f"docker build -t {image_name} {path}", shell=True)

#push image to docker hub
subprocess.run(f"docker push {image_name}", shell=True)

print(f"Successfully built and pushed {image_name}")