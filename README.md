# cookiecutter-grpc-python

Powered by [Cookiecutter](https://github.com/audreyr/cookiecutter), Cookiecutter gRPC Python is a framework for jumpstarting production-ready gRPC Python projects quickly.

## Features

- [x] Makefile
- [ ] Docker version choice
- [ ] Docker-compose
- [x] .gitignore
- [x] README.md
- [x] cookiecutter-options.yml
- [ ] tests for cookiecutter
- [ ] Python client
  - [ ] base client
  - [ ] client keepalive
  - [ ] channel ready (reconnects if connection dropped)
  - [ ] client tests
- [ ] Server
  - [ ] Healthcheck
  - [x] System Info
  - [ ] tests for gRPC service
  - [x] server keepalive
  - [x] Dockerfile
  - [ ] docker base image choice
  - [ ] endpoint decorator
  - [ ] log server start
  - [ ] log endpoint call

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

If you want to re-apply the changes to this cookiecutter, run:
```console
$ cookiecutter https://github.com/lieutdan13/cookiecutter-grpc-python --config-file [location_of_your_project]/cookiecutter-options.yml -f [parent_directory_of_your_project]
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
