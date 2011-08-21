
import numpy.linalg
from pos import pos

class Beam(object):
    def __init__(self):
        self.color = (0, 0, 0)
        self.width = 2
        self.damage = 10 
        self.pos1 = pos(0, 0)
        self.pos2 = pos(0, 0)

    def length(self):
        return numpy.linalg.norm(self.pos1 - self.pos2)

    def make_damage(self, entity):
        entity.damage(self.damage + 10000)
