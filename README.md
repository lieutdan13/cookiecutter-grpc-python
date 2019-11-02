# cookiecutter-grpc-python

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter gRPC Python is a framework for jumpstarting production-ready gRPC Python projects quickly.

## Features

- [x] Makefile
- [x] Dockerfile
- [ ] docker base image choice
- [ ] Docker version choice
- [ ] Docker-compose
- [x] .gitignore
- [ ] README.md
- [x] Starter proto file
- [ ] Python client
- [ ] Healthcheck
- [x] System check
- [ ] cookiecutter-options.yml
- [ ] tests for cookiecutter
- [ ] tests for gRPC service

## Usage

First, get Cookiecutter:
```console
$ pip install cookiecutter
```

Alternatively, you can install `cookiecutter` with homebrew:
```console
$ brew install cookiecutter
```

Finally, to run it based on this template, type:
```console
$ cookiecutter https://github.com/lieutdan13/cookiecutter-grpc-python
```

## options
You will be asked about your basic info (name, project name, app name, etc.). This info will be used to customize your new project.

Warning: After this point, change all default options to your own information.

Answer the prompts with your own desired options.

```console
full_name [John Doe]: 
project_name [gRPC Python]: 
project_slug [grpc-python]: 
app_name [grpc_python]: 
project_short_description [A gRPC service powered by Python.]:
```
