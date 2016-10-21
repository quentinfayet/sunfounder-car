class TcpServer:

    _host = None
    _port = None
    _buffer_size = None
    _adress = None

    def __init__(self, host='', port=21567, buffer_size=1024):
        self._host = host
        self._port = port
        self._buffer_size = buffer_size
        self._adress = (self._host, self._port)
