.PHONY: build

SANDBOX_DIR=../cookiecutter-sandbox

build: sandbox clean
	cookiecutter --no-input -o ${SANDBOX_DIR} .

rebuild: sandbox
	cookiecutter -f --no-input -o ${SANDBOX_DIR} .

build-interactive: sandbox
	cookiecutter -f -o ${SANDBOX_DIR} .

sandbox:
	mkdir -p ${SANDBOX_DIR}

clean:
	rm -rf ${SANDBOX_DIR}/grpc-python
