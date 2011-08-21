

from numpy import arange
import pygame
from random import randint
from beam import Beam
from pos import pos
from drone import Drone
from collision import line_circle_intersect

class Engine(object):
    def __init__(self, size):
        self.players = []
        self.beams = []
        self.entities = []
        self.size = size
        self.points = 0 
        self.game_over = False

        self.playersprites = pygame.sprite.RenderPlain()
        self.entitysprites = pygame.sprite.RenderPlain() 


    def lose_point(self):
        self.points -= 1
        if self.points <= 0:
            # Game over
            self.game_over = True

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
        if not self.game_over:
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
        for beam in self.beams:
            length = beam.length() 

            for entity in self.entities:
                if line_circle_intersect(beam.pos1, beam.pos2, entity.pos, entity.radius):
                    beam.make_damage(entity)

    def spawn(self):
        if randint(0, 50) == 0:
            drone = Drone(self)
        
            drone.pos = pos(randint(20, self.size[0]-20*2), -drone.radius-2)
            self.add_entity(drone)


    def draw(self, screen):
        self.entitysprites.draw(screen)
        self.playersprites.draw(screen)

    def reset(self):

        buf = 0.0
        # Reset player positions
        #positions = [pos(buf, buf), pos(self.size[0]-buf, buf), pos(self.size[0]-buf, self.size[1]-buf), pos(buf, self.size[1]-buf)]
        positions = [pos(self.size[0]*(i+1)/(1.0 + len(self.players)), self.size[1]-80) for i in xrange(len(self.players))] 
        for i, p in enumerate(self.players):
            p.pos = positions[i]
            p.velocity = pos(0, 0)
        
        self.entities = []
        self.entitysprites = pygame.sprite.RenderPlain() 
    
        self.game_over = False
        self.points = 5
