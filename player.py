import random
import time

from laser import *
from loader import *
import pygame
from pygame.locals import *


### DIRECCOES:
### 0 - NORTE
### 1 - ESTE
### 2 - SUL
### 3- OESTE
class Player(pygame.sprite.Sprite):

    def __init__(self,posicao, keypresset,playernum,shiptype,numkills):
        pygame.sprite.Sprite.__init__(self)
        self.keys = keypresset
        self.playernum = playernum
        self.dx = 0
        self.dy = 0
        self.angle = 0
        self.lastDir = 0
        self.damage_multiplier = 1
        self.shiptype = shiptype
        self.curweapon=0;
        self.ammo = 10
        self.mines_ammo = 10
        self.empty = load_sound("click.wav")
        # powerup variables
        # guarda o instante em milisegundos em que apanhou o powerup
        self.powerup_time = 0
        self.timer = 0
        
        ##criar caracteristicas da nave
        self.__ship_type(shiptype)

        self.coordinates = posicao
        self.respawnpos = self.coordinates
   
        #colocar nave em posicao inicial
        self.rect.center = self.respawnpos


        ##array que guarda estatisticas do jogador
        # 0 - numero de vidas que tem
        # 1 - numero tiros disparados
        # 2 - numero tiros certeiros
        # 3 - numero pontos
        self.statistics = [numkills,0,0,0]

        self.isDead = False
        self.playernum = playernum




    def __respawn(self,statistics):
        pygame.sprite.Sprite.__init__(self)
        
        sound = load_sound('respawn.wav')
        sound.set_volume(0.3)
        self.dx = 0
        self.dy = 0
        #self.angle = 0
        #self.lastDir = 0
        #self.lasertimer = 0
        #self.lasermax = 5
        self.hitpoints = self.maxhitpoints
        self.curweapon=0;
        # powerup variables
        # guarda o instante em milisegundos em que apanhou o powerup
        self.powerup_time = 0
        self.timer = 0
        self.ammo = 10
        self.mines_ammo = 10
        #colocar nave em posicao inicial
        respawnx = random.randrange(40,950)
        respawny = random.randrange(40,710)
        self.respawnpos = (respawnx,respawny)
        self.rect.center = self.respawnpos
        self.coordinates = self.respawnpos
        # powerup variables
        # guarda o instante em milisegundos em que apanhou o powerup
        self.powerup_time = 0
        self.timer = 0
        self.damage_multiplier = 1
        self.statistics = statistics
        self.isDead = False
        
        sound.play()

    def get_hitpoints(self):
        return self.hitpoints

    def set_hitpoints(self,num):
        self.hitpoints = self.hitpoints+num

        

    def update(self,screen):
        
        #se diferente de 0, entao apanhou um power up ou tem algum power up activo
        #ligar relogio
        if self.powerup_time == 1:
            
            self.timer = time.clock()
            self.powerup_time = 2

        if self.powerup_time == 2:
            elapsed = time.clock()

        
            #se passaram 10 segundos, acabou o buff de dano
            if  round(elapsed - self.timer) == 10.0:
                self.damage_multiplier = 1
                self.powerup_time = 0
                
        #mover player
        
        self.rect.move_ip((self.dx*self.vmax, self.dy*self.vmax))
      
        
        if self.rect.top >= 0 and self.rect.bottom <= 740 and self.rect.left >= 0 and self.rect.right <= 1000:
            self.coordinates = (self.coordinates[0] + self.dx , self.coordinates[1]+self.dy)        
        else:
            if self.rect.top < 0:
                self.rect.top = 0
                self.dx = 0
                self.dy = 0
            elif self.rect.bottom > 730:
                self.rect.bottom = 730
                self.dx = 0
                self.dy = 0
            if self.rect.left < 0:
                self.rect.left = 0
                self.dx = 0
                self.dy = 0
            elif self.rect.right > 1000:
                self.rect.right = 1000
                self.dx = 0
                self.dy = 0
 

        self.barpoints = self.__calc_barpoints(self.hitpoints,self.maxhitpoints)


        #actualizar barra de vida em funcao da nave e da sua sprite
        if self.shiptype == 1:
            self.healthbar = pygame.Rect((self.rect.centerx-25,self.rect.centery+26),(self.barpoints,5))
        elif self.shiptype == 2:
            self.healthbar = pygame.Rect((self.rect.centerx-28,self.rect.centery+34),(self.barpoints,5))
        elif self.shiptype == 3:
            self.healthbar = pygame.Rect((self.rect.centerx-31,self.rect.centery+32),(self.barpoints,5))
        else:
            self.healthbar = pygame.Rect((self.rect.centerx-29,self.rect.centery+31),(self.barpoints,5))
            

        #Fire the laser
        
        key = pygame.key.get_pressed()
        if key[self.keys[4]]:
            if (self.curweapon == 1 and self.ammo >0) or self.curweapon == 0:
                
                self.lasertimer = self.lasertimer + 1
                if self.lasertimer == self.lasermax:
                    if self.lastDir == 0:
                        laser = Laser(self.rect.midtop,self.shiptype, self.curweapon, 90, self.playernum)
                    if self.lastDir == 1:
                         laser = Laser(self.rect.midleft,self.shiptype, self.curweapon, 180, self.playernum)
                    if self.lastDir == 2:
                         laser = Laser(self.rect.midbottom,self.shiptype, self.curweapon, -90, self.playernum)
                    if self.lastDir == 3:
                         laser = Laser(self.rect.midright,self.shiptype, self.curweapon, 0, self.playernum)

                    if self.curweapon == 1:
                        self.ammo = self.ammo -1
                    if self.curweapon == 2:
                        self.mines_ammo = self.mines_ammo -1

                    laser.spin(self.lastDir)
                    self.laserSprite.add(laser)
                    self.lasertimer = 0
                    self.statistics[1]+=1
                    
                    if self.curweapon == 1:
                        self.lasersound2.play()
                    else:
                        self.lasersound1.play()
                        
                    
            elif self.curweapon == 2 and self.mines_ammo >0:
                self.lasertimer = self.lasertimer + 1
                if self.lasertimer == self.lasermax:
                    if self.lastDir == 0:
                        laser = Laser(self.rect.midtop,self.shiptype, self.curweapon, 90, self.playernum)
                    if self.lastDir == 1:
                         laser = Laser(self.rect.midleft,self.shiptype, self.curweapon, 180, self.playernum)
                    if self.lastDir == 2:
                         laser = Laser(self.rect.midbottom,self.shiptype, self.curweapon, -90, self.playernum)
                    if self.lastDir == 3:
                         laser = Laser(self.rect.midright,self.shiptype, self.curweapon, 0, self.playernum)


                    self.mines_ammo = self.mines_ammo -1

                    laser.spin(self.lastDir)
                    self.laserSprite.add(laser)
                    self.lasertimer = 0
                    self.statistics[1]+=1
                    self.minesound.play()
            else:
                self.empty.play()


        #quando actualiza o proprio jogador, actualiza e desenha os seus lasers
        self.laserSprite.update()
        self.laserSprite.draw(screen)


    def changeWeapon(self):
     
        sound = load_sound('powerupweapon.wav')
        self.curweapon = (self.curweapon+1)%3;
        
        sound.play();
           

    def spin(self, angle, dir):
        rotate = pygame.transform.rotate
        if self.lastDir != dir:

            if (self.lastDir +1)%4 == dir:
                self.angle = angle
            elif (self.lastDir -1)%4 == dir:
                self.angle = -angle
            else:
                self.angle = angle*2
            self.lastDir = dir
            self.image = rotate(self.image, self.angle)

        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def draw_health(self,screen):
        if(self.hitpoints >= 20):
            pygame.draw.rect(screen,(255,0,0),self.healthbar)
        else:
            pygame.draw.rect(screen,(150,0,0),self.healthbar)


    def draw_stats(self,screen):
        font = pygame.font.SysFont("consola", 20)
        if self.curweapon == 0:
            weapon_selected = "Lasers  - inf."
        elif self.curweapon == 1:
            weapon_selected = "Blaster - "+str(self.ammo)
        else:
            weapon_selected = "Mines   - "+str(self.mines_ammo)

        if self.shiptype == 1:
            coords = (self.rect.centerx-30,self.rect.centery+31)
            
            if self.curweapon == 0:
                mult = font.render(weapon_selected, True, (255,255,255))
            elif self.curweapon == 1:
                if self.ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.ammo <= 5 and self.ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            elif self.curweapon == 2:
                if self.mines_ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.mines_ammo <= 5 and self.mines_ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            screen.blit(mult, coords)
            coords = (self.rect.centerx-50,self.rect.centery+28+15)
        elif self.shiptype == 2:
            coords = (self.rect.centerx-30,self.rect.centery+39)
            
            if self.curweapon == 0:
                mult = font.render(weapon_selected, True, (255,255,255))
            elif self.curweapon == 1:
                if self.ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.ammo <= 5 and self.ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            elif self.curweapon == 2:
                if self.mines_ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.mines_ammo <= 5 and self.mines_ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            screen.blit(mult, coords)
            coords = (self.rect.centerx-50,self.rect.centery+38+15)
        elif self.shiptype == 3:
            coords = (self.rect.centerx-32,self.rect.centery+38)
            
            if self.curweapon == 0:
                mult = font.render(weapon_selected, True, (255,255,255))
            elif self.curweapon == 1:
                if self.ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.ammo <= 5 and self.ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            elif self.curweapon == 2:
                if self.mines_ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.mines_ammo <= 5 and self.mines_ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            screen.blit(mult, coords)
            coords = (self.rect.centerx-51,self.rect.centery+40+15)
        else:
            coords = (self.rect.centerx-30,self.rect.centery+37)
            
            if self.curweapon == 0:
                mult = font.render(weapon_selected, True, (255,255,255))
            elif self.curweapon == 1:
                if self.ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.ammo <= 5 and self.ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            elif self.curweapon == 2:
                if self.mines_ammo > 5:
                    mult = font.render(weapon_selected, True, (255,255,255))
                elif self.mines_ammo <= 5 and self.mines_ammo > 0:
                    mult = font.render(weapon_selected, True, (255,165,0))
                else:
                    mult = font.render(weapon_selected, True, (180,0,0))
            screen.blit(mult, coords)
            coords = (self.rect.centerx-51,self.rect.centery+38+15)

        
        
        if self.damage_multiplier == 2:
            string = "Double Damage"
            mult = font.render(string, True, (255,255,255))
            screen.blit(mult, coords)
        elif self.damage_multiplier == 4:
            string = "Quad Damage!!"
            mult = font.render(string, True, (255,0,0))
            screen.blit(mult, coords)
        
        
        

    def kill_player(self):
        self.healthbar = pygame.Rect((self.coordinates[0]-25,self.coordinates[1]+35),(0,0))
        self.statistics[0] -= 1
        
        if self.statistics[0]<=0:
            self.kill()
            self.isDead = True
            return 1
        else:
            self.__respawn(self.statistics)
        
        return 0

    def __calc_barpoints(self,num,hitmax):
        #percentagem de vida que jogador tem
        life = (num * 100) / hitmax

        return (life * self.rect.width) / 100
        

    def __ship_type(self,shipnumber):

        #armas
        # indice 0 - Laser
        # indice 1 - ...
        # indice 2 - ...

        #lista com armas do jogador.
        # 1- disponivel
        # 0- indisponivel
        self.weapons = [1,0,0]

        if shipnumber == 1:
            self.image, self.rect = load_image('nave1.png', -1)
            #lista com danos das armas do player
            self.weapon_damage = [-1,-5,-10]
            self.maxhitpoints = 40
            self.hitpoints = 40
            self.barpoints = self.__calc_barpoints(self.hitpoints,self.maxhitpoints)
            self.vmax = 1
            self.lasertimer = 0
            self.lasermax = 8
            self.lasersound1 = load_sound("1_1.wav")
            self.lasersound2 = load_sound("1_2.wav")

        elif shipnumber == 2:
            self.image, self.rect = load_image('nave2.png', -1)
            #lista com danos das armas do player
            self.weapon_damage = [-1,-5,-10]
            self.maxhitpoints = 50
            self.hitpoints = 50
            self.barpoints = self.__calc_barpoints(self.hitpoints,self.maxhitpoints)
            self.vmax = 0.8
            self.lasertimer = 0
            self.lasermax = 5
            self.lasersound1 = load_sound("2_1.wav")
            self.lasersound2 = load_sound("2_2.wav")

        elif shipnumber == 3:
            self.image, self.rect = load_image('nave3.png', -1)
            #lista com danos das armas do player
            self.weapon_damage = [-1,-5,-10]
            self.maxhitpoints = 75
            self.hitpoints = 75
            self.barpoints = self.__calc_barpoints(self.hitpoints,self.maxhitpoints)
            self.vmax = 0.6
            self.lasertimer = 0
            self.lasermax = 5
            self.lasersound1 = load_sound("3_1.wav")
            self.lasersound2 = load_sound("3_2.wav")

        elif shipnumber == 4:
            self.image, self.rect = load_image('nave4.png', -1)
            #lista com danos das armas do player
            self.weapon_damage = [-5,-10,-10]
            self.maxhitpoints = 100
            self.hitpoints = 100
            self.barpoints = self.__calc_barpoints(self.hitpoints,self.maxhitpoints)
            self.vmax = 0.5
            self.lasertimer = 0
            self.lasermax = 20
            self.lasersound1 = load_sound("4_1.wav")
            self.lasersound2 = load_sound("4_2.wav")

        else:
            self.image, self.rect = load_image('nave5.png', -1)
            #lista com danos das armas do player
            self.weapon_damage = [-5,-10,-10]
            self.maxhitpoints = 100
            self.hitpoints = 100
            self.barpoints = self.__calc_barpoints(self.hitpoints,self.maxhitpoints)
            self.vmax = 0.4
            self.lasertimer = 0
            self.lasermax = 20
            self.lasersound1 = load_sound("5_1.wav")
            self.lasersound2 = load_sound("5_2.wav")

        
        self.minesound = load_sound("mine.wav")    

        #guardar os seus proprios lasers
        self.laserSprite = pygame.sprite.RenderPlain(())
        
