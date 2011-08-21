
import os
import pygame
import numpy.linalg
from pos import pos
from pygame.locals import *


def load_image(name, colorkey=None):
    fullname = os.path.join('img', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Entity(pygame.sprite.Sprite):
    def __init__(self, engine):
        pygame.sprite.Sprite.__init__(self)
        self.load_sprite()

        #self.image = pygame.transform.scale(self.image, (48, 48))
        self.radius = self.rect.size[0]/2.0

        self.engine = engine
        self._pos = pos(0, 0)
        self.color = (0, 0, 0)
        self.die = False
        self.life = 100
        self.sprite = pygame.sprite.Sprite

    def sprite_name(self):
        return 'drone.bmp'

    def load_sprite(self):
        self.image, self.rect = load_image(self.sprite_name(), -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def getpos(self):
        return self._pos
       
    def setpos(self, val):
        self._pos = val
        self.rect.center = (self._pos[0], self._pos[1])

    pos = property(getpos, setpos)
    
    def process(self):
        pass

    def damage(self, damage):
        self.life -= damage

        self.radius = 3
        if self.life < 0:
            self.kill_self()

    def kill_self(self):
        self.die = True 

    def dist_to(self, pos):
        return numpy.linalg.norm(self.pos - pos) 
