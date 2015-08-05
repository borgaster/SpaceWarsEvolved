import time

from animation import *
from asteroidField import *
from background import *
from loader import *
from physics import *
from player import *
from powerup import *
import pygame
from pygame.locals import *
from rotatingMenu_img import *
from spacemenu import *
from starField import *


# teclas dos jogadores default
keyPresset1 = [K_LEFT,K_RIGHT,K_UP,K_DOWN, K_SPACE, K_m]
keyPresset2 = [K_a, K_d, K_w, K_s, K_x, K_r]
pygame.init()
   

def game(numkills,nave1,nave2):
    

    SCREENSIZE = [800,600]


    #screen = pygame.display.set_mode(SCREENSIZE,pygame.FULLSCREEN)
    ## uncomment for debug
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.mouse.set_visible(0)
    clock = pygame.time.Clock()
    #init background
    background = Background(screen,'galaxy.jpg')
    #init efeito campo estrelado e asteroids
    starfield = StarField(screen)
    asteroidField = AsteroidField(screen)
    
    

    #init musica
    rand = random.randrange(0,2)
    if rand == 0:
        load_music('After Burner.mp3')
    else:
        load_music('Spybreak.mp3')
    #load_music('Gundam.mp3')
    
    #init players
    player1 = Player((200,SCREENSIZE[1]/2),keyPresset1,1,nave1,numkills)
    playerSprite1 = pygame.sprite.RenderPlain((player1))
    player1.spin(90,3)
    player2 = Player((SCREENSIZE[0]-200,SCREENSIZE[1]/2),keyPresset2,2,nave2,numkills)
    playerSprite2 = pygame.sprite.RenderPlain((player2))
    player2.spin(90,1)

    #powerup stuff variables
    powerups_on_screen = False
    done = False
    retval = 0
    powerup_available = 0

    #vars apenas para animacao do rapaz no canto do ecra
    i = random.randrange(1,4)
    pickup_timer = 0
    
    while not done:
        clock.tick(40)

        #se nao ha asteroides, respawn
        current_asteroids = len(asteroidField.asteroidSprites)
        if current_asteroids <= 0:
            current_asteroids = asteroidField.refresh(asteroidField.num_asteroids +1)

        if pickup_timer != 0:
            elapsed = round(time.clock())

        ##desenhar informacoes do jogadores
        font = pygame.font.SysFont("consola", 20)
        ScorePanel1 ="Player 1 - Lives: "+str(player1.statistics[0])+" "+"Score: "+str(player1.statistics[3])
        scorePlayer1 = font.render(ScorePanel1, True, (255,255,255))
        if nave2 != 0:
            ScorePanel2 ="Player 2 - Lives: "+str(player2.statistics[0])+" Score: "+str(player2.statistics[3])
            scorePlayer2 = font.render(ScorePanel2, True, (255,255,255))

        # desenhar informacoes de powerups disponiveis
        font = pygame.font.SysFont("consola", 40)
        PowerupPanel = ""
        if powerups_on_screen == False:
            poweruppanel = font.render(PowerupPanel, True, (0,255,0))

        #############################
        ##MOVER JOGADORES

        #se esta so um jogador
        if nave2 == 0:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    elif event.key == keyPresset1[0]:
                        player1.dx = -10
                        player1.spin(90,1)
                    elif event.key == keyPresset1[1]:
                        player1.dx = 10
                        player1.spin(90,3)
                    elif event.key == keyPresset1[2]:
                        player1.dy = -10
                        player1.spin(90,0)
                    elif event.key == keyPresset1[3]:
                        player1.dy = 10
                        player1.spin(90,2)
                        
                elif event.type == KEYUP:
                    if event.key == keyPresset1[0]:
                        player1.dx = -3
                    elif event.key == keyPresset1[1]:
                        player1.dx = 3
                    elif event.key == keyPresset1[2]:
                        player1.dy = -3
                    elif event.key == keyPresset1[3]:
                        player1.dy = 3
                    elif event.key == keyPresset1[5]:
                        player1.changeWeapon()
                        
        # ha dois jogadores a jogar, apanhar teclas todas
        else:    
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        done = True
                    elif event.key == keyPresset1[0]:
                        player1.dx = -10
                        player1.spin(90,1)
                    elif event.key == keyPresset1[1]:
                        player1.dx = 10
                        player1.spin(90,3)
                    elif event.key == keyPresset1[2]:
                        player1.dy = -10
                        player1.spin(90,0)
                    elif event.key == keyPresset1[3]:
                        player1.dy = 10
                        player1.spin(90,2)
                    elif event.key == keyPresset2[0]:
                        player2.dx = -10
                        player2.spin(90,1)
                    elif event.key == keyPresset2[1]:
                        player2.dx = 10
                        player2.spin(90,3)
                    elif event.key == keyPresset2[2]:
                        player2.dy = -10
                        player2.spin(90,0)
                    elif event.key == keyPresset2[3]:
                        player2.dy = 10
                        player2.spin(90,2)
                    
                elif event.type == KEYUP:
                    if event.key == keyPresset1[0]:
                        player1.dx = -3
                    elif event.key == keyPresset1[1]:
                        player1.dx = 3
                    elif event.key == keyPresset1[2]:
                        player1.dy = -3
                    elif event.key == keyPresset1[3]:
                        player1.dy = 3
                    elif event.key == keyPresset1[5]:
                        player1.changeWeapon()
                    elif event.key == keyPresset2[0]:
                        player2.dx = -3
                    elif event.key == keyPresset2[1]:
                        player2.dx = 3
                    elif event.key == keyPresset2[2]:
                        player2.dy = -3
                    elif event.key == keyPresset2[3]:
                        player2.dy = 3
                    elif event.key == keyPresset2[5]:
                        player2.changeWeapon()

        background.update()
        starfield.update()
 
        #calcular tempo de activacao de um powerup novo e o tipo
        #se estiver em single player so ha powerup de armas
        activate_powerups = random.randrange(0,200)
        if nave2 != 0:
            powerup_type = random.randrange(1,4)
        else:
            powerup_type = 2
        if activate_powerups == 150:
            if powerups_on_screen == False:
                powerup_available = powerup_type
                if (powerup_type == 1):
                    PowerupPanel = "Health Powerup Available!"
                    poweruppanel = font.render(PowerupPanel, True, (0,255,0))
                elif powerup_type == 2:
                    PowerupPanel = "Weapon Powerup Available!"
                    poweruppanel = font.render(PowerupPanel, True, (255,0,0))
                else:
                    PowerupPanel = "Mines Available!!"
                    poweruppanel = font.render(PowerupPanel, True, (255,0,0))

                powerup = Powerup(powerup_available,SCREENSIZE)
                powerupSprite = pygame.sprite.RenderPlain((powerup))
                powerups_on_screen = True
                ## POWERUP JA ESTA NO ECRA

        ########################
        #calculos de intersects       
        #Calcular colisoes de lasers entre jogadores
        kill = lasers(player1,player2,playerSprite1,playerSprite2,asteroidField)
        #se matou algum jogador, sai
        if kill == 1:
            done = True

        kill = asteroids(player1,player2,playerSprite1,playerSprite2,asteroidField)
        #se matou algum jogador, sai
        if kill == 1:
            done = True
            
        #apanhar powerups
        if powerups_on_screen == True:
            retval = pickup_powerup(powerup,powerupSprite,player1,playerSprite1,powerup_available)
            if retval == 1:
                retval = 0
                powerups_on_screen = False
                if powerup.tipo == 2 and powerup.damagefactor == 4:
                    pickup_timer = round(time.clock())
                    elapsed = pickup_timer
                    
            else:
                retval = pickup_powerup(powerup,powerupSprite,player2,playerSprite2,powerup_available)
                if retval == 1:
                    retval = 0
                    powerups_on_screen = False
                    if powerup.tipo == 2 and powerup.damagefactor == 4:
                        pickup_timer = round(time.clock())
                        elapsed = pickup_timer


        #############################
        # Desenhar
            
        #desenhar jogador 1
        screen.blit(scorePlayer1, (10, 740))
        playerSprite1.update(screen)
        playerSprite1.draw(screen)
        player1.draw_health(screen)
        player1.draw_stats(screen)
        
        #desenhar jogador 2
        if nave2 != 0:
            screen.blit(scorePlayer2, (10, 750))
            playerSprite2.update(screen)
            playerSprite2.draw(screen)
            player2.draw_health(screen)
            player2.draw_stats(screen)

        #powerups
        screen.blit(poweruppanel, (350, 10))
        if powerups_on_screen == True:
            powerupSprite.draw(screen)

        #desenhar powerup_pickups
        for sprite in weapon_pickups:
            sprite.render(screen,False)
        for sprite in health_pickups:
            sprite.render(screen,False)

        #desenhar asteroides
        asteroidField.update()

        #desenhar explosoes
        for sprite in explosoes:
            sprite.render(screen,False)

        #desenhar humor pic        
            
        if pickup_timer != 0:
            if (elapsed - pickup_timer) < 1.5:
                toasty_pic, toasty_rect = load_image("toasty"+str(i)+".PNG", -1)
                screen.blit(toasty_pic,(885,650))
            else:
                pickup_timer = 0
                #Alterei o random pois o grau de aleatoriedade eh baixo
                #desta forma aparecemos todos mais vezes :)
                listagem=[1,2,3,4]
                random.shuffle(listagem)
                random.shuffle(listagem)
                i = listagem[0]

        pygame.display.flip()

        ##FIM DO WHILE
        #####################################

    stop_music()
    pygame.display.set_mode([800,600])

    return player1,player2
    

def main():


    pygame.init()
    SCREENSIZE = [800,600]
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("Space War Evolved")
    pygame.mouse.set_visible(0)
    #init musica
    load_music('menu.mp3')
    clock = pygame.time.Clock()

    SP, rect = load_image("SP.png", -1)
    MP, rect2 = load_image("MP.png", -1)
    S, rect3 = load_image("S.png", -1)
    H, rect4 = load_image("H.png", -1)
    A, rect5 = load_image("A.png", -1)
    E, rect6 = load_image("E.png", -1)

    SP_red, rect = load_image("SP_red_35_433.png", -1)
    MP_red, rect = load_image("MP_red_93_433.png", -1)
    S_red, rect = load_image("S_red_151_478.png", -1)
    H_red, rect = load_image("H_red_93_478.png", -1)
    A_red, rect = load_image("A_red_151_433.png", -1)
    E_red, rect = load_image("E_red_35_478.png", -1)

    extra, rect = load_image("extra.png", -1)

    multi = []
    multi_images = load_sliced_sprites(221,34,'multi_player_anim_221x34.png')

    single = []
    single_images = load_sliced_sprites(243,34,'single_anim_243x34.png')

    help = []
    help_images = load_sliced_sprites(74,35,'help_anim_74x35.png')

    about = []
    about_images = load_sliced_sprites(112,29,'about_anim_112x29.png')

    exit = []
    exit_images = load_sliced_sprites(74,28,'exit_anim_74x28.png')

    setkeys = []
    setkeys_images = load_sliced_sprites(179,29,'setkeys_anim_179x29.png')

    jiproj = []
    jiproj_images = load_sliced_sprites(128,160,'ji_proj_128x160.png')
    jiproj.append(AnimatedSprite(jiproj_images,129,31))

    autores = []
    autores_images = load_sliced_sprites(111,160,'autores.png')
    autores.append(AnimatedSprite(autores_images,129,217))
    
    moverCursor = load_sound('moverCursor.wav')
    moverCursor.set_volume(0.2)

    clock = pygame.time.Clock()

    menu = RotatingMenu(x=520, y=295, radius=160, arc=pi, defaultAngle=pi/2.0)
    background = Background(screen,'Stargate_menu.png')

    menu.addItem(MenuItem(H))
    menu.addItem(MenuItem(S))
    menu.addItem(MenuItem(SP))
    menu.addItem(MenuItem(MP))
    menu.addItem(MenuItem(A))
    menu.addItem(MenuItem(E))
    menu.selectItem(2)

 #Loop
    while True:
        #Handle events
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moverCursor.play()
                    menu.selectItem(menu.selectedItemNumber + 1)
                if event.key == pygame.K_RIGHT:
                    moverCursor.play()
                    menu.selectItem(menu.selectedItemNumber - 1)
                if event.key == pygame.K_RETURN:
                    if menu.selectedItemNumber == 0:
                        option2()
                    elif menu.selectedItemNumber == 1:
                        option4()
                        
                    elif menu.selectedItemNumber == 2:
                        option0()
                        
                    elif menu.selectedItemNumber == 3:
                        option1()
                        
                    elif menu.selectedItemNumber == 4:
                        option3()
                        
                    elif menu.selectedItemNumber == 5:
                        option5()
                        
                        return False

        #Update stuff
        background.update()
        menu.update()

        for sprite in jiproj:
            sprite.render(screen,True)

        for sprite in autores:
            sprite.render(screen,True)

        screen.blit(extra, (124,24))
        
        if menu.selectedItemNumber == 0:
            single = []
            multi = []
            exit = []
            about = []
            setkeys = []
            screen.blit(H_red, (93,478))
            help.append(AnimatedSprite(help_images,490,280))
        elif menu.selectedItemNumber == 1:
            single = []
            help = []
            exit = []
            about = []
            multi = []
            screen.blit(S_red, (151,478))
            setkeys.append(AnimatedSprite(setkeys_images,435,280))
        elif menu.selectedItemNumber == 2:
            help = []
            multi = []
            exit = []
            about = []
            setkeys = []
            screen.blit(SP_red, (35,433))
            single.append(AnimatedSprite(single_images,403,280))
        elif menu.selectedItemNumber == 3:
            single = []
            help = []
            exit = []
            about = []
            setkeys = []
            screen.blit(MP_red, (93,433))
            multi.append(AnimatedSprite(multi_images,410,280))
        elif menu.selectedItemNumber == 4:
            single = []
            multi = []
            exit = []
            help = []
            setkeys = []
            screen.blit(A_red, (151,433))
            about.append(AnimatedSprite(about_images,470,280))
        elif menu.selectedItemNumber == 5:
            single = []
            multi = []
            help = []
            about = []
            setkeys = []
            screen.blit(E_red, (35,478))
            exit.append(AnimatedSprite(exit_images,490,280))

        for sprite in multi:
            sprite.render(screen,True)

        for sprite in single:
            sprite.render(screen,True)

        for sprite in about:
            sprite.render(screen,True)

        for sprite in exit:
            sprite.render(screen,True)

        for sprite in help:
            sprite.render(screen,True)

        for sprite in setkeys:
            sprite.render(screen,True)
        #Draw stuff
        #display.fill((0,0,0))
        menu.draw(screen)
        pygame.display.flip() #Show the updated scene
        clock.tick(fpsLimit) #Wait a little

if __name__ == "__main__":
   main()
