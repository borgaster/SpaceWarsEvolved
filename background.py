import os

import pygame
from pygame.locals import *


class Background():

    def __init__(self,screen,img):
        fullname = os.path.join('./img',img)
        self.background = pygame.image.load(fullname).convert()
        self.screen = screen
        self.screen.blit(self.background,(0,0))    

    def update(self):
        self.screen.blit(self.background,(0,0))
