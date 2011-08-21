

from numpy import arange
import pygame
from random import randint
from beam import Beam
from pos import pos
from drone import Drone

class Engine(object):
    def __init__(self, size):
        self.players = []
        self.beams = []
        self.entities = []
        self.size = size

        self.playersprites = pygame.sprite.RenderPlain()
        self.entitysprites = pygame.sprite.RenderPlain() 


    def add_player(self, player):
        self.players.append(player)
        self.playersprites.add(player)

    def add_entity(self, entity):
        self.entities.append(entity)
        self.entitysprites.add(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)
        self.entitysprites.remove(entity)

    def process(self):
        self.spawn()

        # Entities
        deletes = []
        for p in self.entities:
            p.process()
            if p.die:
                deletes.append(p) 

        for d in deletes:
            self.remove_entity(d)
            


        # Players
        for p in self.players:
            p.process()
    
        self.process_beams()


        # Update sprites
        self.playersprites.update()
        self.entitysprites.update() 

    def process_beams(self):
        self.beams = []
        for p1 in self.players:
            for p2 in self.players:
                if p1.dist_to(p2.pos) < 120.0:
                    beam = Beam()
                    beam.pos1 = p1.pos
                    beam.pos2 = p2.pos
                    beam.damage = 3

                    self.beams.append(beam)

        # Make the beams take damage!
        if 0:
            for beam in self.beams:
                length = beam.length() 
                for t in arange(0, length, 3.0):
                    pos = beam.pos1 + (beam.pos2 - beam.pos1) * length
                    for ent in self.entities:
                        if ent.dist_to(pos) <= ent.radius:
                            beam.make_damage(ent)

    def spawn(self):
        if randint(0, 20) == 0:
            drone = Drone(self)
        
            drone.pos = pos(randint(0, self.size[0]), -drone.radius-2)
            self.add_entity(drone)


    def draw(self, screen):
        self.entitysprites.draw(screen)
        self.playersprites.draw(screen)
