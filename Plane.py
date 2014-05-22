# -*- coding:utf-8 -*-
# Luciano Camargo Cruz (lccruz)
# luciano@hadi.com.br

import pygame

class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imageMaster = pygame.image.load("image/air_plane_BLUE.png") #(40, 40)
        self.imageMaster = self.imageMaster.convert()
        self.image = self.imageMaster
        self.rect = self.image.get_rect()
        self.rect.center = (250, 200)
        self.speed = 2
        self.angulo = 0

    def update(self):
        pass
 
    def plane_left(self):
        self.rect.left -= self.speed
        return
