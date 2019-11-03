.PHONY: build

SANDBOX_DIR=../cookiecutter-sandbox

build:
	mkdir -p ${SANDBOX_DIR}
	rm -rf ${SANDBOX_DIR}/grpc-python
	cookiecutter --no-input -o ${SANDBOX_DIR} .

build-interactive:
	mkdir -p ${SANDBOX_DIR}
	cookiecutter -f -o ${SANDBOX_DIR} .
