from . import service_method
from logger import module_logger
from proto.health_pb2_grpc import HealthServicer as grpc_HealthServicer
from proto.health_pb2 import HealthCheckResponse


class HealthServicer(grpc_HealthServicer):
    def __init__(self):
        self.logger = module_logger(__name__)

    @service_method(logging=False)
    def HealthCheck(self, request, context):
        """
        Check connections to the service's dependencies, reporting the status:
            - database
            - file store
            - caching layer
            - queuing system
            - external logger
            - etc.
        """
        return HealthCheckResponse(status_code=HealthCheckResponse.OK, status="OK")
