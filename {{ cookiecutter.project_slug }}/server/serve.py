import logging
import signal
import time

from concurrent import futures

import grpc

from logger import module_logger
from proto.health_pb2_grpc import add_HealthServicer_to_server
from servicers.health import HealthServicer
from proto.system_info_pb2_grpc import add_SystemInfoServicer_to_server
from servicers.system_info import SystemInfoServicer

GRPC_MAX_WORKERS = 10
GRPC_INSECURE_PORT = 50050
GRPC_SECURE_PORT = 50051

logger = module_logger(__name__)


class Server(object):
    def __init__(self):
        self._create_server()
        self._add_servicers()

    def _create_server(self):
        logger.info("Creating server")
        logger.debug("ThreadPoolExecutor.max_workers = %s", GRPC_MAX_WORKERS)
        self.server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=GRPC_MAX_WORKERS),
            options=self._server_options(),
        )

    def _server_options(self):
        server_options = (
            ("grpc.keepalive_time_ms", 20000),  # send keepalive every x milliseconds
            (
                "grpc.keepalive_timeout_ms",
                5000,
            ),  # keepalive ping time out after x milliseconds
            (
                "grpc.keepalive_permit_without_calls",
                True,
            ),  # allow keepalive pings when there's no gRPC calls
            (
                "grpc.http2.max_pings_without_data",
                0,
            ),  # allow unlimited amount of keepalive pings without data
            (
                "grpc.http2.min_time_between_pings_ms",
                10000,
            ),  # allow grpc pings from client every x milliseconds
            (
                "grpc.http2.min_ping_interval_without_data_ms",
                5000,
            ),  # allow grpc pings from client without data every x milliseconds
        )
        logger.debug("Server options: {}".format(server_options))
        return server_options

    def _add_servicers(self):
        logger.info("Adding servicers")
        logger.debug("Adding HealthServicer")
        add_HealthServicer_to_server(HealthServicer(), self.server)
        logger.debug("Adding SystemInfoServicer")
        add_SystemInfoServicer_to_server(SystemInfoServicer(), self.server)

    def setup_insecure_server(self):
        logger.info("Setting up an insecure server.")
        self.server.add_insecure_port(
            "[::]:{insecure_port}".format(insecure_port=GRPC_INSECURE_PORT)
        )
        logger.info("Listening on [::]:%s (insecure)", GRPC_INSECURE_PORT)

    def serve(self):
        logger.info("Starting server")
        self.server.start()
        try:
            logger.info("Server ready!!!")
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            logger.warn("Gracefully stopping server")
            logging.shutdown()
            self.server.stop(0)


def handle_sigterm(*args):
    logger.warn("SIGTERM issued")
    raise KeyboardInterrupt()


signal.signal(signal.SIGTERM, handle_sigterm)


if __name__ == "__main__":
    server = Server()
    server.setup_insecure_server()
    server.serve()
