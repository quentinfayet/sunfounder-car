import socket

class TcpServer:

    _host = None
    _port = None
    _buffer_size = None
    _adress = None
    _socket = None

    def __init__(self, host='', port=4242, buffer_size=1024):
        self._host = host
        self._port = port
        self._buffer_size = buffer_size
        self._adress = (self._host, self._port)

    def connect(self, max_pool_connections = 5):
        if self._sock is None:
            self._create_socket();
        self._socket.bind(self._adress)
        self._socket.listen(max_pool_connections)

    def _create_socket(self):
        if self._sock is None:
            self._sock = socket.socket(socket.AF_INET, socker.SOCK_STREAM);

    def receive(self):
        if self._socket is None:
            raise RuntimeError("Socket must be connected first!")

        return self._socket.recv(self._buffer_size)
