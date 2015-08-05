from animation import *
from loader import *
import pygame
from pygame.locals import *


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos,shipnumber, weapon, dir, playernum):
        pygame.sprite.Sprite.__init__(self)
        rotate = pygame.transform.rotate
        if playernum == 1:
            self.mine = load_sliced_sprites(16,16,'mina_blue_16x16.PNG')
        else:
            self.mine = load_sliced_sprites(16,16,'mina_red_16x16.PNG')
        if shipnumber == 1:
            self.name = "fireb_43x26.PNG"
            self.laserFire = load_sliced_sprites(43,26,'fireb_43x26.PNG')
            self.laserFireAlt =  load_sliced_sprites(105,39,'tiro fixe_105x39.PNG')
        elif shipnumber == 2:
            self.name = "lile_frost_40x22.PNG"
            self.laserFire = load_sliced_sprites(40,22,self.name)
            self.laserFireAlt =  load_sliced_sprites(67,35,'frost_bolt_67x35.PNG')
        elif shipnumber == 3:
            self.name = "fire_34x34.PNG"
            self.laserFire = load_sliced_sprites(34,34,self.name)
            self.laserFireAlt =  load_sliced_sprites(72,45,'fireball_72x45.PNG')
        elif shipnumber == 4:
            self.name = "tiro_magico_50x33.PNG"
            self.laserFire = load_sliced_sprites(50,33,self.name)
            self.laserFireAlt =  load_sliced_sprites(100,60,'deathblow_100x60.PNG')
        else:
            self.name = "frost_arrow_42x34.PNG"
            self.laserFire = load_sliced_sprites(42,34,self.name)
            self.laserFireAlt =  load_sliced_sprites(34,49,'ring_34x49.PNG')
        count = 0
        for img in self.laserFire:
            self.laserFire[count] = rotate(self.laserFire[count], dir)
            count = count +1
        count = 0
        for imgAlt in self.laserFireAlt:
           self.laserFireAlt[count] = rotate (self.laserFireAlt[count], dir)
           count = count +1
        count = 0
        for imgAlt in self.mine:
           self.mine[count] = rotate (self.mine[count], dir)
           count = count +1
        count = 0
        self.image = self.laserFire[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 0
        self.lastDir = 0
        self.impactpoint = (0,0)
        self.count = 0
        self.weapon = weapon


    #0 norte 1 este 2 sul 3 oeste
    def update(self):

        if self.weapon == 2:
            self.count = (self.count+1)%len(self.mine)
            self.image = self.mine[self.count]
        elif self.weapon == 1:
            self.count = (self.count+1)%len(self.laserFireAlt)
            self.image = self.laserFireAlt[self.count]
        elif self.weapon == 0:
            self.count = (self.count+1)%len(self.laserFire)
            self.image = self.laserFire[self.count]
        if self.rect.top < 0 or self.rect.bottom > 768 or self.rect.left < 0 or self.rect.right > 1024:
            self.kill()
        if self.weapon != 2:
            if self.lastDir == 0:
                self.impactpoint = (self.rect.centerx-10,self.rect.top-20)
                self.rect.move_ip(0, -15)
            if self.lastDir == 1:
                self.impactpoint = (self.rect.left-25,self.rect.centery-10)
                self.rect.move_ip(-15, 0)
            if self.lastDir == 2:
                self.impactpoint = (self.rect.centerx-10,self.rect.bottom)
                self.rect.move_ip(0, 15)
            if self.lastDir == 3:
                self.impactpoint = (self.rect.right+5,self.rect.centery-10)
                self.rect.move_ip(15, 0)
        else:
            if self.lastDir == 0:
                self.impactpoint = (self.rect.centerx-10,self.rect.top-20)
            if self.lastDir == 1:
                self.impactpoint = (self.rect.left-25,self.rect.centery-10)
            if self.lastDir == 2:
                self.impactpoint = (self.rect.centerx-10,self.rect.bottom)
            if self.lastDir == 3:
                self.impactpoint = (self.rect.right+5,self.rect.centery-10)
                


        
            
    def spin(self, dir):
        rotate = pygame.transform.rotate
        if self.lastDir != dir:

            if (self.lastDir +1)%4 == dir:
                self.angle = 90
            elif (self.lastDir -1)%4 == dir:
                self.angle = -90
            else:
                self.angle = 90*2
            self.lastDir = dir
            self.image = rotate(self.image, self.angle)

        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    



