from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, event):
        pass
