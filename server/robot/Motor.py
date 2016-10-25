from event import Event


class Motor:
    def handle(self, event):
        print('Received ', event.get_value())
        response = Event('hello')
        event.respond_to_emmiter(response)
