import math
import random

from loader import *
import pygame
from pygame.locals import *


class Asteroid(pygame.sprite.Sprite):
    def __init__(self,num):
        pygame.sprite.Sprite.__init__(self)
        #Para garantir o maximo de aleatoriedade possivel
        listagem=[1,2,3,4,5,6,7,8,9,10]
        random.shuffle(listagem)
        random.shuffle(listagem)
        i=random.uniform(0,9)
        if listagem[int(i)] >= 3 and listagem[int(i)] <= 5:
            if listagem[int(i)] == 3:
                picture="asteroid_pekeno1.png"
            elif listagem[int(i)] == 4:
                picture="asteroid_pekeno2.png"
            else:
                picture="asteroid_pekeno3.png"
            self.hitpoints = 10
        elif listagem[int(i)] < 3:
            if listagem[int(i)] >=1 and listagem[int(i)]<=2:
                picture="crazyAlien.gif"
                self.hitpoints = 20
            else:
                picture="spaceGosma.png"
                self.hitpoints=15
        else:
            listagem=[2,1]
            random.shuffle(listagem)
            if listagem[0]==1:
                picture="crazyDoc.png"
                self.hitpoints = 5
            else:
                picture="crazyship1.gif"
                self.hitpoints = 11

        self.image, self.rect = load_image(picture, -1)
        self.Sprite = pygame.sprite.RenderPlain(())
        
        self.num = num
        self.screensize = [1120,840]
        
        modifier = random.randrange(0,2)
        if modifier == 0:
            modifier = -1
        else:
            modifier = 1
        multiplicador1 = (random.randrange(0,4)+1)*modifier

        modifier = random.randrange(0,2)
        if modifier == 0:
            modifier = -1
        else:
            modifier = 1
        multiplicador2 = (random.randrange(0,4)+1)*modifier

        self.vel = [multiplicador1, multiplicador2]
        #self.pos = [random.randrange(0,960)+40,random.randrange(0,660)+40]
        self.pos = [self.screensize[0]/2,-100]
        self.rect.center = self.pos

    def update(self):
        
        self.rect.move_ip(self.vel[0], self.vel[1])
       # print "my coords: "+str(self.rect.center)
        self.pos[0] +=self.vel[0]
        self.pos[1] +=self.vel[1]
        
        if not -110 < self.pos[0] < self.screensize[0]:
                self.vel[0] = -self.vel[0]
            
        if not -110 < self.pos[1] < self.screensize[1]:
                self.vel[1] = -self.vel[1]

    def kill_asteroid(self):
        if self.hitpoints <=0:
            self.kill()
            return 1
        
        return 0

                

