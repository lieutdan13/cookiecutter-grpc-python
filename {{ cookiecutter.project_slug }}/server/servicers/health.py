from . import service_method
from proto.health_pb2_grpc import HealthServicer as grpc_HealthServicer
from proto.health_pb2 import HealthCheckResponse


class HealthServicer(grpc_HealthServicer):

    @service_method
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
        return HealthCheckResponse(status="OK")
