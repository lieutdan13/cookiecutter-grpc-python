import time

from socket import gethostname, gethostbyname

from . import service_method
from proto.system_info_pb2_grpc import SystemInfoServicer as grpc_SystemInfoServicer
from proto.system_info_pb2 import SystemInfoResponse, ServerInfo, HostInfo


class SystemInfoServicer(grpc_SystemInfoServicer):

    @service_method
    def SystemInfo(self, request, context):
        hostname = gethostname()
        ip_addr = gethostbyname(hostname)

        return SystemInfoResponse(
            client_info=request.client_info,
            server_info=ServerInfo(
                host_info=HostInfo(
                    hostname=hostname,
                    ip_addr=ip_addr,
                    port=50051,
                    timestamp=int(time.time())
                )
            )
        )
