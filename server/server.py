#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import Server
from robot import Motor


def main():
    motor = Motor()
    server = Server()
    server.subscribe(motor)
    server.run()

if __name__ == '__main__':
    main()
