# cookiecutter-grpc-python

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter gRPC Python is a framework for jumpstarting production-ready gRPC Python projects quickly.

## Features

- [x] Makefile
- [ ] Dockerfile
- [ ] docker base image choice
- [ ] Docker version choice
- [ ] Docker-compose
- [ ] .gitignore
- [ ] README.md
- [ ] Starter proto file
- [ ] Python client
- [ ] Healthcheck
- [ ] System check
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
app_name [example]:
project_short_description [example description]:
Select docker_build_image_version:
1 - 1.11
2 - 1.10.3
3 - 1.9.7
Choose from 1, 2, 3 [1]:
use_docker [y]:
Select use_ci:
1 - travis
2 - circle
3 - none
Choose from 1, 2, 3 [1]:

```
