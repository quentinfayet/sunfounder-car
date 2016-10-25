from observable import Observer
from event import Event


class Direction(Observer):
    def handle(self, event):
        print('Received ', event.get_value())
        response = Event('hello')
        event.respond_to_emmiter(response)
