#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import Server
from controller import Direction, LightController


def main():
    server = Server()
    initialize_robot(server).run()


def initialize_robot(server):
    """Initializes all robot connections and subscribes events

        Args:
            server (:obj: `Server`): The main server
    """
    direction = Direction()
    server.subscribe(direction)

    lightController = LightController()
    server.subscribe(lightController)

    return server


if __name__ == '__main__':
    main()
