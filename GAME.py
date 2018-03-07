#need to get layouts, options

#DETAILS list has (image,name) of players in it. need to get it here!!! :D
import pygame, sys, random,time
from pygame.locals import *
from howtoplay import *
from settin import *
from manage import *
from Players import *
from trade import *

#for initialisation of necessary steps
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Sound Track/Nanana.mp3')
pygame.mixer.music.set_volume(0.17) #need to decide this versus other SFX
pygame.mixer.music.play(-1)
pygame.time.delay(700)


#reading file and making Players

from tokenselect import tokenlist

tokennames=['Car','Dog','Thimble','Trolley','Ship','Iron','Hat','Shoe']

load_profile = open('pythontest.txt','r')

print 'reading....'
print load_profile.read()

load_profile = open('pythontest.txt','r')

for i, l in enumerate(load_profile):#print i,l prints line number from 0 with content in each line!             
    pass
playerno= (i + 1)/2 #number of lines (counts from 0) 

print 'players:',playerno

load_profile = open('pythontest.txt','r')
read_it = load_profile.read().splitlines()

#playerno=file_len('pythontest.txt')/2

#print playerno

Players=[]

for i in range(playerno):
    Players.append(Player('name','peg'))


count=0
for i in range(2*playerno):
    #print read_it[i],
    if i%2==0:
        tempo=read_it[i]
    else:
        Players[count].Name=tempo
        #Players[count].Peg=read_it[i]
        for j in range(8):
            if tokennames[j]==read_it[i]:
                Players[count].Peg=tokenlist[j]
        count+=1

for i in Players:
    pict=i.Peg
    i.Peg=pygame.transform.scale(pict,(size[0]/22,size[0]/22))


#end of it


    
import ctypes #foreign function library, provides C compatible data types etc.

user32 = ctypes.windll.user32
screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
size=(screenSize)
size=(1024,768)
#setup the window display
windowSurface = pygame.display.set_mode((size), 0, 32) #the tuple has pixels #display is a module within pygame 
pygame.display.set_caption('Super Mumbo Epicness') #the title of window
#dude=pygame.display.set_mode((size) , pygame.FULLSCREEN)


# set up fonts
basicFont = pygame.font.SysFont(None, 48) #none is for default system font, number is size of font

twenty8=int(0.036458333334*size[1]) #font size for roll over displays in 1024x768 is 28

Font = pygame.font.SysFont(None, twenty8) #same thing

#set colors R,G,B code 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148,0,221)
ORANGE = (255,140,0)

#palette of complementing colours to the board
Colour1=(239,232,239) #board colour, probably only for future ref./uses
Colour2=(182,143,182) #BOX COLOUR
Colour2L=(215,194,215) #BG COLOUR

#player colours
P1Colour=(251,198,201)
P2Colour=(172,181,216)
P3Colour=(255,253,196)
P4Colour=(213,234,211)
PxColours=[P1Colour,P2Colour,P3Colour,P4Colour]

#board image
boardimg=pygame.image.load('Images/board22.jpg')

#OPTIONS: texts and boxes
rolldice=pygame.image.load('Images/Options/dicebutton.png')
diceoff=pygame.image.load('Images/Options/diceoff.png')
end=pygame.image.load('Images/Options/endturn.jpg')
endturnoff=pygame.image.load('Images/Options/endturnoff.jpg')
manage=pygame.image.load('Images/Options/manage.png')
settings=pygame.image.load('Images/Options/Settingsbutton.png')
trade=pygame.image.load('Images/Options/Trade.png')
#optionslist=[rolldice,manage,trade,end,settings]

#dice icons
dicenumbers=[]
for i in range(6):
    dicenumbers.append(pygame.image.load('Images/dice '+str(i+1)+'.png'))



BABA=0.065104166667*size[1] #the fifty
BEBE=BABA*1.16 #the fifty eight

baba=int(BABA)
bebe=int(BEBE)

#list with the ratio based sizes
optionslist=[pygame.transform.scale(rolldice,(baba,baba)),pygame.transform.scale(manage,(baba,baba)),pygame.transform.scale(trade,(bebe,baba)),pygame.transform.scale(end,(baba,baba)),pygame.transform.scale(settings,(baba,baba))]

hello=(size[1]*0.104166666667)
bello=int(hello)

iconboxes=[0 for i in range(5)]
i=size[0]/2 - (2*bello) #x coordinate of boxes

for image in optionslist:
    box=image.get_rect(center=(i,size[1]/2))
    iconboxes[optionslist.index(image)]=box
    i+=bello
    
#the central menu on the board! (complete other functions and use their call)
def BoardMenu():
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x,y = event.pos
            print x,y
            for b in range(5):
                if iconboxes[b].collidepoint(x,y):
                    if b==0:
                        popup='Roll dice'                        
                    elif b==1:
                        popup='Manage'                        
                    elif b==2:
                        popup='Trade'
                    elif b==3:
                        popup='End Turn'                        
                    elif b==4:
                        popup='Settings'                        
                    ref=b
                    break
            try:
                text=Font.render(popup,True,BLACK)
                forty=int(0.052083333334*size[1]) #used below for spacing!!!!
                box=text.get_rect(center=(iconboxes[ref].centerx,iconboxes[ref].centery+forty)) #for the spacing b/w text and icon
                windowSurface.blit(text,box)                                           
            except UnboundLocalError:
                pass
            
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            pos=event.pos
            for b in range(5):
                if iconboxes[b].collidepoint(pos):
                    if b==0:
                        global Rollcheck
                        if Rollcheck==True:
                            player.Move(dicenumbers,Players,windowSurface)
                            player.Turns+=1                            
                            Rollcheck=False
                    elif b==1:
                        print 'Manage'
                        m=Manage(player)
                        break
                    elif b==2:
                        print 'Trade'
                        t=Trade(player,Players)
                    elif b==3:
                        #global Rollcheck
                        if Rollcheck==False:
                            print 'End Turn'
                            global loop
                            loop=1
                            print 'loop here:', loop
                        
                    elif b==4:
                        print 'Settings'
                        a=Settings() #need to fix its loop end its so annoying now
                        if a==2:
                            pygame.time.delay(1500)
                            global flag
                            flag=True
                            #execfile('restarting.py')
                            #execfile('GAME.py')
                        break                    
                    ref=b
                    break
                

        #fullscreen toggle!!! this is temporary, change method on this.
        if event.type==KEYDOWN and event.key==K_a:
            dude=pygame.display.set_mode((size))            
        if event.type==KEYDOWN and event.key==K_d:
            dude=pygame.display.set_mode((size) , pygame.FULLSCREEN)            
    for a in range(5):
        if a==0 and Rollcheck==False:
            windowSurface.blit(diceoff,iconboxes[a])
        if a==3 and Rollcheck==True:
            windowSurface.blit(endturnoff,iconboxes[a])
        else:
            windowSurface.blit(optionslist[a],iconboxes[a])
    

#the left screen division display!
def LeftBar(i,Players):
    pygame.draw.rect(windowSurface, PxColours[i], (0,0,(size[0]-size[1])/2,size[1]))
    Font.set_underline(True)
    text=Font.render('Current Turn',True,VIOLET)
    box=text.get_rect(center=(size[0]/15,size[1]/15))
    windowSurface.blit(text,box)
    Font.set_underline(False)
    blah=pygame.transform.scale2x(Players[i].Peg)
    rect=blah.get_rect(center=(size[0]/15,size[1]/5))
    windowSurface.blit(blah,rect)
    text=Font.render('Player '+str(i+1),True,BLACK)
    box=text.get_rect(center=(size[0]/15,size[1]/7))
    windowSurface.blit(text,box)
    text=Font.render('Name:',True,BLACK)
    box=text.get_rect(center=(size[0]/30,3*size[1]/10))
    windowSurface.blit(text,box)
    text=Font.render(Players[i].Name,True,BLACK)
    box=text.get_rect(center=(size[0]/15,33*size[1]/100))
    windowSurface.blit(text,box)
    text=Font.render('Cash:',True,BLACK)
    box=text.get_rect(center=(size[0]/31,4*size[1]/10))
    windowSurface.blit(text,box)
    text=Font.render(str(Players[i].Cash),True,BLACK)
    box=text.get_rect(center=(size[0]/15,43*size[1]/100))
    windowSurface.blit(text,box)
    text=Font.render('SME points:',True,BLACK)
    box=text.get_rect(center=(size[0]/17,5*size[1]/10))
    windowSurface.blit(text,box)
    text=Font.render(str(Players[i].SME),True,BLACK)
    box=text.get_rect(center=(size[0]/15,53*size[1]/100))
    windowSurface.blit(text,box)
    text=Font.render('Properties:',True,BLACK)
    box=text.get_rect(center=(size[0]/18,6*size[1]/10))
    windowSurface.blit(text,box)
    
#the right screen division display!
def RightBar(Players):
    right = (size[0]-size[1])/2 + size[1]
    box=pygame.draw.rect(windowSurface, GREEN, (right,0,(size[0]-size[1])/2,size[1]))
    yuhoo=13 #centery of boxes
    for boy in Players:
        Font.set_underline(True)
        text=Font.render('Player '+str(Players.index(boy)+1),True,BLACK)
        box=text.get_rect(center=(right+(size[0]-size[1])/4,yuhoo+5))
        pygame.draw.rect(windowSurface,PxColours[Players.index(boy)],(right,box.top-5,(size[0]-size[1])/2,box.height+150))        
        windowSurface.blit(text,box)
        Font.set_underline(False)
        yalla=pygame.draw.line(windowSurface, BLACK, (right,box.top-7), (size[0],box.top-7), 5)
        text=Font.render(boy.Name,True,BLACK)
        box=text.get_rect(center=(right+(size[0]-size[1])/4,yuhoo+35))
        windowSurface.blit(text,box)
        box=boy.Peg.get_rect(center=(right+(size[0]-size[1])*3/8,yuhoo+66))
        windowSurface.blit(boy.Peg,box)
        networth=boy.Cash
        for prop in boy.Owned:
            networth+=prop.Price
        text=Font.render("$"+str(networth),True,BLACK) #replace with NetWorth
        box=text.get_rect(center=(right+(size[0]-size[1])/8,yuhoo+55))
        windowSurface.blit(text,box)
        text=basicFont.render("*",True,RED)
        box=text.get_rect(center=(right+(size[0]-size[1])/32,yuhoo+85))
        windowSurface.blit(text,box)
        text=Font.render(str(boy.SME),True,RED)
        box=text.get_rect(center=(right+(size[0]-size[1])/12,yuhoo+77))
        windowSurface.blit(text,box)        
        yuhoo+=200
        pygame.draw.line(windowSurface, BLACK, (right,box.bottom+70), (size[0],box.bottom+70), 5)
        

#keep track of player token spaces in whole game!
#Import all the pictures for tokens here, blit player tokens on the board by relating current position number to posdict value!!!!!!!!!!!!!!


#def PlayerSpaces(place):
    #box=token.get_rect(center=posdict[place])
    #windowSurface.blit(token,box)


position=(size[0]-size[1])/2 + size[1]-70
positionx = (size[0]-size[1])/2 + (0.904947916667*size[1])
positiony=size[1]-(0.065104166667*size[1])

sixtythree=0.08203125*size[1] #because in 1024x768, the step value for token is 63 

#idea : use {'position number: coordinates'}!!!! 1 is GO
posdict={1:(positionx,positiony),2:(positionx-sixtythree,positiony),3:(positionx-2*sixtythree,positiony),4:(positionx-3*sixtythree,positiony),5:(positionx-4*sixtythree,positiony),6:(positionx-5*sixtythree,positiony),7:(positionx-6*sixtythree,positiony),8:(positionx-7*sixtythree,positiony),9:(positionx-8*sixtythree,positiony),10:(positionx-9*sixtythree,positiony),11:(positionx-10*sixtythree,positiony+sixtythree/3),'Jail':(positionx-10*sixtythree,positiony-sixtythree/3),12:(positionx-11*sixtythree+(sixtythree/2),positiony-2*sixtythree+(sixtythree/2))}
posdict[13]=(posdict[12][0],posdict[12][1]-sixtythree)
for i in range(14,22):
    posdict[i]=(posdict[i-1][0],posdict[i-1][1]-sixtythree)
posdict[22]=(posdict[21][0]+2*sixtythree-(sixtythree/2),posdict[21][1])
for i in range(23,31):
    posdict[i]=(posdict[i-1][0]+sixtythree,posdict[i-1][1])
posdict[31]=(posdict[30][0]+2*sixtythree-(sixtythree/2),posdict[30][1])
for i in range(32,41):
    posdict[i]=(posdict[i-1][0],posdict[i-1][1]+sixtythree)

Token=pygame.image.load('Tokens/Dog.jpeg')
token=pygame.transform.scale(Token,(size[0]/22,size[0]/22))

Token2=pygame.image.load('Tokens/Shoe.jpeg')
token2=pygame.transform.scale(Token2,(size[0]/22,size[0]/22))


www=1

def BoardDisplay(windowSurface):
    windowSurface.blit(pygame.transform.scale(boardimg,(size[1],size[1])),((size[0]-size[1])/2,0))
    
        
player='null' #initialize variable

Rollcheck=True #this checks if he can roll dice

loop=0 #loop variable
def GAME(Players): #the list containing class objects
    #this needs work!!!!!! >.<
    global player
    global loop, flag
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                Settings()
        while True:            
            for guy in Players:
                player=guy                
                print "Its Player",str(Players.index(guy)+1),"turn"                
                while loop==0:
                    #putting quitting options for every player
                    for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        key = pygame.key.get_pressed()
                        if key[pygame.K_ESCAPE]:
                            Settings()
                    #end of the top
                    BoardDisplay(windowSurface)
                    BoardMenu()
                    if flag==True:
                        return 500                       
                    current=Players.index(guy)
                    LeftBar(current,Players)
                    RightBar(Players)
                    player.PlayerSpaces(windowSurface)
                    for ey in Players:
                        ey.PlayerSpaces(windowSurface)
                    pygame.display.flip()
                if loop==1: #end turn                    
                    for person in Players:
                        print person.Name,"has:",person.Cash,'and:',person.SME,'SMEpoints'
                        print person.Name,'Properties:',
                        for jagah in person.Owned:
                            print jagah.Name,
                        print
                    global Rollcheck
                    Rollcheck=True
                    loop=0
                    continue

'''

A=Player('Vineet',token)
B=Player('Praveena',token2)
Players=[A,B]
'''
for obj in Players: #just to make sure that position is reset before running game
    obj.Position=1
BoardDisplay(windowSurface)
flag=False
B=GAME(Players)
if B==500:
    execfile('restarting.py')

'''
I. At the center of the board (use images for buttonclicks)
-----------------------------------------------------------------------
1. Roll dice
2. Trade
3. Manage - a. properties owned list (mortgaged/not)
                    i. improve properties - house/hotel
            b. cash
            c. SMEpoints
            d. Use SME points
            e. GOOJ cards
            f. etc.
4.End turn
5. Options- a. Back to game
(toggle     b. Restart game
 with ESC   c. Help
 key)       d. Exit game
            (e. SFX and Music toggle, and screen resolution change - if we are adding)
            
***********************************************************************

II. Standard display at either sides
-----------------------------------------------------------------------
1. Left side -  Current player turn details
                    . Set left side of the player colour
                    . Token
                    . Name
                    . Cash
                    . SME points
                    . mini icons of property color cards
                        -toggle only those occupied by the player
                        -GOOJ card if present
                        -grey the mortgaged prop.
                    . etc.

2. Right side - Players names and token with networth in respective color
                small boxes
                    - if bankrupt, grey the box and disable
                    - 
***********************************************************************

III. During Roll Dice
-----------------------------------------------------------------------
On the board - At the left bottom corner below display roll of dice

***********************************************************************

IV. During landing on a place
-----------------------------------------------------------------------
At right side - At the bottom corner show image of the square landed on

Central pop up for buy/auction

If owned by another, central pop up for rent

If unmortgaged or owned by self, pass
***********************************************************************

V. During trade
-----------------------------------------------------------------------
Central screen pop up for choosing player to trade with

Left side same

At right side, replicate that of left side but with that of the player with
whom the trade is called on

Enable clicks on icons for this mode. Else disable.

Also insert a calculator like display that takes input for cash trade
***********************************************************************

VI. When using additional activities (like building, SMEpoints)
-----------------------------------------------------------------------
Central pop up as required

***********************************************************************

VII. During jail
-----------------------------------------------------------------------
Roll dice becomes 'Try doubles'

At right bottom corner insert the boxes for ways to get out of jail

Also keep count of turn in jail
***********************************************************************

VIII. Auction
-----------------------------------------------------------------------
- Player name with token, cash in hand, net worth
-Bid 5,10,50,100
-card, original value
***********************************************************************
'''
