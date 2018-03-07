#IT WORKS!!!!!!! B| 

import pygame, sys, random,time, eztext
from pygame.locals import *

pygame.init()

#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32) #the tuple has pixels #display is a module within pygame 
pygame.display.set_caption('Super Mumbo Epicness') #the title of window

#setup font
basicFont = pygame.font.SysFont(None, 48)

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148,0,221)
ORANGE = (255,140,0)
YELLOW=(255,215,0)

Car=pygame.image.load('Tokens/Car.jpeg')
Dog=pygame.image.load('Tokens/Dog.jpeg')
Thimble=pygame.image.load('Tokens/Thimble.jpeg')
Trolley=pygame.image.load('Tokens/Trolley.jpeg')
Ship=pygame.image.load('Tokens/Ship.jpeg')
Iron=pygame.image.load('Tokens/Iron.jpeg')
Hat=pygame.image.load('Tokens/Hat.jpeg')
Shoe=pygame.image.load('Tokens/Shoe.jpeg')

start=pygame.image.load('Images/home.png')
back=pygame.image.load('Images/back.png')
startbox=start.get_rect(center=(71,585))
backbox=back.get_rect(center=(40,18.5))
togame=pygame.image.load('Images/ok.jpg')
togamebox=togame.get_rect(center=(920,640-18.5))

BG=pygame.image.load('Images/images.jpg')
playercolour=[RED,GREEN,BLUE,YELLOW]
tokenlist=[Car,Dog,Thimble,Trolley, Ship, Iron, Hat, Shoe]
PLAYERTOKENS=[]
SUPER=[0 for i in range(4)]
def tokenselect(playerno,MEGALIST):
    print "started from the bottom now we are here"
    global variable
    blacklist=[] #for keeping count of selected tokens
    #SUPER=[0 for i in range(playerno)]
    playericons=['null' for i in range(playerno)]
    carbox=dogbox=thimblebox=trolleybox=shipbox=ironbox=hatbox=shoebox='null'
    rectangles=[carbox,dogbox,thimblebox,trolleybox,shipbox,ironbox,hatbox,shoebox]
    i=1
    q=0
    x=0 #to stop appending infinite in blacklist
    while 0<i<=playerno+1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                if backbox.collidepoint(pos):
                    if i>0:
                        i-=1
                        if i==0: #goes back to playersinput
                            print "HHhalelujah"
                            return 10001
                            break
                        q-=1
                        for l in rectangles:
                            if x==i:
                                if l==i:                                    
                                    blacklist.pop()                                    
                                    rectangles[rectangles.index(l)]='changed'                                    
                                    x-=1                                    
                        x=0
                        break
                       
                if startbox.collidepoint(pos):
                    print "home"
                    return 10 #then to main program
                if i>playerno:
                    if togamebox.collidepoint(pos):
                        print SUPER
                        print 'finished'
                        print playericons
                        print rectangles
                        v=1
                        while v<=len(playericons):
                            for i in range(8):
                                if type(rectangles[i])==int:
                                    if rectangles[i]==v:
                                        PLAYERTOKENS.append(tokenlist[i])
                                        v+=1
                        print
                        print PLAYERTOKENS
                        print
                        print blacklist
                        print
                        print MEGALIST
                        
                        
                    
                #print SUPER #which contains tuples of name and image 
                if i<=playerno:
                    for k in rectangles:
                        if type(k)!=int:
                            if k.collidepoint(pos):
                                playericons[q]=k
                                SUPER[q]=(MEGALIST[i-1],k)
                                i+=1
                                q+=1
                                x=0
                                rectangles[rectangles.index(k)]=i-1 #change rectangle type to int
                                break
                    
            j=130
            windowSurface.blit(pygame.transform.scale(BG, (960,640)), (0,0))
            if x==0:
                blacklist=[]
                for d in range(i-1):
                    blacklist.append('-') #fixing blacklist length every selection
                x+=1
            x=0
            for e in range(len(rectangles)):
                if e<4:
                    k=240
                if e==4:
                    j=130
                if e>=4:
                    k=400
                buttonclick=tokenlist[e].get_rect(center=(j,k))
#need to fix the black to white thing. need to set temporary variable
#as recently blackened image

                if type(rectangles[e])==int:
                    if x<i-1:
                        blacklist[x]=(rectangles[e])#check for ones already finished
                        x+=1
                    pygame.draw.rect(windowSurface, BLACK, (buttonclick.left, buttonclick.top, buttonclick.width, buttonclick.height))                
                else:
                    rectangles[e]=buttonclick
                    pygame.draw.rect(windowSurface, WHITE, (buttonclick.left, buttonclick.top, buttonclick.width, buttonclick.height))
                        
                windowSurface.blit(tokenlist[e],buttonclick)
                j+=240
                
            if i>playerno:
                fini=basicFont.render('Click OK to proceed to game!', True, VIOLET)
                box=fini.get_rect(center=(500,600))
                windowSurface.blit(fini,box)
                windowSurface.blit(togame,togamebox)
                #put OK and to game
            else:
                prompts = basicFont.render('Player '+str(i)+" "+MEGALIST[q]+' choose your token', True, VIOLET) #text color, bg color
                box=prompts.get_rect(center=(500,600))
                windowSurface.blit(prompts,box)
                
            windowSurface.blit(start,startbox)
            windowSurface.blit(back,backbox)
            pygame.display.flip()
        pygame.display.flip()
    if len(MEGALIST)>playerno:
        F=-1 #some initial value
        diff=len(MEGALIST)-playerno
        for i in range(diff):
            R=random.randint(0,7)
            while R==F:
                R=random.randint(0,7)
            F=R #reference variable
            while tokenlist[R] in PLAYERTOKENS:
                R=random.randint(0,7)
            PLAYERTOKENS.append(tokenlist[R])
    print
    print PLAYERTOKENS
    return 10002
#print tokenselect(2,['a','b','CPU1','CPU2'])
