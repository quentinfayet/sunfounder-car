from .network import TcpServer
from observable import Observable, Observer
from event import Instruction


class Server(Observable, Observer):
    """Describes the main server routine.

        Attributes:
            _tcpServer (:obj:`TcpServer`): The TCP server handling the
                communication through sockets
    """
    _tcpServer = None

    def __init__(self):
        self._tcpServer = TcpServer()

    def run(self):
        """Defines the main server loop.
        """
        while True:
            self._tcpServer.connect()

            while True:
                data = None
                data = self._tcpServer.receive()
                if data:
                    instruction = Instruction(data[:-1], self)
                    self.fire(instruction)
                else:
                    break

    def handle(self, event):
        """Implementation of the :obj:`Observer` event handling method

            Args:
                event (:obj:`Event`): The received event
        """
        print('Event received ', event.get_value())
