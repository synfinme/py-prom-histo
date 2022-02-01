
REPO_NAME := synfinmelab
IMAGE_NAME := py-prom-histo
IMAGE_TAG := v0.5
IMAGE := "${REPO_NAME}/${IMAGE_NAME}:${IMAGE_TAG}"

_init	:
	echo "*** Use { build | push } ***"

build	:
	docker build -t ${IMAGE} .

push	: build
	docker push ${IMAGE}
