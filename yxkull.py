# Framework
import os
import sys

if 0:
    def stdspecial(object):
        def __init__(self, output):
            self.output

        def write(x):
            if x[:3] != "SDL":
                self.output.write("hej"+x)

    sys.stdout = stdspecial(sys.stdout) 
    sys.stderr = stdspecial(sys.stderr)

import pygame
from pygame.locals import *

# Project
from pos import pos
from player import Player

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize Everything
    pygame.init()
    WIDTH, HEIGHT = 1024, 768 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Yxkull')
    pygame.mouse.set_visible(0)

    #Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    
    # Joysticks
    PLAYERS = 4 
    JOYSTICKS = 2
    joysticks = [pygame.joystick.Joystick(i) for i in xrange(JOYSTICKS)]  

    players = []

    for i, j in enumerate(joysticks):
        j.init()
        print j.get_numaxes()


    axes = []
    for j in xrange(JOYSTICKS):
        for i in xrange(2):
            def _get_axis(axis, joysticks):
                return joysticks[j].get_axis(i*2+axis)            
            axes.append(_get_axis)

    #print axes

    colors = [(100, 0, 0), (0, 100, 0), (0, 0, 100), (100, 0, 100)]
    buf = 80.0
    positions = [pos(buf, buf), pos(WIDTH-buf, buf), pos(WIDTH-buf, HEIGHT-buf), pos(buf, HEIGHT-buf)]
    
    players = []
    for p in xrange(PLAYERS):
        player = Player(colors[p], axes[p])
        player.pos = positions[p]
        players.append(player)

    #players += [Player(j, (0, 100*(1-i), 100*i))]

    screen.blit(background, (0, 0))
    pygame.display.flip()


    clock = pygame.time.Clock()

    while 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return
            elif event.type == MOUSEBUTTONDOWN:
                pass
            elif event.type is MOUSEBUTTONUP:
                pass

        for j in xrange(JOYSTICKS):
            for i in xrange(2):
                p = players[j*2+i]
                p.apply_control(joysticks[j].get_axis(i*3), joysticks[j].get_axis(i*3+1))
    
    
        for p in players:
            p.process()

        if 0:
            for p1 in players:
                for p2 in players:
                    if p1.dist_to(p2) < 60.0:
                        pygame.draw.line(
    
        # Draw
        screen.blit(background, (0, 0))

        for p in players:
            pygame.draw.circle(screen, p.color, p.pos, p.radius) 

        pygame.display.flip()

        

if __name__ == '__main__': 
    main()
