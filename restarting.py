import pygame,time,random
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

times=1
start=pygame.image.load('Images/monopoly-start-logo.png')
# set up the text
text = basicFont.render('Restarting', True, ORANGE,WHITE) #text color, bg color
#dot dot dot
dot=basicFont.render(".",True,ORANGE,WHITE)

#get_rect() "gets" a "rect"angle 
textRect=text.get_rect(center=(470,400))
i=560
pygame.mixer.music.stop() 
while times<12:
    windowSurface.fill((255,255,255))
    windowSurface.blit(pygame.transform.scale(start, (800,640)), (80,0))
    windowSurface.blit(text, textRect)
    #the dot dot dot loading        
    dotRect = dot.get_rect(center=(i,400))                
    windowSurface.blit(dot, dotRect)
    time.sleep(0.5)
    i+=10            
    if i>590:
        i=560          
    times+=random.randint(0,2)                
    pygame.display.update()

pygame.time.delay(2000)
execfile('GAME.py')

