import grpc
import sys

from proto import health_pb2_grpc
from proto.health_pb2 import HealthCheckRequest


class HealthCheck(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50050")
        self.setup_stubs()

    def __del__(self):
        try:
            self.channel.close()
        except Exception:
            pass

    def setup_stubs(self):
        self.health_check_stub = health_pb2_grpc.HealthStub(self.channel)

    def check_health(self):
        response = self.health_check_stub.HealthCheck(HealthCheckRequest())
        if response.status.lower() == "ok":
            sys.exit(0)
        sys.exit(1)


if __name__ == "__main__":
    client = HealthCheck()
    client.check_health()
