class Observable:

    _observers = list()

    def subscribe(self, observer):
        self._observers.append(observer)

    def fire(self, event):
        for observer in self._observers:
            observer.handle(event)
