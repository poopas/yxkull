
import numpy
import numpy.linalg

from pos import pos
from entity import Entity

class Player(Entity):
    def __init__(self, engine, color, axis_get_func):
        Entity.__init__(self, engine)
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
        Entity.process(self)

        self.pos += self.velocity
        self.velocity *= 0.8 


