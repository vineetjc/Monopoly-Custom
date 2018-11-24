'''import pygame, sys, random
from pygame.locals import *
#initialize pygame
pygame.init()  
#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32)  
pygame.display.set_caption('Super Mumbo Epicness') #the title of window
#set colors R,G,B code
BROWN = (139,69,19)
BROWNY=(93,35,15)
while True:
    windowSurface.fill(BROWNY)
    pygame.display.flip()
/'''

'''house coordinates
L corner 10,575
R corner 155, 575

top 80,518

bottom 37,635

so rectangle of house

(10, 518) , (155,518), (155,635), (10,635)'''
'''
from testings import *

A=Vineet('Vineet',0)
A.Loot=0

B=Vineet('Divya',15)
print B.Cash
B.somefunction(A)

print B.Cash
print
print A.Loot

print A.Name
print A.Cash
print A.Loot
'''
a=5
b=10
c=100
Dict={1:a,2:b,3:c}

a-=2

print a
print Dict
