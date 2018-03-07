import pygame, sys, random,time
from tokenselect import PLAYERTOKENS, SUPER
from pygame.locals import *
slides=[]
for i in range(2):
    a=pygame.image.load('Some tips and tricks//Slide'+str(i+1)+'.jpg')
    slides.append(a)

BG=pygame.image.load('Images/bg1.jpg')

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

clock=pygame.time.Clock()

# set up the text
text = basicFont.render('The game is loading, please wait', True, VIOLET)
text2 = basicFont.render('Setting the game board, please wait', True, BLACK)
#dot dot dot
dot=basicFont.render(".",True,VIOLET)

#get_rect() "gets" a "rect"angle 
textRect=text.get_rect(center=(480,550)) 
text2Rect=text2.get_rect(center=(440,100))
#pygame.draw.rect(windowSurface, WHITE, (dotRect.left, dotRect.top, dotRect.width, dotRect.height))    #draw rectangle of text
pygame.draw.rect(windowSurface, WHITE, (textRect.left, textRect.top, textRect.width, textRect.height))

P1DETAILS=[]
P2DETAILS=[]
P3DETAILS=[]
P4DETAILS=[]
DETAILS=[P1DETAILS,P2DETAILS,P3DETAILS,P4DETAILS] #contains image and name of player
def Tips(PLAYERTOKENS,SUPER):
    g=0 #initializing variable for CPU numbers
    for t in range(len(PLAYERTOKENS)):
        if SUPER[t]==0:
            DETAILS[t].append((PLAYERTOKENS[t],'CPU'+str(g+1)))
            g+=1
        else:
            DETAILS[t].append((PLAYERTOKENS[t],SUPER[t][0]))
        print 'ok'
    i=750
    j=0
    times=1
    global dot
    while times<30:
        clock.tick(30)    
        for event in pygame.event.get():   
            if event.type==QUIT:
                pygame.quit()
                sys.exit()    

        windowSurface.blit(pygame.transform.scale(slides[j], (960,640)), (0,0))
        windowSurface.blit(text, textRect)
        #the dot dot dot loading        
        dotRect = dot.get_rect(center=(i,550))                
        windowSurface.blit(dot, dotRect)
        time.sleep(0.5)
        i+=10
        if i>780:
            i=750
        times+=random.randint(0,2)
        if times>14:
            j=1
        pygame.display.update()
    pygame.display.flip()
    loop=1
    i=740
    dot=basicFont.render(".",True,BLACK)
    while loop==1:
        clock.tick(30)    
        for event in pygame.event.get():   
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        k=150
        l=0
        temp=[]
        m=0 #keeps count of how many tokens displayed
        for token in PLAYERTOKENS:
            while l<=300:
                q=m #to set back m value at end, ref. variable
                windowSurface.blit(pygame.transform.scale(BG, (960,640)), (0,0))
                windowSurface.blit(text2, text2Rect)
                dotRect = dot.get_rect(center=(i,100))                
                windowSurface.blit(dot, dotRect)
                time.sleep(0.2)
                i+=10
                if i>770:
                    i=740
                for image in temp:
                    rect=image.get_rect(center=(k-200*m, 300))
                    windowSurface.blit(image,rect)
                    pygame.display.flip()
                    m-=1
                if m==0:
                    m=q
                box=token.get_rect(center=(k,l))
                windowSurface.blit(token,box)
                pygame.display.flip()
                l+=20
            if l>300:
                temp.append(token)
            k+=200
            l=0
            m+=1
            if m==len(PLAYERTOKENS):
                print DETAILS
                return
            pygame.time.delay(600)
            pygame.display.flip()
        pygame.display.flip()
