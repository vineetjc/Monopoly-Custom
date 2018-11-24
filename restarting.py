import pygame, time, random
#initialize pygame
pygame.init()

#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32)
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

pygame.mixer.music.stop()
execfile('GAME.py')
