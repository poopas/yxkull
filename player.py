
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
        #self.radius = 10

    def sprite_name(self):
        return 'player.bmp'

    def apply_control(self, x, y):
        self.velocity[0] += x * self._speed
        self.velocity[1] += y * self._speed

    def process(self):
        Entity.process(self)

        self.pos += self.velocity

        wall_dist = 10.0
        buf = wall_dist + self.radius
        # Check position boundaries
        if self.pos[0] < buf:
           self.pos = pos(buf, self.pos[1]) 
        if self.pos[0] > self.engine.size[0]-buf:
           self.pos = pos(self.engine.size[0]-buf, self.pos[1]) 
        if self.pos[1] < buf:
            self.pos = pos(self.pos[0], buf)
        if self.pos[1] > self.engine.size[1]-buf:
            self.pos = pos(self.pos[0], self.engine.size[1]-buf)

        self.velocity *= 0.8 


