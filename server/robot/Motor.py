class Motor:
    def handle(self, event):
        print('Received ', event.get_value())
