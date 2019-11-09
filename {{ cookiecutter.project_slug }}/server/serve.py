import time

from concurrent import futures

import grpc

from proto.health_pb2_grpc import add_HealthServicer_to_server
from servicers.health import HealthServicer
from proto.system_info_pb2_grpc import add_SystemInfoServicer_to_server
from servicers.system_info import SystemInfoServicer

GRPC_MAX_WORKERS = 10
GRPC_INSECURE_PORT = 50050
GRPC_SECURE_PORT = 50051


class Server(object):
    def __init__(self):
        self.server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=GRPC_MAX_WORKERS),
            options=(
                ("grpc.keepalive_time_ms", 20000),  # send keepalive every x milliseconds
                ("grpc.keepalive_timeout_ms", 5000),  # keepalive ping time out after x milliseconds
                ("grpc.keepalive_permit_without_calls", True),  # allow keepalive pings when there's no gRPC calls
                ("grpc.http2.max_pings_without_data", 0),  # allow unlimited amount of keepalive pings without data
                ("grpc.http2.min_time_between_pings_ms", 10000),  # allow grpc pings from client every x milliseconds
                ("grpc.http2.min_ping_interval_without_data_ms", 5000),  # allow grpc pings from client without data every x milliseconds
            ),
        )
        self._add_servicers()

    def _add_servicers(self):
        add_SystemInfoServicer_to_server(SystemInfoServicer(), self.server)
        add_HealthServicer_to_server(HealthServicer(), self.server)

    def setup_insecure_server(self):
        self.server.add_insecure_port("[::]:{insecure_port}".format(insecure_port=GRPC_INSECURE_PORT))

    def serve(self):
        self.server.start()
        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            self.server.stop(0)


if __name__ == "__main__":
    server = Server()
    server.setup_insecure_server()
    server.serve()
