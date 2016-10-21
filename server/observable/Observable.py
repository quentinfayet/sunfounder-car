class Observable:

    _observers = list()

    def subscribe(self, callback):
        self._observers.append(callback)

    def fire(self, event):
        for callback in self._observers:
            callback(event)
