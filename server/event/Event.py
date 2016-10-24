from observable import Observer

class Event:

    _value = None
    _emmiter = None

    def __init__(self, value, emmiter=None):
        self._value = value
        self._emmiter = emmiter

    def get_value(self):
        return self._value

    def respond_to_emmiter(self, event):
        if isinstance(self._emmiter, Observer):
            self._emmiter.handle(event)
