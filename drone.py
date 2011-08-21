
from entity import Entity
from pos import pos

class Drone(Entity):
    def __init__(self, engine):
        Entity.__init__(self, engine)
        pass
        self.radius = 20 

    def process(self):
        Entity.process(self)

        self.pos = pos(self.pos[0], self.pos[1] + 0.5) 
        if self.pos[1]  > self.engine.size[1]:
            self.kill_self()


