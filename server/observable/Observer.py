from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """Abstract class defining an observer. Handle method must be implemented.
    """

    @abstractmethod
    def handle(self, event):
        """Abstract method defining how the :obj:`Osberver` should react to
            any incoming event.
        """
        pass
