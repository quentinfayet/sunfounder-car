from .network import TcpServer
from observable import Observable
from event import Instruction

class Server(Observable):

    _tcpServer = None

    def __init__(self):
        self._tcpServer = TcpServer()

    def run(self):
        while True:
            self._tcpServer.connect()

            while True:
                data = None
                data = self._tcpServer.receive()
                if data:
                    instruction = Instruction(data)
                    self.fire(instruction)
                else:
                    break
