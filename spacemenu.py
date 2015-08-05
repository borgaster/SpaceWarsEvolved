from background import *
from main import *
from player import *
import pygame
from pygame.locals import *
from rotatingMenu_img import *


SCREENSIZE = [800, 600] #[1024,768]
screen = pygame.display.set_mode(SCREENSIZE)


class SpaceMenu:

    
#Define the initalize self options
    def __init__(self, *options):

        self.options = options
        self.x = 0
        self.y = 0
        self.font = pygame.font.Font(None, 32)
        self.option = 0
        self.width = 1
        self.color = [0, 0, 0]
        self.hcolor = [0, 0, 0]
        self.height = len(self.options)*self.font.get_height()
        self.menu_beep = load_sound("beep2.wav")
        for o in self.options:
            text = o[0]
            ren = self.font.render(text, 1, (0, 0, 0))
            if ren.get_width() > self.width:
                self.width = ren.get_width()

#Draw the menu
    def draw(self, surface):
        i=0
        for o in self.options:
            if i==self.option:
                clr = self.hcolor
            else:
                clr = self.color
            text = o[0]
            ren = self.font.render(text, 1, clr)
            if ren.get_width() > self.width:
                self.width = ren.get_width()
            surface.blit(ren, (self.x, self.y + i*self.font.get_height()))
            i+=1

#Menu Input
    def update(self, events):
        for e in events:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_DOWN:
                    self.option += 1
                    self.menu_beep.play()
                if e.key == pygame.K_UP:
                    self.option -= 1
                    self.menu_beep.play()
                if e.key == pygame.K_RETURN:
                    self.menu_beep.play()
                    self.options[self.option][1]()
        if self.option > len(self.options)-1:
            self.option = 0
        if self.option < 0:
            self.option = len(self.options)-1

#Position Menu
    def set_pos(self, x, y):
        self.x = x
        self.y = y

#Font Style
    def set_font(self, font):
        self.font = font

#Highlight Color
    def set_highlight_color(self, color):
        self.hcolor = color

#Font Color
    def set_normal_color(self, color):
        self.color = color

#Font position
    def center_at(self, x, y):
        self.x = x-(self.width/2)
        self.y = y-(self.height/2)

#Save score in JSON format
def SaveScoreJSON(playerData):
    with open(FILENAME, 'w') as outFile:
        json.dump(playerData, outFile)
        
#Get scores
#TODO: Still need to decide PlayerData format
def GetScores():
    with open(FILENAME) as dataFile:
        playerData = json.load(dataFile)
    return playerData

#para o modo Versus
def ScoreMenu(Player1,Player2):
    load_music('statistics.mp3')
    background = Background(screen,'1vs1Mode.png')
    
    if (Player1[3])>(Player2[3]):
            winner=SpaceMenu(
                [""],
                ["Player 1 'teebaged' Player 2"])
            statusPlayer1=SpaceMenu(
                [""],
                ["WINNER"])
            statusPlayer2=SpaceMenu(
                [""],
                ["LOSER"])
    elif(Player1[3])<(Player2[3]):
            winner=SpaceMenu(
                [""],
                ["Player 2 'teebaged' Player 1"])
            statusPlayer1=SpaceMenu(
                [""],
                ["LOSER"])
            statusPlayer2=SpaceMenu(
                [""],
                ["WINNER"])
    else:
            winner=SpaceMenu(
                [""],
                ["It's a Draw!"])
            statusPlayer1=SpaceMenu(
                [""],
                [""])
            statusPlayer2=SpaceMenu(
                [""],
                [""])
        

    if Player1[1]!=0 and Player1[2]!=0:
        acuracyPlayer1=Player1[2]*100/Player1[1]
    else:
        acuracyPlayer1=0
    
    if Player2[1]!=0 and Player2[2]!=0:
        acuracyPlayer2=Player2[2]*100/Player2[1]
    else:
        acuracyPlayer2=0

    #Statistics Player 1
    Player1Score = SpaceMenu(
        [""],
        ["Score -> "+str(Player1[3])+" points"])

    Player1ShotsFired = SpaceMenu(
        [""],
        ["Total shots fired -> " +str(Player1[1])+""])
   
    Player1ShotsMissed = SpaceMenu(
        [""],
        ["Shots missed -> "+str(Player1[1]-Player1[2])+""])

    Player1Accurary= SpaceMenu(
        [""],
        ["Accurary -> "+str(acuracyPlayer1)+"%"])

    #Statistics Player 2
    Player2Score = SpaceMenu(
        [""],
        ["Score -> "+str(Player2[3])+" points"])

    Player2ShotsFired = SpaceMenu(
        [""],
        ["Total shots fired -> " +str(Player2[1])+""])
   
    Player2ShotsMissed = SpaceMenu(
        [""],
        ["Shots missed -> "+str(Player2[1]-Player2[2])+""])

    Player2Accurary= SpaceMenu(
        [""],
        ["Accurary -> "+str(acuracyPlayer2)+"%"])


    #Draw settings for Player 1 stuff
    Player1Score.center_at(370, 163)
    Player1Score.set_font(pygame.font.Font(None, 16))
    Player1Score.set_normal_color((255, 255, 255))

    Player1ShotsFired.center_at(380, 183)
    Player1ShotsFired.set_font(pygame.font.Font(None, 16))
    Player1ShotsFired.set_normal_color((255, 255, 255))

    Player1ShotsMissed.center_at(368, 200)
    Player1ShotsMissed.set_font(pygame.font.Font(None, 16))
    Player1ShotsMissed.set_normal_color((255, 255, 255))

    Player1Accurary.center_at(363, 220)
    Player1Accurary.set_font(pygame.font.Font(None, 16))
    Player1Accurary.set_normal_color((255, 255, 255))

    #Draw settings for Player 2 stuff
    Player2Score.center_at(640, 163)
    Player2Score.set_font(pygame.font.Font(None, 16))
    Player2Score.set_normal_color((255, 255, 255))

    Player2ShotsFired.center_at(650, 180)
    Player2ShotsFired.set_font(pygame.font.Font(None, 16))
    Player2ShotsFired.set_normal_color((255, 255, 255))

    Player2ShotsMissed.center_at(635, 200)
    Player2ShotsMissed.set_font(pygame.font.Font(None, 16))
    Player2ShotsMissed.set_normal_color((255, 255, 255))

    Player2Accurary.center_at(625, 215)
    Player2Accurary.set_font(pygame.font.Font(None, 16))
    Player2Accurary.set_normal_color((255, 255, 255))

    #Draw Settings Winner
    winner.center_at(500, 390)
    winner.set_font(pygame.font.Font(None, 42))
    winner.set_normal_color((255, 255, 255))

    #Draw status settings
    statusPlayer1.center_at(365, 240)
    statusPlayer1.set_font(pygame.font.Font(None, 25))
    statusPlayer1.set_normal_color((255, 255, 255))

    statusPlayer2.center_at(650, 240)
    statusPlayer2.set_font(pygame.font.Font(None, 25))
    statusPlayer2.set_normal_color((255, 255, 255))

    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
           #Draw

           background.update()
           statusPlayer1.draw(screen)
           statusPlayer2.draw(screen)
           Player1Score.draw(screen)
           Player1ShotsFired.draw(screen)
           Player1ShotsMissed.draw(screen)
           Player1Accurary.draw(screen)
           Player2Score.draw(screen)
           Player2ShotsFired.draw(screen)
           Player2ShotsMissed.draw(screen)
           Player2Accurary.draw(screen)
           winner.draw(screen)
           pygame.display.flip()

    stop_music()
    #load_music('menu.mp3')

def updateHighScore(scoreEntry):
    filename='singlePlayer.scores'
    if os.path.isFile(filename):
        highscoreFile = open(filename, 'w')
        highscoreFile.write(scoreEntry)
        highscoreFile.write("\n")
        highscoreFile.close()

def ScoreMenu2(Player1):
    listagem=[]
    background = Background(screen,'gameScore.png')

    if Player1[1]!=0 and Player1[2]!=0:
        acuracyPlayer1=Player1[2]*100/Player1[1]
    else:
        acuracyPlayer1=0

    #Statistics for Option Menu
    statistics = SpaceMenu(
        [""],
        ["Score <> "+str(Player1[3])+" points"],
        ["Total lives left <> "+str(Player1[0])+""],
        ["Total shots fired <> "+str(Player1[1])+""],
        [" -> missed: "+str(Player1[1]-Player1[2])+""],
        ["Accuracy <> "+str(acuracyPlayer1)+"%"])        

    #Ler os highscores existentes
    #Passagem dos valores do ficheiro para uma lista
    filename='singlePlayer.scores'
    msgStatus=0
    if os.path.isfile('singlePlayer.scores'):
        highScoreFile = open("singlePlayer.scores", 'r')
        #Passar os valores para uma lista
        checkEmpty=0
        rank=0
        for line in highScoreFile.readlines():
            var = line.split()
            listagem.append([int(var[0]),str(var[1])])
            checkEmpty=checkEmpty+1
        print len(listagem)
        #Se ha 0 resultados entao temos highscore
        print 
        if len(listagem) == 0:
            msgStatus=1
        
        #Caso contrario, vamos entao verificar entre os top scores se temos lugar    
        else:

            print 
            listagem.sort() # ordenacao dos top scores do ficheiro onde a ultima posicao representa o rank 1
            highScore=listagem[2]

            #Escrita do top 3 inicial, colocar aqui devido ao append mais abaixo
#             top3Escrita=SpaceMenu(
#                 [""],
#                 ["***** TOP PLAYERS *****"],
#                 ["First place, "+str(listagem[2])],
#                 ["Second place, "+str(listagem[1])],
#                 ["Third place, "+str(listagem[0])])
            top3Escrita=SpaceMenu(createHighScoreMenu(listagem))

            #top3Escrita Settings
            top3Escrita.center_at(560,260)
            top3Escrita.set_font(pygame.font.Font(None, 20))
            top3Escrita.set_normal_color((255, 255, 255))
            
            jogadorDados=[]
            jogadorDados.append([int(Player1[3]),'Your_Entry'])
            
            if jogadorDados[0] >= listagem[2]:
                stop_music()
                lugar=2
                #bestSong = load_music('youarethebest.mp3')
                #pygame.mixer.music.play(1)
                listagem.append(jogadorDados[0])
                listagem.sort()
                valorAremover=listagem[0]
                listagem.remove(valorAremover)
                msgStatus=1
                rank=1
            elif jogadorDados[0] >= listagem[1]:
                stop_music()
                lugar=1
                #bestSong = load_music('youarethebest.mp3')
                #pygame.mixer.music.play(1)
                listagem.append(jogadorDados[0])
                listagem.sort()
                valorAremover=listagem[0]
                listagem.remove(valorAremover)
                msgStatus=1
                rank=2
            elif jogadorDados[0] >= listagem[0]:
                stop_music()
                lugar=0
                ##bestSong = load_music('youarethebest.mp3')
                #pygame.mixer.music.play(1)
                listagem.append(jogadorDados[0])
                listagem.sort()
                valorAremover=listagem[0]
                listagem.remove(valorAremover)
                msgStatus=1
                rank=3
        highScoreFile.close()

    #Se nao fizemos highscore temos a seguinte msg
    if msgStatus == 0:
        #load_music("shit.mp3")
       # pygame.mixer.music.play(1)
        congratsMessage= SpaceMenu(
            [""],
            ["Noob Player, no high score for you! Go eat Chocapic!"],
            ["The game will auto return in 5 seconds."],
            ["But thanks for playing ^_^"])

    #Ao conseguirmos um highscore vamos processar entao a seguinte msg
    else:

        #temos de actualizar
#         top3Escrita=SpaceMenu(
#             [""],
#             ["***** TOP PLAYERS *****"],
#             ["First place, "+str(listagem[2])],
#             ["Second place, "+str(listagem[1])],
#             ["Third place, "+str(listagem[0])])
        top3Escrita=SpaceMenu(createHighScoreMenu(listagem))
        lugar=2
        congratsMessage=SpaceMenu(
            [""],
            ["CONGRATS, You got a new high score, RANK "+str(rank)+" !!! "],
#            ["Last Rank 1 was <> "+str(listagem[2])+""],
            [""],
            ["The game will auto return in 3 seconds,"],
            ["-> after you inserted your name/nickaname!"])

        askNameMsg=SpaceMenu(
            [""],
            ["--------------------------------------------"],
            ["Please write your name or nickname"],
            ["-> Max characters is 5"],
            ["-> press enter to finish"],
            ["--------------------------------------------"])
        #askNameMessage Settings
        askNameMsg.center_at(560,230)
        askNameMsg.set_font(pygame.font.Font(None, 20))
        askNameMsg.set_normal_color((255, 255, 255))

        #askNameMessage Settings, adaptar ao conteudo em caso de highscore
        top3Escrita.center_at(590,330)
        top3Escrita.set_font(pygame.font.Font(None, 20))
        top3Escrita.set_normal_color((255, 255, 255))
        

    #Statistics Settings
    statistics.center_at(160,490)
    statistics.set_font(pygame.font.Font(None, 20))
    statistics.set_normal_color((255, 255, 255))

    #CongratsMessage Settings
    congratsMessage.center_at(580,150)
    congratsMessage.set_font(pygame.font.Font(None, 20))
    congratsMessage.set_normal_color((255, 255, 255))

    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True
    nomeDoJogador=""
    contador=0

    #Vamos agora pedir o nome ao jogador, ate 5 letras e em seguida fazer o registo no ficheiro
    if msgStatus==1:
        fazSleep=1
        highScoreFile = open("singlePlayer.scores", 'w')
        #ate 5 pois o numero max de caracteres para o nome = 5
        while contador<5:
            clock.tick(30)
            #input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                    contador=0
                elif event.type == pygame.KEYDOWN:
                    letra = pygame.key.name(event.key)
                    if event.key != K_RETURN:
                        if event.key != K_BACKSPACE and event.key != K_ESCAPE and event.key != K_SPACE:
                            nomeDoJogador=nomeDoJogador+letra
                            contador=contador+1
                        elif event.key == K_BACKSPACE:
                            nomeDoJogador=""
                            contador = (contador - 1)%5
                    else:
                        load_sound("beep2.wav").play()
                        contador=5
                    
                    #Quando chegarmos a 5 sabemos entao que podemos escrever para o ficheiro, vamos la
                    if contador==5:
                        if lugar == 2:
                            listagem[2]=([int(Player1[3]),nomeDoJogador])
                        elif lugar == 1:
                            listagem[1]=([int(Player1[3]),nomeDoJogador])
                        else:
                            listagem[0]=([int(Player1[3]),nomeDoJogador])
                
                        #Processar nome do jogador e pontos para formato ficheiro
                        #Formatacao dos dados
                        firstPlace=""
                        for c in str(listagem[2]):
                            if not (c=="[" or c=="]" or c=="'" or c==","):
                                firstPlace=firstPlace+c

                        secondPlace=""
                        for h in str(listagem[1]):
                            if not (h=="[" or h=="]" or h=="'" or h==","):
                                secondPlace=secondPlace+h

                        thirdPlace=""
                        for a in str(listagem[0]):
                            if not (a=="[" or a=="]" or a=="'" or a==","):
                                thirdPlace=thirdPlace+a

                        #Escrevendo no ficheiro
                        highScoreFile.write(firstPlace)
                        highScoreFile.write("\n")
                        highScoreFile.write(secondPlace)
                        highScoreFile.write("\n")
                        highScoreFile.write(thirdPlace)
                        highScoreFile.write("\n")

            nameAtscreen=SpaceMenu(
                [""],
                ["-> Your name or nickname is: "+nomeDoJogador+""])

            #nameAtscreen Settings
            nameAtscreen.center_at(525,260)
            nameAtscreen.set_font(pygame.font.Font(None, 20))
            nameAtscreen.set_normal_color((255, 255, 255))
            
            #Render do ecra, dentro do ciclo while 
            background.update()
            statistics.draw(screen)
            congratsMessage.draw(screen)
            askNameMsg.draw(screen)
            nameAtscreen.draw(screen)
            top3Escrita.draw(screen)
            pygame.display.flip()
    #Bem, ao nao conseguirmos highscore apenas fazemos o render 
    else:
            background.update()
            statistics.draw(screen)
            congratsMessage.draw(screen)
            top3Escrita.draw(screen)
            pygame.display.flip()
            time.sleep(5)
            fazSleep=1

    stop_music()
    #load_music('menu.mp3')
#    if fazSleep==1:
#        time.sleep(3)
    time.sleep(3)

def createHighScoreMenu(scoreList):
    header = ["","***** TOP PLAYERS *****"]
    places = ["First place", "Second place", "Third place"]
    for score in scoreList:
        header.append(places[str(index(score))], score)
    return header
    
def roundsMenu(NAVE1,NAVE2):
    NAVE1 = NAVE1
    NAVE2 = NAVE2
    background = Background(screen,'menu.jpg')

    Nave1 , rect = load_image('Nave1.png',-1)
    Nave2 , rect = load_image('Nave2.png',-1)
    Nave3 , rect = load_image('Nave3.png',-1)
    Nave4 , rect = load_image('Nave4.png',-1)
    Nave5 , rect = load_image('Nave5.png',-1)

    #Title for Option Menu
    menuTitle = SpaceMenu(
        ["Choose mode:"])

    #Option Menu Text
    menuRounds = SpaceMenu(
        ["5 kill match",suboption1],
        ["10 kill match",suboption2],
        ["20 kill match",suboption3])

    menuReturn = SpaceMenu(
        ["Press Esc to return"])
    #Title

    menuReturn.center_at(418, 392)
    menuReturn.set_font(pygame.font.Font(None, 24))
    menuReturn.set_highlight_color((0, 255, 0))

    menuTitle.center_at(378, 195)
    menuTitle.set_font(pygame.font.Font(None, 38))
    menuTitle.set_highlight_color((0, 255, 0))

    #Menu settings
    menuRounds.center_at(390, 295)
    menuRounds.set_font(pygame.font.Font(None, 32))
    menuRounds.set_highlight_color((0, 255, 0))
    menuRounds.set_normal_color((0, 85, 0))
    menuuRounds , rect = load_image('next_round2.png',-1)
    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Update Menu
        menuRounds.update(events)

        #Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    keepGoing = False

        #Draw
        #screen.blit(background, (0,0))
        #arena.update()
        #arena.draw(screen)
        background.update()
        screen.blit(menuuRounds, (0,0))
        menuRounds.draw(screen)
        menuTitle.draw(screen)
        menuReturn.draw(screen)
        if NAVE1 == 1:
            screen.blit(Nave1, (55,65))
        elif NAVE1 == 2:
            screen.blit(Nave2, (57,65))
        elif NAVE1 == 3:
            screen.blit(Nave3, (50,74))
        elif NAVE1 == 4:
            screen.blit(Nave4, (50,70))
        else :
            screen.blit(Nave5, (52,70))
        if NAVE2 == 1:
            screen.blit(Nave1, (55,495))
        elif NAVE2 == 2:
            screen.blit(Nave2, (57,495))
        elif NAVE2 == 3:
            screen.blit(Nave3, (50,504))
        elif NAVE2 == 4:
            screen.blit(Nave4, (50,500))
        else :
            screen.blit(Nave5, (52,500))
        pygame.display.flip()


def roundsMenu2(NAVE1):

    NAVE1 = NAVE1
    background = Background(screen,'menu.jpg')

    Nave1 , rect = load_image('Nave1.png',-1)
    Nave2 , rect = load_image('Nave2.png',-1)
    Nave3 , rect = load_image('Nave3.png',-1)
    Nave4 , rect = load_image('Nave4.png',-1)
    Nave5 , rect = load_image('Nave5.png',-1)

    #Title for Option Menu
    menuTitle = SpaceMenu(
        ["Choose mode:"])

    #Option Menu Text
    menuRounds = SpaceMenu(
        ["Easy",easymode],
        ["Medium",mediummode],
        ["Hardcore",hardcoremode])


    menuReturn = SpaceMenu(
        ["Press Esc to return"])

    #Title

    menuReturn.center_at(418, 392)
    menuReturn.set_font(pygame.font.Font(None, 24))
    menuReturn.set_highlight_color((0, 255, 0))

    menuTitle.center_at(378, 195)
    menuTitle.set_font(pygame.font.Font(None, 38))
    menuTitle.set_highlight_color((0, 255, 0))

    #Menu settings
    menuRounds.center_at(395, 295)
    menuRounds.set_font(pygame.font.Font(None, 32))
    menuRounds.set_highlight_color((0, 255, 0))
    menuRounds.set_normal_color((0, 85, 0))

    menuuRounds , rect = load_image('next_round.png',-1)
    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Update Menu
        menuRounds.update(events)

        #Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    keepGoing = False


        #Draw
        #screen.blit(background, (0,0))
        #arena.update()
        #arena.draw(screen)

        background.update()
        screen.blit(menuuRounds, (0,0))
        menuRounds.draw(screen)
        menuTitle.draw(screen)
        menuReturn.draw(screen)
        if NAVE1 == 1:
            screen.blit(Nave1, (55,65))
        elif NAVE1 == 2:
            screen.blit(Nave2, (57,65))
        elif NAVE1 == 3:
            screen.blit(Nave3, (50,74))
        elif NAVE1 == 4:
            screen.blit(Nave4, (50,70))
        else :
            screen.blit(Nave5, (52,70))
        pygame.display.flip()


def chosePlayer():

    choseNave1 , rect = load_image('choseNave1.png',-1)
    choseNave2 , rect = load_image('choseNave2.png',-1)
    choseNave3 , rect = load_image('choseNave3.png',-1)
    choseNave4 , rect = load_image('choseNave4.png',-1)
    choseNave5 , rect = load_image('choseNave5.png',-1)

    desc01 , rect = load_image('desc01.png',-1)
    desc02 , rect = load_image('desc02.png',-1)
    desc03 , rect = load_image('desc03.png',-1)
    desc04 , rect = load_image('desc04.png',-1)
    desc05 , rect = load_image('desc05.png',-1)

    menu = RotatingMenu(x=100, y=160, radius=55, arc=pi*1.6, defaultAngle=pi/2.0, wrap=True)
    menu2 = RotatingMenu(x=100, y=460, radius=55, arc=pi*1.6, defaultAngle=pi/2.0, wrap=True)

    menu.addItem(MenuItem(choseNave1))
    menu.addItem(MenuItem(choseNave3))
    menu.addItem(MenuItem(choseNave2))
    menu.addItem(MenuItem(choseNave4))
    menu.addItem(MenuItem(choseNave5))
    menu.selectItem(1)

    menu2.addItem(MenuItem(choseNave1))
    menu2.addItem(MenuItem(choseNave3))
    menu2.addItem(MenuItem(choseNave2))
    menu2.addItem(MenuItem(choseNave4))
    menu2.addItem(MenuItem(choseNave5))
    menu2.selectItem(1)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    #Title for Option Menu
    text1 = SpaceMenu(
        ["Player 1"])
    goplay = SpaceMenu(
        ["Press Enter to choose rounds"])
    #Option Menu Text
    text2 = SpaceMenu(
        ["Player 2"])

    menu1 , rect = load_image('picknaves.png',-1)
    #Title
    text1.center_at(50, 46)
    text1.set_font(pygame.font.Font(None, 38))
    text1.set_highlight_color((255, 255, 255))

    text2.center_at(50, 346)
    text2.set_font(pygame.font.Font(None, 38))
    text2.set_highlight_color((255, 255, 255))

    goplay.center_at(430, 310)
    goplay.set_font(pygame.font.Font(None, 28))
    goplay.set_highlight_color((0, 255, 0))
    goplay.set_normal_color((0, 85, 0))

    mira = []
    mira_images = load_sliced_sprites(64,61,'mira_64x61.png')
    mira.append(AnimatedSprite(mira_images,68,183))

    mira2 = []
    mira2.append(AnimatedSprite(mira_images,68,483))

    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True
    moverCursor = load_sound('moverCursor.wav')

    while keepGoing:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    keepGoing = False
                elif e.key == keyPresset1[0]:
                    moverCursor.play()
                    menu.selectItem(menu.selectedItemNumber + 1)
                elif e.key == keyPresset1[1]:
                    moverCursor.play()
                    menu.selectItem(menu.selectedItemNumber - 1)
                elif e.key == keyPresset2[0]:
                    moverCursor.play()
                    menu2.selectItem(menu2.selectedItemNumber + 1)
                elif e.key == keyPresset2[1]:
                    moverCursor.play()
                    menu2.selectItem(menu2.selectedItemNumber - 1)
                if e.key == pygame.K_RETURN:
                        keepGoing = False

        #Draw
        #screen.blit(background, (0,0))
        #arena.update()
        #arena.draw(screen)
        screen.blit(background, (0, 0))
        screen.blit(menu1, (0,0))
        screen.blit(menu1, (0,300))
        menu.update()
        menu2.update()

        
        menu.draw(screen)
        menu2.draw(screen)
        text1.draw(screen)
        text2.draw(screen)
        goplay.draw(screen)

        if menu.selectedItemNumber == 0:
            screen.blit(desc01, (210,90))
        elif menu.selectedItemNumber == 1:
            screen.blit(desc02, (210,90))
        elif menu.selectedItemNumber == 2:
            screen.blit(desc03, (210,90))
        elif menu.selectedItemNumber == 3:
            screen.blit(desc04, (210,90))
        else:
            screen.blit(desc05, (210,90))

        if menu2.selectedItemNumber == 0:
            screen.blit(desc01, (210,390))
        elif menu2.selectedItemNumber == 1:
            screen.blit(desc02, (210,390))
        elif menu2.selectedItemNumber == 2:
            screen.blit(desc03, (210,390))
        elif menu2.selectedItemNumber == 3:
            screen.blit(desc04, (210,390))
        else:
            screen.blit(desc05, (210,390))

        for sprite in mira:
            sprite.render(screen,True)
        for sprite in mira2:
            sprite.render(screen,True)
        pygame.display.flip()

    return menu.selectedItemNumber+1,menu2.selectedItemNumber+1

def chosePlayer2():
    choseNave1 , rect = load_image('choseNave1.png',-1)
    choseNave2 , rect = load_image('choseNave2.png',-1)
    choseNave3 , rect = load_image('choseNave3.png',-1)
    choseNave4 , rect = load_image('choseNave4.png',-1)
    choseNave5 , rect = load_image('choseNave5.png',-1)

    desc01 , rect = load_image('desc01.png',-1)
    desc02 , rect = load_image('desc02.png',-1)
    desc03 , rect = load_image('desc03.png',-1)
    desc04 , rect = load_image('desc04.png',-1)
    desc05 , rect = load_image('desc05.png',-1)

    menu = RotatingMenu(x=100, y=160, radius=55, arc=pi*1.6, defaultAngle=pi/2.0, wrap=True)

    menu.addItem(MenuItem(choseNave1))
    menu.addItem(MenuItem(choseNave3))
    menu.addItem(MenuItem(choseNave2))
    menu.addItem(MenuItem(choseNave4))
    menu.addItem(MenuItem(choseNave5))
    menu.selectItem(1)


    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    #Title for Option Menu
    text1 = SpaceMenu(
        ["Player 1"])
    goplay = SpaceMenu(
        ["Press Enter to choose rounds"])
    #Option Menu Text

    menu1 , rect = load_image('picknaves.png',-1)
    #Title
    text1.center_at(50, 46)
    text1.set_font(pygame.font.Font(None, 38))
    text1.set_highlight_color((255, 255, 255))

    goplay.center_at(430, 310)
    goplay.set_font(pygame.font.Font(None, 28))
    goplay.set_highlight_color((0, 255, 0))
    goplay.set_normal_color((0, 85, 0))

    mira = []
    mira_images = load_sliced_sprites(64,61,'mira_64x61.png')
    mira.append(AnimatedSprite(mira_images,68,183))

    moverCursor = load_sound('moverCursor.wav')
    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)

        #Events
        events = pygame.event.get()

        #Quit Event
        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                return
            elif e.type == pygame.KEYDOWN:
                moverCursor.play()
                if e.key == pygame.K_ESCAPE:
                    keepGoing = False
                elif e.key == keyPresset1[0]:
                    menu.selectItem(menu.selectedItemNumber + 1)
                elif e.key == keyPresset1[1]:
                    menu.selectItem(menu.selectedItemNumber - 1)
                if e.key == pygame.K_RETURN:
                    if menu.selectedItemNumber == 0:
                        keepGoing = False
                    elif menu.selectedItemNumber == 1:
                        keepGoing = False
                    elif menu.selectedItemNumber == 2:
                        keepGoing = False
                    elif menu.selectedItemNumber == 3:
                        keepGoing = False
                    elif menu.selectedItemNumber == 4:
                        keepGoing = False

        #Draw
        #screen.blit(background, (0,0))
        #arena.update()
        #arena.draw(screen)
        screen.blit(background, (0, 0))
        screen.blit(menu1, (0,0))
        menu.update()
    
 
        menu.draw(screen)
        text1.draw(screen)
        goplay.draw(screen)
        if menu.selectedItemNumber == 0:
            screen.blit(desc01, (210,90))
        elif menu.selectedItemNumber == 1:
            screen.blit(desc02, (210,90))
        elif menu.selectedItemNumber == 2:
            screen.blit(desc03, (210,90))
        elif menu.selectedItemNumber == 3:
            screen.blit(desc04, (210,90))
        else:
            screen.blit(desc05, (210,90))

        for sprite in mira:
            sprite.render(screen,True)
        pygame.display.flip()


    return menu.selectedItemNumber+1

def changeKeys():
    background = Background(screen,'instructions.jpg')

    setkeys , rect = load_image('set_keys.png',-1)
    #Title for Option Menu
    menuTitle = SpaceMenu(
        ["Set Keys"])

    #Option Menu Text
    setKeys = [SpaceMenu(
        [""],
        ["Player 1:"],
        [""]),SpaceMenu(
        [""],
        ["Player 2:"],
        [""])]



    showKeyLeft = SpaceMenu(
        ["Insert left key"])
    showKeyRight = SpaceMenu(
        ["Insert right key"])
    showKeyUp = SpaceMenu(
        ["Insert up key"])
    showKeyDown = SpaceMenu(
        ["Insert down key"])
    showKeyFire = SpaceMenu(
        ["Insert fire key"])
    showKeyWeapon = SpaceMenu(
        ["Insert change weapon key"])
    showKeyEnter = SpaceMenu(
        ["Press Enter to continue"])
    #Title
    menuTitle.center_at(205, 120)
    menuTitle.set_font(pygame.font.Font(None, 42))
    menuTitle.set_highlight_color((255, 255, 255))

    showKeyLeft.center_at(195, 300)
    showKeyLeft.set_font(pygame.font.Font(None, 42))
    showKeyLeft.set_highlight_color((255, 255, 255))

    showKeyRight.center_at(195, 300)
    showKeyRight.set_font(pygame.font.Font(None, 42))
    showKeyRight.set_highlight_color((255, 255, 255))

    showKeyUp.center_at(195, 300)
    showKeyUp.set_font(pygame.font.Font(None, 42))
    showKeyUp.set_highlight_color((255, 255, 255))

    showKeyDown.center_at(195, 300)
    showKeyDown.set_font(pygame.font.Font(None, 42))
    showKeyDown.set_highlight_color((255, 255, 255))

    showKeyFire.center_at(195, 300)
    showKeyFire.set_font(pygame.font.Font(None, 42))
    showKeyFire.set_highlight_color((255, 255, 255))

    showKeyWeapon.center_at(186, 300)
    showKeyWeapon.set_font(pygame.font.Font(None, 42))
    showKeyWeapon.set_highlight_color((255, 255, 255))

    showKeyEnter.center_at(190, 300)
    showKeyEnter.set_font(pygame.font.Font(None, 42))
    showKeyEnter.set_highlight_color((255, 255, 255))
    #Title Center
    setKeys[0].center_at(200, 220)
    setKeys[1].center_at(200, 220)
    #Menu Font
    setKeys[0].set_font(pygame.font.Font(None, 42))
    setKeys[1].set_font(pygame.font.Font(None, 42))

    #Highlight Color
    setKeys[0].set_normal_color((255, 255, 255))
    setKeys[1].set_normal_color((255, 255, 255))


    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True
    counter = 0
    playerNumber = 0
    keyDefined = 0
    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        keepGoing = False
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
                    if event.key == pygame.K_RETURN:
                        counter = 0
                        keyDefined = 0
                        playerNumber = (playerNumber+1)
                        if playerNumber > 1:
                            playerNumber = 1
                            keepGoing = False
                    else:
                        if playerNumber == 0:
                            if keyDefined <= 5:
                                keyPresset1[counter]= event.key
                                counter = (counter +1)%6
                                keyDefined +=1

                        else:
                            if keyDefined <= 5:
                                keyPresset2[counter]= event.key
                                counter = (counter +1)%6
                                keyDefined +=1

           #Draw

           background.update()
           screen.blit(setkeys, (0,0))
           if keyDefined == 0:
               showKeyLeft.draw(screen)
           elif keyDefined == 1:
               showKeyRight.draw(screen)
           elif keyDefined == 2:
               showKeyUp.draw(screen)
           elif keyDefined == 3:
               showKeyDown.draw(screen)
           elif keyDefined == 4:
               showKeyFire.draw(screen)
           elif keyDefined == 5:
               showKeyWeapon.draw(screen)
           if keyDefined == 6:
               showKeyEnter.draw(screen)
           menuTitle.draw(screen)
           setKeys[playerNumber].draw(screen)
           pygame.display.flip()
           
           
def instructionsMenu():

    background = Background(screen,'helpmenu.jpg')

    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
           #Draw
		   
           background.update()
           pygame.display.flip()




def aboutMenu():


    background = Background(screen,'about.jpg')
    aboutus , rect = load_image('aboutus.png',-1)

    #Set Clock
    clock = pygame.time.Clock()
    keepGoing = True

    while keepGoing:
           clock.tick(30)
           #input
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        keepGoing = False
           #Draw
           background.update()
           screen.blit(aboutus, (230,100))
           pygame.display.flip()

#Functions
def option0():
    global NAVE1
    NAVE1 = chosePlayer2()
    roundsMenu2(NAVE1)
def option1():
    global NAVE1
    global NAVE2
    #global NAVE3
    #global NAVE4
    NAVE1,NAVE2 = chosePlayer()
    roundsMenu(NAVE1,NAVE2)
def option2():
    instructionsMenu()
def option3():
    aboutMenu()
def option4():
    changeKeys()
def option5():
    pygame.quit()
def suboption1():
    player1,player2 = game(5,NAVE1,NAVE2)
    if player2.shiptype != 0:
        ScoreMenu(player1.statistics,player2.statistics)
    else:
        ScoreMenu2(player1.statistics)
def suboption2():
    player1,player2 = game(10,NAVE1,NAVE2)
    ScoreMenu(player1.statistics,player2.statistics)
    
def suboption3():
    player1,player2 = game(20,NAVE1,NAVE2)
    ScoreMenu(player1.statistics,player2.statistics)
   
def easymode():
    player1,player2 = game(10,NAVE1,0)
    ScoreMenu2(player1.statistics)
def mediummode():
    player1,player2 = game(5,NAVE1,0)
    ScoreMenu2(player1.statistics)
def hardcoremode():
    player1,player2 = game(3,NAVE1,0)
    ScoreMenu2(player1.statistics)
