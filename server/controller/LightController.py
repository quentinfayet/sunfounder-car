from observable import Observer
from event import Event
import RPi.GPIO as GPIO
import time

RED = 11
GREEN = 12
BLUE = 13

class LightController(Observer):

    _gpios = None

    def __init__(self):
        for pin in (RED, GREEN, BLUE):
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH)

        self._gpios = {
            'red': GPIO.PWM(RED, 2000),
            'green': GPIO.PWM(GREEN, 1999),
            'blue': GPIO.PWM(BLUE, 5000),
        }


    def handle(self, event):
        event_value = event.get_value()

        if event_value['component'] != 'light':
            return

        #TODO : Add 'command' existence checking

        if event_value['command'] == 'setColor':
            self.setColor(int(event_value['color'], 0))


    def setColor(self, color):
        red_value = (color & 0xff0000) >> 16
        green_value = (color & 0x00ff00) >> 8
        blue_value = (color & 0x0000ff) >> 0

        red_value = self.map(red_value, 0, 255, 0, 100)
        green_value = self.map(green_value, 0, 255, 0, 100)
        blue_value = self.map(blue_value, 0, 255, 0, 100)

        print('changin color')

        self._gpios['red'].ChangeDutyCycle(100 - red_value)
        self._gpios['green'].ChangeDutyCycle(100 - green_value)
        self._gpios['blue'].ChangeDutyCycle(100 - blue_value)

        time.sleep(1)


    def map(self, value, in_min, in_max, out_min, out_max):
        return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
