
from entity import Entity
from pos import pos

class Drone(Entity):
    def __init__(self, engine):
        Entity.__init__(self, engine)
        #self.radius = 20 

    def sprite_name(self):
        return 'drone.bmp'

    def process(self):
        Entity.process(self)

        speed = 0.8

        self.pos = pos(self.pos[0], self.pos[1] + speed) 
        if self.pos[1]  > self.engine.size[1]:
            self.engine.lose_point()
            self.kill_self()


