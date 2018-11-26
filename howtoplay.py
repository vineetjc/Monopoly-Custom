import pygame, sys, random,time, eztext
from pygame.locals import *
slides=[]
for i in range(18):
    a=pygame.image.load('Images/HOW TO PLAY/slide'+str(i+1)+'.jpg')
    slides.append(a)

pygame.init()

size=(960,640)
#setup the window display
windowSurface = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('Super Mumbo Epicness') #the title of window
#dude=pygame.display.set_mode((size) , pygame.FULLSCREEN)
#setup font
basicFont = pygame.font.SysFont(None, 32)

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148,0,221)
ORANGE = (255,140,0)

clock=pygame.time.Clock()





def howtoplay(size):
    #previous and next buttons
    Prev=pygame.image.load("Images/HOW TO PLAY/Prev.png")
    Next=pygame.image.load("Images/HOW TO PLAY/Next.png")
    Prevclick=Prev.get_rect(center=(89,46))
    Nextclick=Next.get_rect(center=(size[0]-53,46))
    if size==(960,640):
        back=pygame.image.load("Images/home.png")
        backclick=back.get_rect(center=(71,size[1]-55))
    if size==(1024,768):
        back=pygame.image.load("Images/back.png")
        backclick=back.get_rect(center=(40,size[1]-(37/2)))
    i=0
    ref=1
    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                if Prevclick.collidepoint(pos):
                    if i>=1:
                        print "clicked previous"
                        i-=1
                    else:
                        pass
                if Nextclick.collidepoint(pos):
                    if i<17:
                        print "clicked next"
                        i+=1
                    else:
                        pass
                if backclick.collidepoint(pos):
                    if i==0 or i==17:
                        print "clicked home"
                        ref=0
                    else:
                        pass


            if i<=17:
                windowSurface.blit(pygame.transform.scale(slides[i], size), (0,0))
                if i>=1:
                    windowSurface.blit(Prev,Prevclick)
                else:
                    windowSurface.blit(back,backclick)
                if i<17:
                    windowSurface.blit(Next,Nextclick)

                else:
                    windowSurface.blit(back,backclick)


        if ref==0:
            break
        pygame.display.flip()

#howtoplay()
