import pygame, sys, random, math
from pygame.locals import *
#initialize pygame
pygame.init()  
import ctypes #foreign function library, provides C compatible data types etc.

user32 = ctypes.windll.user32
screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
size=(screenSize)
size=(1024,768)
#setup the window display
windowSurface = pygame.display.set_mode((size), 0, 32)  
pygame.display.set_caption('Super Mumbo Epicness') #the title of window
#pygame.display.set_mode((size) , pygame.FULLSCREEN)
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
BROWN = (139,69,19)
GOLD = (255,215,0)
YELLOW = (255,255,0)

#images
cart=pygame.image.load('Images/cart.jpg')
coin=pygame.image.load('Images/coin.jpg')
bluecoin=pygame.image.load('Images/bluecoin.jpg')
bomb=pygame.image.load('Images/bomb.png')
bg1=pygame.image.load('Images/coinfallbg1.jpg')
bg2=pygame.image.load('Images/coinfallbg2.jpg')
jailbg1=pygame.image.load('Images/coinfalljailbg.jpg')
jailbg2=pygame.image.load('Images/coinfalljailbg2.jpg')
bglist=[bg1,bg2,jailbg1,jailbg2]

#version 1 is normal, version 2 is jail
Version=1
if Version==2:
    R=random.randint(2,3)
if Version==1:
    R=random.randint(0,1)
BG=bglist[R]

class Cart(object):  
    def __init__(self):
        global cart
        self.image = cart
        self.x = (size[0]/2)-80
        self.y = size[1]-120
        self.Points=0 #this is for count of coins

    def handle_keys(self):
        key = pygame.key.get_pressed()
        dist = int(0.009765625*size[0]) #could change this one 
        if key[pygame.K_RIGHT]:
            if self.x<size[0]-140:
                self.x += dist
            if self.x>=size[0]-140:
                self.x+=0
        elif key[pygame.K_LEFT]:
            if self.x>-10:
                self.x -= dist
            if self.x<=-10:
                self.x-=0

    def draw(self, surface):        
        surface.blit(self.image, (self.x,self.y))
A=Cart()

class Coin(Cart):  #have to make this derived class to access Cart coordinates
    def __init__(self):
        global coin
        self.image=coin
        self.x=random.randint(0,size[0]-55)
        self.y=-15
    def fall(self):
        self.y+=int(0.013020833334*size[1])-3
        ''' 640-123>self.y>640-135'''
        if int(0.83984375*size[1])>self.y>int(0.82421875*size[1]):
            if A.x<self.x+(55.0/2)<(A.x+160) and A.x<self.x and A.x+160>self.x+55:
                print 'yay'
                try:
                    if self.image==bluecoin:
                        A.Points+=3 #bonus coin
                    elif self.image==bomb:
                        print 'boom'
                        global vineet
                        vineet=0
                    else:
                        A.Points+=1
                    del self.image
                    print 'points =', A.Points
                except AttributeError:
                    pass
    def draw(self,surface):
        try:
            surface.blit(self.image, (self.x,self.y))
        except AttributeError:
            pass
        
class BlueCoin(Coin): #bonus coin
    def __init__(self):
        global bluecoin
        Coin.__init__(self)
        self.image=bluecoin

class Bomb(Coin): #bomb 
    def __init__(self):
        global bomb
        Coin.__init__(self)
        self.image=bomb

def CoinGame(Version):
    global A
    global BG
    global i, coinlist, gameclock
    global Coin, BlueCoin, Bomb
    #vineet=1 #loop variable
    #gameclock = pygame.time.Clock()
    #coinlist=[]
    #i=1 #reference variable to traverse coinlist
    #while vineet==1:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    A.handle_keys()
    windowSurface.blit(pygame.transform.scale(BG,(size)),(0,0))
    A.draw(windowSurface)
    if i%3==0 or i%4==0:
        select=random.randint(1,2)
        if select==1:
            C=BlueCoin()
        if select==2:
            C=Bomb()
    elif i%5==0 or i%7==0 or i&11==0:
        C=Bomb()
    else:
        C=Coin()
    coinlist.append(C)
    for B in coinlist[0:i:15]:#use 14 or 15
        B.draw(windowSurface)
        B.fall()
    pygame.display.flip()
    i+=1
    #need to set the winner point still!!!! 
    if Version==2: #jail version
        if A.Points>=int(size[0]*45/size[1]): #set 60
            print 'you win!!!!!!'
            vineet=0
            #return vineet
#    if i==580: #this is roughly 30 seconds with +/- 1 error to the most
#        vineet=0'''

result=0
i=1
coinlist=[]
vineet=1 #loop variable
gameclock = pygame.time.Clock()    
#i=1 #reference variable to traverse coinlist        
timer=0    
print 'goal=',int(size[0]*45/size[1])
while vineet==1:
    q=CoinGame(Version)
    if q==0:
        break
    #fixed final timer!!! :D 
    seconds=gameclock.tick()/1000.0
    timer+=seconds
    displaytimer=math.trunc(timer) #returns real value of timer to integer value "truncated"
    if timer<30:
        TIME=basicFont.render('TIMER:',True,BLACK,WHITE)
        Keeper=TIME.get_rect(center=(900,170))
        windowSurface.blit(TIME,Keeper)
        TIME=basicFont.render(str(displaytimer),True,BLACK,WHITE)
        Keeper=TIME.get_rect(center=(900,200))
        windowSurface.blit(TIME,Keeper)
        pointboard=basicFont.render('POINTS:',True,BLACK,WHITE)
        Keeper=pointboard.get_rect(center=(100,170))
        windowSurface.blit(pointboard,Keeper)
        pointscore=basicFont.render(str(A.Points),True,BLACK,WHITE)
        Keeper=TIME.get_rect(center=(100,200))
        windowSurface.blit(pointscore,Keeper)
        pygame.display.flip()
    if timer>=30:
        TIME=basicFont.render(str(A.Points),True,BLACK,WHITE) #need to change this with time's up
        Keeper=TIME.get_rect(center=(850,200))
        windowSurface.blit(TIME,Keeper)
        pygame.display.flip()
        vineet=0
result=A.Points
print result
