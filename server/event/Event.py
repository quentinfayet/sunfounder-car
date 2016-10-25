from observable import Observer
from .value import Value


class Event:
    """Describes an event. Base class to be inherited from.

        Attributes:
            _value (:obj: `Value`): The given value of the event.
            _emmiter (:obj:`Observable`): The emmiter of the event
    """
    _value = None
    _emmiter = None

    def __init__(self, raw_value, emmiter=None):
        """Initiates the event
            Args:
                raw_value (str): The value to be given to the event
                emmiter (str, optional): Emmiter of the event. Defaults
                    to None
        """
        self._create_appropriate_value(raw_value)
        self._emmiter = emmiter

    def get_value(self):
        return self._value.get_value()

    def respond_to_emmiter(self, event):
        """Send an event to the emmiter, in case emmiter is an :obj:`Observer`

            Args:
                event (:obj: `Event`): The event to be sent to the emmiter
        """
        if isinstance(self._emmiter, Observer):
            self._emmiter.handle(event)

    def _create_appropriate_value(self, value):
        self._value = Value(value)
