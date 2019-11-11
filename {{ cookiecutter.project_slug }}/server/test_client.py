import time

from socket import gethostname, gethostbyname

import grpc

from proto import system_info_pb2_grpc
from proto.system_info_pb2 import SystemInfoRequest, ClientInfo, HostInfo


class TestClient(object):
    def __init__(self):
        self.channel = grpc.insecure_channel("localhost:50050")
        self.setup_stubs()

    def setup_stubs(self):
        self.system_info_stub = system_info_pb2_grpc.SystemInfoStub(self.channel)

    def get_system_info(self):
        hostname = gethostname()
        ip_addr = gethostbyname(hostname)
        response = self.system_info_stub.SystemInfo(
            SystemInfoRequest(
                client_info=ClientInfo(
                    host_info=HostInfo(
                        hostname=hostname,
                        ip_addr=ip_addr,
                        port=50050,
                        timestamp=int(time.time()),
                    )
                )
            )
        )
        return response


if __name__ == "__main__":
    client = TestClient()
    print(client.get_system_info())
