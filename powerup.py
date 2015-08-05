import random

from loader import *
import pygame
from spritesheet import *


class Powerup(pygame.sprite.Sprite):
    #type e o tipo de powerups    
    def __init__(self,tipo,screen):
        pygame.sprite.Sprite.__init__(self)

        self.tipo = tipo
        if tipo == 1:
            #e um escudo
            ss = spritesheet('shields.png')
            #indice = random.randrange(0,8)
            indice = 7
            indicefinal = (indice)+20
            self.image = ss.image_at((indice*25, 0, indicefinal, 25),-1)
            self.rect = self.image.get_rect()
            self.som = load_sound('powerup.wav')
            self.som.play()

            #calcular factor de cura do escudo
            self.healfactor = 0
            i = 0
            while i <= indice:
                self.healfactor += 0.05
                i = i +1
            
        elif tipo == 2:
            ss = spritesheet('weapons.png')
            indice = random.randrange(0,2)
            indice += 1
            indicefinal = (indice)+20
            self.image = ss.image_at((indice*25, 0, indicefinal, 25),-1)
            self.rect = self.image.get_rect()
            self.som = load_sound('powerup.wav')
            self.som.play()


            #double ou quad damage
            if indice == 1:
                self.damagefactor = 2
                self.ammo = 5
            else:
                self.damagefactor = 4
                self.ammo = 10            
    
        elif tipo == 3:
            ss = spritesheet('weapons.png')
            indice = 0
            indicefinal = (indice)+20
            self.image = ss.image_at((indice*25, 0, indicefinal, 25),-1)
            self.rect = self.image.get_rect()
            self.som = load_sound('powerup.wav')
            self.som.play()

        randomx = random.randrange(70,screen[0]-70)
        randomy = random.randrange(70,screen[1]-70) 
        self.rect.center = (randomx,randomy)

def get_powerup_pos():
    return self.rect.center



