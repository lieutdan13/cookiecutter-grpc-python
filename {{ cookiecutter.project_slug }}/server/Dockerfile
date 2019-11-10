FROM grpc/python:1.4-onbuild

HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD python health.py

CMD ["python", "serve.py"]
