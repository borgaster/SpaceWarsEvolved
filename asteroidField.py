# -*- coding: utf-8 -*-
import math
import random
import sys

from asteroid import *
import pygame
from pygame.locals import *


class AsteroidField():    

    def __init__(self,screen):
        self.screen = screen
        self.num_asteroids = 5
        self.asteroids = []
        self.asteroidSprites = pygame.sprite.RenderPlain(())
        self.init_field()


    def init_field(self):

        for x in range(self.num_asteroids):
            asteroid = Asteroid(x)
            self.asteroidSprites.add(asteroid)
            self.asteroids.append(asteroid)

    def refresh(self,num):
        self.num_asteroids = num
        self.init_field()
        asteroids_left = self.num_asteroids
        return self.num_asteroids

    def update(self):
        self.asteroidSprites.update()
        self.asteroidSprites.draw(self.screen)

            

    
