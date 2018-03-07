import pygame, sys, random
from pygame.locals import *
#for initialisation of necessary steps
pygame.init()  
import ctypes #foreign function library, provides C compatible data types etc.

user32 = ctypes.windll.user32
screenSize =  user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
size=(screenSize)
#setup the window display
windowSurface = pygame.display.set_mode((size), 0, 32) #the tuple has pixels #display is a module within pygame 
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

#for the chance/community chest version
otherversion=16
otherturn=5

#for the jail version
jailversion=25
jailturn=6

Earnings=1

def SEARCH(Turns,Version):
    if Version==25:
        KEYPIC=pygame.image.load('Images/THE KEY.jpg')        
        BG=pygame.image.load('Images/jail background.jpg')
        KEYDICT={} #for storing b as key to a picture as value
        INDEX=0 #for traversing through constants list

        rects=[0 for i in range(Version)] #list for boxes in the game
        blacklist=[] #stores numbers of the boxes clicked (already)
        key1=random.randint(1,Version)
        keylist=[key1]
        pictures=[KEYPIC]
        constants=[0]
        
    if Version==16:#chance/community chest
        global Earnings
        pic1=pygame.image.load('Images/search coin 75.jpg')
        pic2=pygame.image.load('Images/search coin 50.jpg')
        pic3=pygame.image.load('Images/search coin 25.jpg')
        BGlist=[pygame.image.load('Images/treasure.jpg'),pygame.image.load('Images/money.jpg')]
        R=random.randint(0,1) #just to choose random background
        BG=BGlist[R]

        pictures=[pic1,pic2,pic3]

        clickedlist=[0,0,0] #to store ones that already clicked to relate to MONEY dict.
        MONEY={pic1:75, pic2:50, pic3:25} #this is to get earnings

        '''constant variables for picture display in the main loop '''
        m=2 #for referring to length of pictures list
        j=random.randint(0,m) #for referring to picture list index in random selection
        p=random.randint(0,m)
        while p==j:
            p=random.randint(0,m)
        q=random.randint(0,m)
        while q==p or q==j:
            q=random.randint(0,m)

        print j,p,q, 'are the constant variables'
        constants=[j,p,q]

        KEYDICT={} #for storing b as key to a picture as value
        INDEX=0 #for traversing through constants list

        rects=[0 for i in range(Version)] #list for boxes in the game
        blacklist=[] #stores numbers of the boxes clicked (already)
        key1=random.randint(1,Version)
        key2=random.randint(1,Version)
        while key2==key1: #for no equal keys
            key2=random.randint(1,Version)
        key3=random.randint(1,Version)
        while key3==key1 or key3==key2:
            key3=random.randint(1,Version)

        print key1, key2, key3
        keylist=[key1,key2,key3]

    turncount=0 #to check turn count
    wincount=0 #to check if successfully selected a key

    ayyo=0 #loop variable

    b=0 #to set default value 
    while ayyo==0:
        right=50
        down=50
        horizontal=100
        vertical=100
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                print 'clicked box',
                for i in rects:
                    if i.collidepoint(pos):
                        print i.center
                        print rects[key1-1].center
                        from math import sqrt
                        distance=sqrt((i.center[0]-rects[key1-1].center[0])**2 + (i.center[1]-rects[key1-1].center[1])**2)
                        print distance
                        # distance to colour 
                        if distance<=100:
                            therm=pygame.image.load('Images/thermo+12Red.jpg')                            
                        if 100<distance<=142:
                            therm=pygame.image.load('Images/thermo+11VermRed.jpg')
                        if 142<distance<=200:
                            therm=pygame.image.load('Images/thermo+10Vermillion.jpg')
                        if 200<distance<=224:
                            therm=pygame.image.load('Images/thermo+9DOrange.jpg')
                        if 224<distance<=283:
                            therm=pygame.image.load('Images/thermo+8Orange.jpg')
                        if 283<distance<=300:
                            therm=pygame.image.load('Images/thermo+7Orangyish.jpg')
                        if 300<distance<=317:
                            therm=pygame.image.load('Images/thermo+6Yellow.jpg')
                        if 317<distance<=361:
                            therm=pygame.image.load('Images/thermo+5Yellow.jpg')
                        if 361<distance<=400:
                            therm=pygame.image.load('Images/thermo+4Yellow.jpg')
                        if 400<distance<=413:
                            therm=pygame.image.load('Images/thermo+3Yellow.jpg')
                        if 413<distance<=425:
                            therm=pygame.image.load('Images/thermo+2Yellow.jpg')                            
                        if 425<distance<=448:
                            therm=pygame.image.load('Images/thermo+1PaleYellow.jpg')
                        if 448<distance<=500:
                            therm=pygame.image.load('Images/thermoPaleYellow.jpg')
                        if 500<distance<=566:
                            therm=pygame.image.load('Images/thermoLightBlu.jpg')
                            
                        windowSurface.blit(therm,therm.get_rect(center=(8*size[0]/10,size[1]/2)))                        
                        clicked=i
                        b=rects.index(i)+1
                        if b not in blacklist:
                            blacklist.append(b)
                            KEYDICT[b]=pictures[constants[INDEX]]                        
                        else:
                            print 'clicked already'
                            b=-100
                            print 'turn count is :', turncount
                            break
                        print b
                        turncount+=1
                        break
                
                if b==0: #i.e. clicked outside the boxes
                    print 'hello'
                    break
                    #turncount-=1
                if b==-100:
                    print 'this is clicked already why are you here again'
                else:
                    #black rectangle background
                    blackrect=pygame.draw.rect(windowSurface,BLACK,(clicked.left,clicked.top,clicked.width,clicked.height))
                    if b in keylist:
                        if Version==16:
                            clickedlist[INDEX]=pictures[constants[INDEX]]
                        text=basicFont.render('BING!',True,ORANGE,BLACK)
                        INDEX+=1
                        if Version==25:
                            wincount+=3
                        else:
                            wincount+=1
                    else:
                        text=basicFont.render(str(b),True,ORANGE,BLACK)
                    textbox=text.get_rect(center=(clicked.centerx,clicked.centery))
                    windowSurface.blit(text,textbox)
                    pygame.display.flip()
                    pygame.time.delay(500)
                    b=0 #reset value
                    if turncount==Turns:
                        if wincount==3:
                            continue
                        else:
                            if Version==25: #checks jail version
                                if wincount!=3:
                                    print 'oh no you are out of turns!!!!!! :O '
                                    ayyo=1
                                    print 'blacklist', blacklist
                                    text=basicFont.render('GAME OVER', True, BLACK)
                                    textbox=text.get_rect(center=(700,100))
                                    windowSurface.blit(text,textbox)
                                    pygame.display.flip()
                                    pygame.time.delay(1500)
                                    
                            if Version==16: #checks coin version
                                global Earnings
                                Earnings=0 #total earning variable
                                for i in clickedlist:
                                    try:
                                        Earnings+=MONEY[i]
                                    except KeyError:
                                        pass
                                print 'oh no you are out of turns!!!!!! :O '
                                ayyo=1
                                print 'blacklist', blacklist
                                text=basicFont.render('GAME OVER', True, BLACK)
                                textbox=text.get_rect(center=(700,100))
                                windowSurface.blit(text,textbox)
                                pygame.display.flip()
                                pygame.time.delay(1500)
                                print 'YOU EARNED =', Earnings
                                return Earnings
                            
        windowSurface.blit(pygame.transform.scale(BG,(size)),(0,0)) #need to change bg w.r.t. game version
        for i in range(Version):
            if i+1 in blacklist:
                if i+1 in keylist:
                    a=pygame.draw.rect(windowSurface, BLACK, (right,down,horizontal,vertical),2)
                    picture=KEYDICT[i+1]               
                    box=picture.get_rect(center=(rects[i].centerx,rects[i].centery))
                    windowSurface.blit(pygame.transform.scale(picture, (100,100)), (right,down,horizontal,vertical))
                else:
                    a=pygame.draw.rect(windowSurface, BLACK, (right,down,horizontal,vertical))
            else:
                a=pygame.draw.rect(windowSurface, BLACK, (right,down,horizontal,vertical),2) #first 2 are right and down position, next 2 are horizontal and vertical sides
            rects[i]=a
            right+=100
            if right==(50+100*(Turns-1)):
                down+=100
                right=50
        try:
            latest=therm
            windowSurface.blit(therm,therm.get_rect(center=(8*size[0]/10,size[1]/2)))
        except NameError:
            pass
        if wincount==3:
            pygame.time.delay(500)
            if Version==16: #coin version
                #global Earnings
                Earnings=0 #total earning variable
                for i in clickedlist:
                    try:                        
                        Earnings+=MONEY[i]
                    except KeyError:
                        pass
                print 'you win', Earnings,'!!!!!!!!!!!'                
                ayyo=1
                text=basicFont.render('YOU WIN!', True, BLACK)
                textbox=text.get_rect(center=(700,100))
                windowSurface.blit(text,textbox)
                pygame.display.flip()
                pygame.time.delay(1000)
                return Earnings

            if Version==25: #jail version
                box=KEYPIC.get_rect(center=(800,300))
                print 'you win!'
                ayyo=1
                text=basicFont.render('YOU WIN!', True, BLACK)
                textbox=text.get_rect(center=(700,100))
                windowSurface.blit(text,textbox)
                windowSurface.blit(KEYPIC,box)
                pygame.display.flip()
                pygame.time.delay(1000)

        pygame.display.flip()



#SEARCH(otherturn,otherversion)

SEARCH(jailturn,jailversion)
