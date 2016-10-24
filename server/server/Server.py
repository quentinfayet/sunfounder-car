from .network import TcpServer

class Server:

    _tcpServer = None

    def __init__(self):
        self._tcpServer = TcpServer()

    def run(self):
        self._tcpServer.connect()

        while True:
            data = None
            data = self._tcpServer.receive()
