class Observable:
    """Defines an object that can be oberved by :obj:`Observer`s.

        Attributes:
            _observers (list): List of subscribing observers
    """
    _observers = list()

    def subscribe(self, observer):
        """Subscribes an :obj:`Observer` to this :obj:`Observable` object.

            Args:
                observer (:obj:`Observer`): The :obj: `Observer` which
                    subscribes to the :obj:`Observable`
        """
        self._observers.append(observer)

    def fire(self, event):
        """Fires an :obj:`Event` to the :obj:`Observer`s.

            Args:
                event (:obj:`Event`): The :obj:`Event` to be fired
        """
        for observer in self._observers:
            observer.handle(event)
