import random

from animation import *
from loader import *
import player
import pygame
from pygame.locals import *
from pygame.sprite import *


#lista de explosoes a desenhar
#init explosoes
explosoes = []

weapon_pickups = []
health_pickups = []

toasty = False

def asteroids(player1,player2,playerSprite1,playerSprite2,asteroidField):
        explosion_images = load_sliced_sprites(100,90,'kaboom.png')
        
        for hit in pygame.sprite.groupcollide(playerSprite1, asteroidField.asteroidSprites, 0, 1):
             __explosion()
             explosoes.append(AnimatedSprite(explosion_images,player1.coordinates[0],player1.coordinates[1]))
             if player1.kill_player():
                    
                    return 1

        if player2.shiptype != 0:
                for hit in pygame.sprite.groupcollide(playerSprite2, asteroidField.asteroidSprites, 0, 1):
                     __explosion()
                     explosoes.append(AnimatedSprite(explosion_images,player2.coordinates[0],player2.coordinates[1]))
                     if player2.kill_player():
                            
                            return 1
        return 0

def lasers(player1,player2,playerSprite1,playerSprite2,asteroidField):
        explosion_images = load_sliced_sprites(20,20,'explosion-sprite.png')

        # DETECTAR COLISOES ENTRE LASERS DO JOGADOR 1 E A NAVE DO JOGADOR 2
        # so se existe esse jogador.
        if player2.shiptype != 0:
                for hit in pygame.sprite.groupcollide(player1.laserSprite, playerSprite2, 1, 0):
                    __explosion()
                    explosoes.append(AnimatedSprite(explosion_images,hit.impactpoint[0],hit.impactpoint[1]))
                    hit.kill()
                    #aumentar tiros acertados
                    player1.statistics[2]+=1
                    #aumentar score
                    player1.statistics[3]+=3
                    player2.set_hitpoints(player1.weapon_damage[player1.curweapon]*player1.damage_multiplier)
                    if(player2.get_hitpoints() <= 0):
                        if player2.kill_player():
                           
                            return 1

        # DETECTAR COLISOES ENTRE LASERS DO JOGADOR 2 E A NAVE DO JOGADOR 1
        for hit in pygame.sprite.groupcollide(player2.laserSprite, playerSprite1, 1, 0):
            __explosion()
            explosoes.append(AnimatedSprite(explosion_images,hit.impactpoint[0],hit.impactpoint[1]))
            hit.kill()
            player2.statistics[2]+=1
            player2.statistics[3]+=3
            player1.set_hitpoints(player2.weapon_damage[player2.curweapon]*player2.damage_multiplier)
            if(player1.get_hitpoints() <= 0):
                if player1.kill_player()==1:
                    
                    return 1

        # DETECTAR COLISOES ENTRE LASERS DO JOGADOR 1 E ASTEROIDES
        for hit in pygame.sprite.groupcollide(asteroidField.asteroidSprites, player1.laserSprite, 0, 1):
                __explosion()
                explosoes.append(AnimatedSprite(explosion_images,hit.rect.centerx,hit.rect.centery))
                #aumentar tiros acertados
                player1.statistics[2]+=1
                #aumentar score
                player1.statistics[3]+=5
                hit.hitpoints += (player1.weapon_damage[player1.curweapon]*player1.damage_multiplier)
                ret = hit.kill_asteroid()
                if ret == 1:
                    hit.kill()
                    
        # DETECTAR COLISOES ENTRE LASERS DO JOGADOR 2 E ASTEROIDES
        for hit in pygame.sprite.groupcollide(asteroidField.asteroidSprites, player2.laserSprite, 0, 1):
                __explosion()
                explosoes.append(AnimatedSprite(explosion_images,hit.rect.centerx,hit.rect.centery))
                #aumentar tiros acertados
                player2.statistics[2]+=1
                #aumentar score
                player2.statistics[3]+=5
                hit.hitpoints += (player2.weapon_damage[player2.curweapon]*player2.damage_multiplier)
                ret = hit.kill_asteroid()
                if ret == 1:
                    hit.kill()
   
        for hit in pygame.sprite.groupcollide(player1.laserSprite, player2.laserSprite, 0, 1):
            __explosion()
            explosoes.append(AnimatedSprite(explosion_images,hit.rect.centerx,hit.rect.centery))
            player1.statistics[2]+=1
            hit.kill()
        
        return 0

def pickup_powerup(powerup,powerupSprite,player,playerSprite,tipo):
    
    for hit in pygame.sprite.groupcollide(powerupSprite, playerSprite, 1, 0):
        if tipo == 1:
                pickup_images_health = load_sliced_sprites(61,57,'health_pickup2.png')
                health_pickups.append(AnimatedSprite(pickup_images_health,powerup.rect.centerx-30,powerup.rect.centery-28))
                __pickup_shield()
                ##cura uma percentagem do max de hitpoints que e 50
                player.hitpoints += (player.maxhitpoints) * powerup.healfactor
                if player.hitpoints > player.maxhitpoints:
                        player.hitpoints = player.maxhitpoints
                return 1
        if tipo == 2:
                pickup_images_weapons = load_sliced_sprites(61,57,'weapon_pickup.png')
                weapon_pickups.append(AnimatedSprite(pickup_images_weapons,powerup.rect.centerx-30,powerup.rect.centery-28))
                player.ammo += powerup.ammo
                player.damage_multiplier = powerup.damagefactor
                if powerup.damagefactor == 4:
                        quad_damage = load_sound('toasty.wav')
                        quad_damage.set_volume(1)
                        quad_damage.play()
                        toasty = True
                      
                player.powerup_time = 1
                __pickup_weapon()
                return 1
        if tipo == 3:
            pickup_images_weapons = load_sliced_sprites(61,57,'health_pickup.png')
            weapon_pickups.append(AnimatedSprite(pickup_images_weapons,powerup.rect.centerx-30,powerup.rect.centery-28))
            player.mines_ammo += 5
            __pickup_weapon()
            return 1
        
                
        else:
            return 0   
        

def __explosion():
    fact = random.randrange(0,4)  
    explosion = load_sound("explosion"+str(fact+1)+".wav")
    #explosion.set_volume(0.2)
    explosion.play()  

def __pickup_shield():
    sound = load_sound('powerupshield.wav')
    sound.set_volume(0.6)
    sound.play()

def __pickup_weapon():
    sound = load_sound('powerupweapon.wav')
    sound.set_volume(0.6)
    sound.play()
  
