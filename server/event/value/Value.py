class Value:
    """Stores event raw value.

        Attributes:
            _value: The value to be stored
            _raw_value (bytes): The raw value
    """

    _value = None
    _raw_value = None

    def __init__(self, raw_value):
        self._store_formated_value(raw_value)
        self._raw_value = raw_value

    def get_value(self):
        return self._value

    def get_raw_value(self):
        return self._raw_value

    def _store_formated_value(self, raw_value):
        """Stores the formated value. This method should be overrided.

            Args:
                raw_value (bytes): the raw value
        """
        self._value = raw_value
