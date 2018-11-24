"""import random,sys

class Vineet:
    def __init__(self):
        self.Doublecount=0
        self.Position=1

    def Move(self): #visual: associate pictures with a and b
        if self.Doublecount<3:
            #this is for dice roll, two variables give dice effect
            a=5
            b=5
            if a==b:
                self.Doublecount+=1
            Roll=a+b
            if self.Doublecount==3:
                print 'youre in jail dude' #self.Jail()
                sys.exit()
            else: #visual of token movement
                print 'vineet'
                '''q=self.Position
                p=1
                while p<=Roll:
                    if q==40:
                        q=0
                        self.Cash+=200                    
                    o=q
                    self.Position=o+1
                    BoardDisplay()
                    LeftBar()
                    RightBar()
                    PlayerSpaces(self.Position)
                    pygame.display.flip()
                    pygame.time.delay(300)
                    q+=1
                    p+=1 #end of token visual

                #action decide
                if self.Position in [6,16,26,36]:
                    self.Teleportland()
                    break
                if self.Position in [13,29]:
                    self.SMEland()
                    break
                if self.Position in [8,23,37]:
                    self.Chance()
                    break
                if self.Position in [3,18,34]:
                    self.Communitychest()
                    break
                if self.Position in [5,39]:
                    self.Tax()
                    break            
                if self.Position in [1,11]:
                    pass
                if self.Position==31:
                    self.Jail()
                    break
                if self.Position==21:
                    self.FreeParking()
                    break            
                else:
                    self.Propertyland()
                    break'''
        if a==b:
            self.Move()
    
hello=Vineet()
hello.Move()
"""
'''
import pygame,os
pygame.init()
pygame.mixer.init()
windowSurface = pygame.display.set_mode((400,400), 0, 32)  

pygame.mixer.music.load('Sound Track/Game Music.mp3')
pygame.mixer.music.play(-1)

while True:
    windowSurface.fill((0,0,0))
    pygame.display.flip()
    windowSurface.fill((255,0,0))
    pygame.display.flip()
    for event in pygame.event.get():
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            print 'keft'
            pygame.time.delay(1500)
            execfile('temporary.py')
            #os.system('temporary.py')
'''
Players=[1,2,3,4]
def Function(Players):
    done=False
    while done==False:
        print 'hi'
        inputa=input('enter 5:')
        if inputa==5:
            Function2(Players)
def Function2(Players):
    print Players
    print 'vineet is awesome'

Function(Players)
