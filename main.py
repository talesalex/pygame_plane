# -*- coding:utf-8 -*-
#Luciano Camargo Cruz (lccruz)
#luciano@hadi.com.br

import pygame
from Plane import Plane

def main():
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Plane Pygame")
    
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))

    plane = Plane()
    airplanes = pygame.sprite.Group(plane)
    
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    plane.plane_left()

        airplanes.clear(screen, background)
        airplanes.draw(screen)
        pygame.display.flip()

    
if __name__ == "__main__":
    pygame.init()
    main()
