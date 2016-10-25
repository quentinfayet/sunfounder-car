from . import Value
import json


class JsonValue(Value):
        """Stores a JSON value.
        """

        def _store_formated_value(self, raw_value):
            self._value = json.loads(raw_value)
