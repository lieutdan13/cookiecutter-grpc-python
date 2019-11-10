SHELL := bash

.PHONY: build help generate-proto build-server

PROTO_DIR = ./protos/generated

build: generate-proto
	docker-compose build

run:
	docker-compose up -d

help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort

generate-proto:
	docker run -v "${PWD}":/src -w /src grpc/python:1.4 bash ./generate-grpc-code.sh && \
	cp -rf ./protos/python/proto/* ./server/proto/ && \
	cp -rf ./protos/python/proto/* ./client/python/proto/ && \
	tree ./protos
