class Value:
    """Stores event raw value.

        Attributes:
            _value: The value to be stored. Raw value.
    """

    _value = None

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value
