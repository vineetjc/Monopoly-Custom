import pygame, sys, random,time
from pygame.locals import *

slides=[]
for i in range(2):
    a=pygame.image.load('Images//Some tips and tricks//Slide'+str(i+1)+'.JPG')
    slides.append(a)

BG=pygame.image.load('Images/settokensbg.jpg')

pygame.init()

#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32) #the tuple has pixels #display is a module within pygame
pygame.display.set_caption('Super Mumbo Epicness') #the title of window

#setup font
basicFont = pygame.font.SysFont(None, 48)

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (148,0,221)

# set up the text
text = basicFont.render('The game is loading, please wait', True, VIOLET)
text2 = basicFont.render('Setting the game board, please wait', True, BLACK)
textRect=text.get_rect(center=(480,550))
text2Rect=text2.get_rect(center=(440,100))
pygame.draw.rect(windowSurface, WHITE, (textRect.left, textRect.top, textRect.width, textRect.height))

def Tips(PLAYERTOKENS, names_and_icons):
    dot=basicFont.render(".",True,VIOLET)

    DETAILS=[[] for i in range(4)] #contains image and name of player
    k=0
    for i in range(len(PLAYERTOKENS)):
        if names_and_icons[i]==0:
            DETAILS[i].append((PLAYERTOKENS[i], 'CPU'+str(k+1)))
            k+=1
        else:
            DETAILS[i].append((PLAYERTOKENS[i], names_and_icons[i][0]))

    #False Loading Screen part 1 - 'Tips and tricks'
    i=750
    j=0
    times=1
    while times<30:
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

        times+=random.randint(0,2) #varying incrementor to vary false loading screen time
        if times>14:
            j=1
        pygame.display.update()
    pygame.display.flip()

    #False Loading Screen part 2 - 'Setting game tokens on board' visual
    i=740
    dot = basicFont.render(".", True, BLACK)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        x=150
        y=0
        settokens=[]
        m=0 #keeps count of how many tokens displayed
        for token in PLAYERTOKENS:
            while y<=300:
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                temp = m #to set back m value at end, ref. variable
                windowSurface.blit(pygame.transform.scale(BG, (960,640)), (0,0))
                windowSurface.blit(text2, text2Rect)

                #dot dot dot
                dotRect = dot.get_rect(center=(i,100))
                windowSurface.blit(dot, dotRect)
                time.sleep(0.2)
                i+=10
                if i>770:
                    i=740

                #draw already set tokens
                for image in settokens:
                    rect=image.get_rect(center=(x-200*m, 300))
                    windowSurface.blit(image,rect)
                    pygame.display.flip()
                    m-=1
                if m==0:
                    m = temp
                box=token.get_rect(center=(x,y))
                windowSurface.blit(token,box)
                pygame.display.flip()
                y+=20
            if y>300:
                settokens.append(token)
            x+=200
            y=0
            m+=1
            if m==len(PLAYERTOKENS):
                print names_and_icons
                print PLAYERTOKENS
                print DETAILS
                return DETAILS
            pygame.display.flip()
        pygame.display.flip()
