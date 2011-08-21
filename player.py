
import numpy

from pos import pos

class Player(object):
    def __init__(self, color, axis_get_func):
        self.color = color
        self.get_axis = axis_get_func
        self.pos = pos(0, 0) 
        self.velocity = pos(0, 0)
        self._speed = 1.0
        self.radius = 10

    def apply_control(self, x, y):
        self.velocity[0] += x * self._speed
        self.velocity[1] += y * self._speed

    def process(self):
        self.pos += self.velocity
        self.velocity *= 0.8 
