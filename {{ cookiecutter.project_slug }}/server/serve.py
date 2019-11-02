import time

from concurrent import futures

import grpc

from proto.system_info_pb2_grpc import add_SystemInfoServicer_to_server
from servicers.system_info_servicer import SystemInfoServicer

GRPC_MAX_WORKERS = 10
GRPC_INSECURE_PORT = 50050
GRPC_SECURE_PORT = 50051


class Server(object):
    def __init__(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=GRPC_MAX_WORKERS))
        self._add_servicers()

    def _add_servicers(self):
        add_SystemInfoServicer_to_server(SystemInfoServicer(), self.server)

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
