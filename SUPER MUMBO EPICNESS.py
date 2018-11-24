import pygame, sys, random, time, eztext
from howtoplay import *
from playersinput import *
from Tips import *
from pygame.locals import *
from Players import *

#initialize pygame
pygame.init()

#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32) #the tuple has pixels
pygame.display.set_caption('Super Mumbo Epicness') #the title of window

# set up fonts
basicFont = pygame.font.SysFont(None, 48) #none is for default system font, number is size of font

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148,0,221)
ORANGE = (255,140,0)

#player colours
P1Colour=(251,198,201)
P2Colour=(172,181,216)
P3Colour=(255,253,196)
P4Colour=(213,234,211)
PxColours=[P1Colour,P2Colour,P3Colour,P4Colour]

#Loading pictures
home=pygame.image.load('Images/homescreen.jpeg')
about=pygame.image.load('Images/about.png')
playerscreen=pygame.image.load('Images/chooseplayerbg.jpg')
button=pygame.image.load('Images/home.png')
playername=pygame.image.load('Images/playerinputbg.jpg')

#list of players
Player1=0
Player2=0
Player3=0
Player4=0
Players=[Player1, Player2, Player3, Player4]

#set up mixer
pygame.mixer.init()
pygame.mixer.music.load('Sound Track/Menu Music.mp3')
pygame.mixer.music.play(-1)

menu=0

open('playerdetaillog.txt', 'w').close() #Open a log file/clear out the file contents

while True:
    for event in pygame.event.get():
        if event.type==QUIT:            #i.e. clicking the x button
            pygame.quit()
            sys.exit()

        #START SCREEN
        if menu==0:
            windowSurface.blit(pygame.transform.scale(home, (960,640)), (0,0))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if 20<=x<=256 and 253<=y<=335: #How to play
                    howtoplay((960,640))
                elif 20<=x<=352 and 368<=y<=465: #About the game
                    windowSurface.blit(pygame.transform.scale(about, (960,640)), (0,0))
                    clickedhome = False
                    while not clickedhome:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                if event.type==QUIT:            #i.e. clicking the x button
                                    pygame.quit()
                                    sys.exit()
                                x,y=event.pos
                                if 10<=x<=155 and 518<=y<=635: #Home button in About section
                                    clickedhome = True
                        pygame.display.update()
                elif 20<=x<=130 and 133<=y<=220: #Start game
                    menu=1

        #player number screen
        while menu==1:
            windowSurface.blit(pygame.transform.scale(playerscreen, (960,640)), (0,0))
            buttonclick=button.get_rect(center=(116,347))
            windowSurface.blit(button, buttonclick)
            for event in pygame.event.get():
                if event.type==QUIT: #i.e. clicking the x button
                    pygame.quit()
                    sys.exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    x,y=event.pos
                    playerno=0
                    if buttonclick.collidepoint(x,y): #Home
                        menu=0
                    elif 345<=x<=610 and 137<=y<=367: #1
                        playerno=1
                    elif 625<=x<=888 and 137<=y<=367: #2
                        playerno=2
                    elif 345<=x<=610 and 380<=y<=612: #3
                        playerno=3
                    elif 625<=x<=888 and 380<=y<=612: #4
                        playerno=4
                    if playerno>0:
                        menu=2
            pygame.display.flip()

        #Player name input and token select
        if menu==2:
            playerinputdone=Playerinput(playerno)
            if not playerinputdone:
                menu=1
                break
            else:
                menu=3
            pygame.display.flip()

        #False loading screen showing tips
        if menu==3:
            Tips(PLAYERTOKENS,SUPER)
            menu=4
        #The Game
        if menu==4:
            pygame.time.delay(2000)
            windowSurface.fill(ORANGE)
            p=1
            for i in range(4):
                if DETAILS[i]==[]:
                    break
                else:
                    if DETAILS[i][0][1]=='CPU'+str(p):
                        p+=1
                        Players[i]=AI(DETAILS[i][0][1],DETAILS[i][0][0]) #creating AI class objects

                    else:
                        Players[i]=Player(DETAILS[i][0][1],DETAILS[i][0][0]) #creating Player class object
            for player in Players:
                if player==0:
                    Players=Players[0:Players.index(player)]
                    break

            print "Writing...."

            target=open('playerdetaillog.txt','a')

            for i in Players:
                line1=i.Name
                for j in range(8):
                    if tokenlist[j]==i.Peg:
                        if j==0:
                            line2='Car'
                        elif j==1:
                            line2='Dog'
                        elif j==2:
                            line2='Thimble'
                        elif j==3:
                            line2='Trolley'
                        elif j==4:
                            line2='Ship'
                        elif j==5:
                            line2='Iron'
                        elif j==6:
                            line2='Hat'
                        elif j==7:
                            line2='Shoe'
                        break
                target.write(line1)
                target.write("\n")
                target.write(line2)
                target.write("\n")
            target.close()
            #execute GAME
            import GAME

            pygame.display.flip()
    pygame.display.flip() #updates the screen


"""for input eztezt -
txtbx.update(pygame.event.get())
txtbx.draw(windowSurface) """

'''refer to these for mouse clicks at menu

start (20,133), (130,133), (130,220), (20,220)

how to play (20, 253), (256,253), (256,335), (20,335)

about (20,368), (352,368), (352,465), (20,465)

1 (345,137), (610,137), (610,367), (345,367)
2 (625,137), (888,137), (888,367), (625,367)
3 (345,380), (610,380), (610,612), (345,612)
4 (625,380), (888,380), (888,612), (625,612)

'''
