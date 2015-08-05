# -*- coding: utf-8 -*-
import math
import random
import sys

import pygame
from pygame.locals import *


#constantes
SCREENSIZE = [1024, 768]
WINCENTRE = [512,384]#representa o centro da janela
NUM_ESTRELAS = 250
white = 239, 240, 231
black = 0, 0, 0
yellow = 219,220,211
FACTOR = 2

class StarField():    

    def __init__(self,screen):
        self.screen = screen
        random.seed()
        self.estrelas = []
        self.init_estrelado()
        

    def increase_factor(x):
        FACTOR = FACTOR * x

    def increase_stars(x):
        NUM_ESTRELAS = NUM_ESTRELAS + x

    def init_estrela(self):

        direccao = random.randrange(100000)
        multiplicador = random.random() * FACTOR * .6 + .4
        velocidade = [math.sin(direccao) * multiplicador, math.cos(direccao) * multiplicador]
        #WINCENTRE[:] retorna uma copia do WINCENTRE, e nao a referencia
        return velocidade, WINCENTRE[:]

    def init_estrelado(self):
        
        for x in range(NUM_ESTRELAS):
            estrela = self.init_estrela()
            vel, pos = estrela

            #gerar posicao inicial aleatoria
            #screensize[0] pois ?? o valor maior do screensize
            #print SCREENSIZE
            steps = random.randint(0, WINCENTRE[0])
            #a minha posicao no x e no y vai ser a anterior mais qq coisa
            pos[0] = pos[0] + (vel[0] * steps)
            pos[1] = pos[1] + (vel[1] * steps)
            #a minha velocidade segundo x e y vai ser a anterior mais qq coisa
            #aumentar velocidade de saida inicial
            vel[0] = vel[0] * (steps * .09)
            vel[1] = vel[1] * (steps * .09)

            #guardo a estrela
            self.estrelas.append(estrela)


    def mover_estrelas(self,estrelas):
        #para cada estrela no ceu
        #aumentamos a posicao segundo a velocidade no XX e YY
        for vel, pos in estrelas:
            pos[0] = pos[0] + vel[0]
            pos[1] = pos[1] + vel[1]
            #se a estrela nao estiver entre as dimensoes da janela, isto e
            #se sai fora do ecra, geramos uma nova estrela
            if not 0 <= pos[0] <= SCREENSIZE[0] or not 0 <= pos[1] <= SCREENSIZE[1]:
                vel[:], pos[:] = self.init_estrela()
            #senao, multiplicamos ligeiramente a sua velocidade
            else:
                vel[0] = vel[0] * 1.05
                vel[1] = vel[1] * 1.05


    def desenhar_estrelas(self,ecra, estrelas, cor):
        for vel, pos in estrelas:
            pos = (int(pos[0]), int(pos[1]))
            ecra.set_at(pos, cor)


    def update(self):
        self.desenhar_estrelas(self.screen, self.estrelas, yellow)
        self.mover_estrelas(self.estrelas)
        self.desenhar_estrelas(self.screen, self.estrelas, white)

            

    
