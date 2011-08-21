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
from engine import Engine
from entity import load_image

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

def main():
    #Initialize Everything
    pygame.init()
    WIDTH, HEIGHT = 1024, 720 
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Yxkull')
    pygame.mouse.set_visible(0)

    #Create The Backgound
    if 1:
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))
    else:
        background, bg_rect = load_image('background.bmp')

    hud = None

    # Add walls to the background
    
    # Joysticks
    JOYSTICKS = pygame.joystick.get_count()
    PLAYERS = 2 * JOYSTICKS 
    joysticks = [pygame.joystick.Joystick(i) for i in xrange(JOYSTICKS)]  

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

    engine = Engine((WIDTH, HEIGHT))
    
    colors = [(100, 0, 0), (0, 100, 0), (0, 0, 100), (100, 0, 100)]
    
    for p in xrange(PLAYERS):
        player = Player(engine, colors[p], axes[p])
        #player.pos = positions[p]
        engine.add_player(player)

    #players += [Player(j, (0, 100*(1-i), 100*i))]

    screen.blit(background, (0, 0))
    pygame.display.flip()


    heart, heart_rect = load_image('heart.bmp', -1)
    num_hearts_generated = -1

    clock = pygame.time.Clock()

    engine.reset()

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
            elif event.type == KEYDOWN and event.key == K_SPACE:
                if engine.game_over:
                    engine.reset() 

        for j in xrange(JOYSTICKS):
            for i in xrange(2):
                p = engine.players[j*2+i]
                p.apply_control(joysticks[j].get_axis(i*3), joysticks[j].get_axis(i*3+1))
    
    
        engine.process()

        # Draw
        screen.blit(background, (0, 0))

        #for p in engine.entities:
            #pygame.draw.circle(screen, p.color, p.pos, p.radius) 

        #for p in engine.players:
        #    pygame.draw.circle(screen, p.color, p.pos, p.radius) 

        engine.draw(screen)

        for beam in engine.beams:
            pygame.draw.line(screen, beam.color, beam.pos1, beam.pos2, beam.width)

        if engine.game_over:
            #pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, WIDTH, HEIGHT))
            if pygame.font:
                font = pygame.font.Font(None, 36)
                text = font.render("Game Over", 1, (255, 255, 255))
                textpos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2)
                screen.blit(text, textpos)


        if num_hearts_generated != engine.points:
            hud = pygame.Surface(screen.get_size(), SRCALPHA)
            hud = hud.convert_alpha() 

            for i in xrange(engine.points):
                hud.blit(heart, (5+i*36, 5))

            num_hearts_generated = engine.points

        if hud:
            screen.blit(hud, (0, 0))

        pygame.display.flip()

        

if __name__ == '__main__': 
    main()
