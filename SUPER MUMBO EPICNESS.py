import pygame, sys, random,time, eztext
from howtoplay import *
from playersinput import *
from Tips import *
from pygame.locals import *
from Players import *

#for initialisation of necessary steps
pygame.init()  
   
#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32) #the tuple has pixels #display is a module within pygame 
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

windowSurface.fill(WHITE)

#pictures

start=pygame.image.load('Images/monopoly-start-logo.png')
home=pygame.image.load('Images/skyline.jpeg')
about=pygame.image.load('Images/about.png')
playerscreen=pygame.image.load('Images/edit this.jpg')
button=pygame.image.load('Images/home.png')
playername=pygame.image.load('Images/bgggs.jpg')
board=pygame.image.load('Images/board.jpg')

# set up the text
text = basicFont.render('Loading', True, ORANGE,WHITE) #text color, bg color
#dot dot dot
dot=basicFont.render(".",True,ORANGE,WHITE)

#get_rect() "gets" a "rect"angle 
textRect=text.get_rect(center=(480,400)) 

#pygame.draw.rect(windowSurface, WHITE, (dotRect.left, dotRect.top, dotRect.width, dotRect.height))    #draw rectangle of text
pygame.draw.rect(windowSurface, WHITE, (textRect.left, textRect.top, textRect.width, textRect.height))
    
#temporary - line draw command (displayname, <(color)>, coordinates)
#pygame.draw.line(windowSurface, (0, 0, 255), (0, 600), (800, 0)) #this draws a cross 
'''aa is for anti aliased lines, i.e. blurring of rectangles in line'''


#MAIN PROGRAM
i=560
times=1
#setting a clock (mainly for ticks - fps) 
clock = pygame.time.Clock()
#list of players
Player1=0
Player2=0
Player3=0
Player4=0
Players=[Player1, Player2, Player3, Player4]


abra=0
while times<12:
    windowSurface.blit(pygame.transform.scale(start, (800,640)), (80,0))
    windowSurface.blit(text, textRect)
    #the dot dot dot loading        
    dotRect = dot.get_rect(center=(i,400))                
    windowSurface.blit(dot, dotRect)
    time.sleep(0.5)
    i+=10            
    if i>590:
        i=560
    if abra==0:
        if 10>times>5:
            print 'yay'
            abra=1
            pygame.mixer.init()
            pygame.mixer.music.load('Sound Track/Track2.mp3')
            pygame.mixer.music.play(-1)            
    times+=random.randint(0,2)                
    pygame.display.update()

pygame.time.delay(2000)
menu=0

open('pythontest.txt', 'w').close() #just to clear out the file contents

while True:    
    for event in pygame.event.get():    #event is a pygame module to manage "events" in the program
        if event.type==QUIT:            #i.e. clicking the x button
            pygame.quit()
            sys.exit()                  #quit whole program function
        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            print "mouse at",(x,y)

#START SCREEN    
        if menu==0:
            windowSurface.blit(pygame.transform.scale(home, (960,640)), (0,0))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos                              
                if 20<=x<=256 and 253<=y<=335:
                    windowSurface.fill(BLACK)
                    print "you clicked HOW TO PLAY"
                    howtoplay((960,640))                        
                elif 20<=x<=352 and 368<=y<=465:                  
                    print "you clicked ABOUT THE GAME"                    
                    windowSurface.blit(pygame.transform.scale(about, (960,640)), (0,0))
                    A=1
                    while A==1:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                x,y=event.pos
                                if 10<=x<=155 and 518<=y<=635:
                                    print "clicked home"
                                    A=0                                
                        pygame.display.update()                    
                elif 20<=x<=130 and 133<=y<=220:
                    print "you clicked START"
                    menu=1
#CLICKED START
        while menu==1:
            #player number screen
            clock.tick(30)
            windowSurface.blit(pygame.transform.scale(playerscreen, (960,640)), (0,0))
            buttonclick=button.get_rect(center=(116,347))
            windowSurface.blit(button,buttonclick)            
            for event in pygame.event.get():    #event is a pygame module to manage "events" in the program
                if event.type==QUIT:            #i.e. clicking the x button
                    pygame.quit()
                    sys.exit()                  #quit whole program function
                elif event.type == pygame.MOUSEMOTION:
                    x, y = event.pos
                    print "mouse at",(x,y)
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    x,y=event.pos
                    playerno=0
                    if buttonclick.collidepoint(x,y):
                        print "Clicked home"
                        menu=0
                    elif 345<=x<=610 and 137<=y<=367:
                        print "you clicked 1"
                        playerno=1
                    elif 625<=x<=888 and 137<=y<=367:
                        print "you clicked 2"
                        playerno=2
                    elif 345<=x<=610 and 380<=y<=612:
                        print "you clicked 3"
                        playerno=3
                    elif 625<=x<=888 and 380<=y<=612:
                        print "you clicked 4"
                        playerno=4
                    if playerno in [1,2,3,4]:
                        menu=2        
            pygame.display.flip()

#after choosing no. of players                
        if menu==2:
            for event in pygame.event.get():   
                if event.type==QUIT:
                    pygame.quit()
                    sys.exit()
            #need to work on this still
                variable=Playerinput(playerno)
                if variable==1:
                    print "dude we're here"
                    blah=0
                    menu=1
                    break
                else:
                    menu=3                
                pygame.display.flip()
#before the game
        if menu==3:
            Tips(PLAYERTOKENS,SUPER)
            #pygame.time.delay(3000)
            menu=4
#the actual game    
        if menu==4:
            pygame.time.delay(2000)
            print 'we do the game from here'
            windowSurface.fill(ORANGE)
            print 'DETAILS:', DETAILS
            p=1
            for i in range(4):
                if DETAILS[i]==[]:
                    break
                else:
                    if DETAILS[i][0][1]=='CPU'+str(p):
                        print 'Hi I am CPU'+str(p)
                        p+=1
                        Players[i]=AI(DETAILS[i][0][1],DETAILS[i][0][0]) #creating AI class objects
                        
                    else:
                        print 'Hi I am Player'+str(i+1)
                        Players[i]=Player(DETAILS[i][0][1],DETAILS[i][0][0]) #creating Player class object
            for player in Players:
                if player==0:
                    print 'ande ka funda'
                    Players=Players[0:Players.index(player)]
                    break

            print "Writing...."

            target=open('pythontest.txt','a')

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
            #execfile('GAME.py')
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
