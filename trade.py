#make a left bar, right bar and fill screen with a version of the board!

import pygame, sys, random,time
from pygame.locals import *
#initialize pygame
pygame.init()
size=(1024,768)
windowSurface = pygame.display.set_mode((size), 0, 32)  
pygame.display.set_caption('Super Mumbo Epicness') #the title of window

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148,0,221)
ORANGE = (255,140,0)

basicFont = pygame.font.SysFont(None, 32)
TradeFont = pygame.font.SysFont(None, 40)

backarrow=pygame.image.load("Images/back.png")
backbox=backarrow.get_rect(center=(40+size[0]/2-((0.78125*size[1])/2),size[0]/10.0+37/2))
def Trade(Caller,Players): #make Players list as argument
    templist=[player.Name for player in Players]
    templist.remove(Caller.Name)
    print templist
    tempboxes=[0 for i in range(len(Players)-1)]
    e=size[0]/10.0 + 120
    for word in templist:
        text=basicFont.render(word,True,WHITE)
        box=text.get_rect(center=(size[0]/2,e))
        tempboxes[templist.index(word)]=box
        e+=70
    done=False
    while not done:
        pygame.draw.rect(windowSurface,BLACK,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],0.78125*size[1]),5)
        purble=pygame.draw.rect(windowSurface,(192,192,192),(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],0.78125*size[1]))
        question=basicFont.render('Whom would you like to trade with?',True,WHITE)
        paper=question.get_rect(center=(size[0]/2,size[0]/10.0 + 70))
        windowSurface.blit(question,paper)
        windowSurface.blit(backarrow,backbox)
        for b in range(len(Players)-1):
            w=pygame.draw.rect(windowSurface,(160,160,160),(tempboxes[b].left,tempboxes[b].top-5,tempboxes[b].width,tempboxes[b].height+10))
            text=basicFont.render(templist[b],True,WHITE)
            windowSurface.blit(text,tempboxes[b])
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                if backbox.collidepoint(pos):
                    done=True
                    return
                for b in range(len(Players)-1):                
                        if tempboxes[b].collidepoint(pos):
                            target=Players[b].Name
                            for dude in Players:
                                if dude.Name==target:
                                    Party=dude
                                    break
                            accepted=False
                            while not accepted:
                                CallerBar(Caller)
                                PartyBar(Party)
                                #display some thing in middle
                                pygame.display.flip()
                            
        pygame.display.flip()

def CallerBar(Caller): #Caller is the one who activates trade
    pygame.draw.rect(windowSurface, (192,192,192), (0,0,(size[0]-size[1])/2,size[1]))

def PartyBar(Party): #Party is the receiving end
    right = (size[0]-size[1])/2 + size[1]
    box=pygame.draw.rect(windowSurface, GREEN, (right,0,(size[0]-size[1])/2,size[1]))
    
#Trade()

#trade algorithm
"""
c=0
trade1=[]
trade2=[]
while c==0:
    ppty1=raw_input("Property:")
    done=False
    while not done:
        for i in Properties:
            if i.Name==ppty1:                                        
                done=True
                break
        else:
            ppty2=raw_input("Property:") 
    money1=input("the amount:")
    trade1=[ppty1,money1]
    g=raw_input("player2 do you accept/counter/reject trade?: (y/c/n)")
    if g=="y" or g=='Y':
        print 'accepted'
        trade1,trade2=trade2,trade1
        c=1
    elif g=='n' or g=='N':
        print 'rejected'
        c=1
    elif g=='c' or g=='C':
        ppty2=raw_input("Property:")
        done=False
        while not done:
            for i in Properties:
                if i.Name==ppty2:
                    done=True
                    break
            else:
                ppty2=raw_input("Property:")                                            
        money2=input("The amount:")
        trade2=[ppty2,money]
        x=raw_input("Player 1 do you accept/counter/reject trade?: (y/c/n)")
        if x=="y" or x=='Y':
            print 'accepted'
            trade1,trade2=trade2,trade1
            c=1
        elif x=='n' or x=='N':
            print 'rejected'
            c=1
        elif x=='c' or x=='C':
            pass
    else:
        print 'wrong input, enter again'
        print

"""
