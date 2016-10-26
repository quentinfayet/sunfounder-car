import socket


class TcpServer:
    """Handles TCP communication between server and clients through sockets.

        Attributes:
            _host (str): The host. Empty host allows connection from any host.
            _port (int): The port the socket will listen on
            _buffer_size (int): Maximum reading buffer size for the socket
            _adress (tuple): Tuple defining the couple host/port
            _socket (:obj:`Socket`): The server socket
            _socketClient (): The opened socket through the client
    """
    _host = None
    _port = None
    _buffer_size = None
    _adress = None
    _socket = None
    _socketClient = None

    def __init__(self, host='', port=4242, buffer_size=1024):
        """Initializes the :obj:`TcpServer`.

            Args:
                host (str, optional): The host. Default is ''.
                port (int, optional): The listening port. Default is 4242
                buffer_size (int, optional): The reading buffer size. Default
                    is 1024
        """
        self._host = host
        self._port = port
        self._buffer_size = buffer_size
        self._adress = (self._host, self._port)

    def connect(self, max_pool_connections=5):
        """Connects the socket to the port and waits for an incoming connection.

            Args:
                max_pool_connection (int, optional): The maximum number of
                    parallel connections allowed by the server.
        """
        if self._socket is None:
            self._create_socket()
            self._socket.bind(self._adress)
            self._socket.listen(max_pool_connections)

        print('Server is waiting for connections.')
        while True:
                self._socketClient, addr = self._socket.accept()

                if self._socketClient is not None:
                    print('Connected from ', addr)
                    return

    def _create_socket(self):
        """Creates the socket."""
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def receive(self):
        """Read data from the client through socket.

            Returns:
                str: The bytes read from the socket

            Raises:
                RuntimeError: The socket has not been initialized/connected to
                    the port or to a client.
        """
        if self._socket is None:
            raise RuntimeError("Socket must be connected first!")

        return self._socketClient.recv(self._buffer_size).decode('utf-8')
