import pygame, sys, random
from pygame.locals import *
#initialize pygame
pygame.init()

size=(1024,768)
#setup the window display
windowSurface = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('Super Mumbo Epicness') #the title of window
#pygame.display.set_mode((size) , pygame.FULLSCREEN)
# set up fonts
basicFont = pygame.font.SysFont(None, 48) #none is for default system font, number is size of font
Font = pygame.font.SysFont(None, 32)
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

def ScratchCard():
    prizelist=[pygame.image.load('Images/150.png'),pygame.image.load('Images/200.jpg'),pygame.image.load('Images/250.png'),pygame.image.load('Images/300.jpg')]
    image=prizelist[random.randint(0,3)]
    bg=pygame.image.load('Images/gold-frame.jpg')
    grey=pygame.image.load('Images/silver scratchy.jpg')
    done=False
    text=pygame.image.load("Images/you_ve won text.png")
    box=text.get_rect(center=(1024/2,(768/2)-150))
    text2=pygame.image.load('Images/scratch text.png')
    box2=text2.get_rect(center=(500,43*size[1]/100))
    windowSurface.blit(bg,bg.get_rect())
    windowSurface.blit(text,box)
    windowSurface.blit(text2,box2)
    windowSurface.blit(grey,(size[0]/2-330,49*size[1]/100),(0,0,660,260))
    while not done:
        b=pygame.key.get_pressed()
        if b[pygame.K_LEFT]:
            print 'vineet'
        for event in pygame.event.get():
            mouse=pygame.mouse.get_pressed()
            if mouse[0]: #i.e. is 'scratching'
                #print 'yay'
                try:
                    x,y=event.pos
                except:
                    pass

                if 182<=x<=840 and 384<=y<=628:
                    a=windowSurface.blit(image,(event.pos[0]-10,event.pos[1]-10),(event.pos[0],event.pos[1],20,20)) #image, (at this place), (top,left,this much area)
                else:
                    pass
            else:
                pass
                #print 'no' #i.e. isn't 'scratching'
        try:
            a
        except UnboundLocalError:
            pass
        pygame.display.flip()

ScratchCard()
