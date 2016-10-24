from .network import TcpServer
from observable import Observable, Observer
from event import Instruction

class Server(Observable, Observer):

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
                    instruction = Instruction(data, self)
                    self.fire(instruction)
                else:
                    break

    def handle(self, event):
        print('Event received ', event.get_value())
