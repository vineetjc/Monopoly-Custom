import pygame, sys, random,time
from pygame.locals import *
pygame.init()
size=(1024,768)
windowSurface = pygame.display.set_mode((size), 0, 32)
pygame.display.set_caption('Super Mumbo Epicness') #the title of window

ManageFont = pygame.font.SysFont(None, 30)
ManageFont2= pygame.font.SysFont(None, 36)


"""
3. Manage - a. Player details- props, cash, SMEpoints, GOOJ (if any)
            b. Build
            c. Mortgage/Unmortgage
            d. Use SME points
"""
Blue=(0,166,216)
BLACK=(0,0,0)
WHITE=(255,255,255)
Colour2=(182,143,182)

Tab1=pygame.image.load("Images/firsttab.png")
Tab2=pygame.image.load("Images/secondtab.png")
Tab3=pygame.image.load("Images/thirdtab.png")
Tab4=pygame.image.load("Images/fourthtab.png")
backarrow=pygame.image.load("Images/back.png")
backbox=backarrow.get_rect(center=(40,37/2))

def Manage(player):
    templist=['Details','Build','(Un)Mortgage','SME']
    CurrentTab=Tab1
    tempboxes=[0 for i in range(4)]
    #e=size[0]/4
    e=size[0]/2-((0.78125*size[1])/2.094)
    e+=e/4
    f=size[0]/10.0
    f+=f/4
    text=ManageFont.render(templist[0],True,WHITE)
    box=text.get_rect(center=(e,f))
    tempboxes[0]=box
    e+=152
    text=ManageFont.render(templist[1],True,WHITE)
    box=text.get_rect(center=(e,f))
    tempboxes[1]=box
    e+=155
    text=ManageFont.render(templist[2],True,WHITE)
    box=text.get_rect(center=(e,f))
    tempboxes[2]=box
    e+=155
    text=ManageFont.render(templist[3],True,WHITE)
    box=text.get_rect(center=(e,f))
    tempboxes[3]=box
    done=False
    value=0 #initialize variable
    def texting():
        e=size[0]/2-((0.78125*size[1])/2.094)
        e+=e/4
        e=12*e/10
        f=size[0]/10.0
        f+=f/4
        f=17*f/10
        string=ManageFont.render('Player Name:',True,WHITE)
        stringbox=string.get_rect(center=(e,105*f/100))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render(player.Name,True,WHITE)
        stringbox=string.get_rect(center=(15*e/10,105*f/100))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render('Net worth:',True,WHITE)
        stringbox=string.get_rect(center=(e,13*f/10))
        windowSurface.blit(string,stringbox)
        networth=player.Cash
        for prop in player.Owned:
            networth+=prop.Price
        string=ManageFont.render(str(networth),True,WHITE) #get the same from the GAME.py
        stringbox=string.get_rect(center=(15*e/10,13*f/10))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render('Cash:',True,WHITE)
        stringbox=string.get_rect(center=(e,155*f/100))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render(str(player.Cash),True,WHITE)
        stringbox=string.get_rect(center=(15*e/10,155*f/100))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render('SME points:',True,WHITE)
        stringbox=string.get_rect(center=(e,18*f/10))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render(str(player.SME),True,WHITE)
        stringbox=string.get_rect(center=(15*e/10,18*f/10))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render('Get out of Jail card(s):',True,WHITE)
        stringbox=string.get_rect(center=(e,205*f/100))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render(str(player.GOOJ),True,WHITE)
        stringbox=string.get_rect(center=(15*e/10,205*f/100))
        windowSurface.blit(string,stringbox)
        string=ManageFont.render('Properties:',True,WHITE)
        stringbox=string.get_rect(center=(e,23*f/10))
        windowSurface.blit(string,stringbox)
    while not done:
        windowSurface.fill((150,200,255))
        windowSurface.blit(backarrow,backbox)
        pygame.draw.rect(windowSurface,BLACK,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],0.78125*size[1]),5)
        purble=pygame.draw.rect(windowSurface,Colour2,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],0.78125*size[1]))
        windowSurface.blit(pygame.transform.scale(CurrentTab, (int(0.78125*size[1]),int(1.948051948051948*41))), (size[0]/2-((0.78125*size[1])/2), size[0]/10.0))
        for b in range(4):
            if b==value:
                text=ManageFont2.render(templist[b],True,WHITE)
                tempboxes[b].centerx-=5
            else:
                text=ManageFont.render(templist[b],True,WHITE)
            #w=pygame.draw.rect(windowSurface,(255,0,0),(tempboxes[b].left,tempboxes[b].top-5,tempboxes[b].width,tempboxes[b].height+10))

            windowSurface.blit(text,tempboxes[b])
        tempboxes[value].centerx+=5
        texting()
        for event in pygame.event.get(): #using new definitions for function to over write
            if event.type == pygame.MOUSEMOTION:
                x,y = event.pos
                if backbox.collidepoint(x,y):
                    dptext=ManageFont.render('Back to game',True,BLACK)
                    dptextbox=dptext.get_rect(center=(150,37/2))
                    windowSurface.blit(dptext,dptextbox)
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                if backbox.collidepoint(pos):
                    return
                for b in range(4):
                        if tempboxes[b].collidepoint(pos):
                            print 'hi',b
                            if b==0:
                                CurrentTab=Tab1
                                def texting():
                                    e=size[0]/2-((0.78125*size[1])/2.094)
                                    e+=e/4
                                    e=12*e/10
                                    f=size[0]/10.0
                                    f+=f/4
                                    f=17*f/10
                                    string=ManageFont.render('Player Name:',True,WHITE)
                                    stringbox=string.get_rect(center=(e,105*f/100))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render(player.Name,True,WHITE)
                                    stringbox=string.get_rect(center=(15*e/10,105*f/100))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render('Net worth:',True,WHITE)
                                    stringbox=string.get_rect(center=(e,13*f/10))
                                    windowSurface.blit(string,stringbox)
                                    networth=player.Cash
                                    for prop in player.Owned:
                                        networth+=prop.Price
                                    string=ManageFont.render(str(networth),True,WHITE) #get the same from the GAME.py
                                    stringbox=string.get_rect(center=(15*e/10,13*f/10))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render('Cash:',True,WHITE)
                                    stringbox=string.get_rect(center=(e,155*f/100))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render(str(player.Cash),True,WHITE)
                                    stringbox=string.get_rect(center=(15*e/10,155*f/100))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render('SME points:',True,WHITE)
                                    stringbox=string.get_rect(center=(e,18*f/10))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render(str(player.SME),True,WHITE)
                                    stringbox=string.get_rect(center=(15*e/10,18*f/10))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render('Get out of Jail card(s):',True,WHITE)
                                    stringbox=string.get_rect(center=(e,205*f/100))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render(str(player.GOOJ),True,WHITE)
                                    stringbox=string.get_rect(center=(15*e/10,205*f/100))
                                    windowSurface.blit(string,stringbox)
                                    string=ManageFont.render('Properties:',True,WHITE)
                                    stringbox=string.get_rect(center=(e,23*f/10))
                                    windowSurface.blit(string,stringbox)
                                value=0
                            elif b==1:
                                CurrentTab=Tab2
                                def texting():
                                    string=ManageFont.render('Page 2',True,WHITE)
                                    stringbox=string.get_rect(center=(500,500))
                                    windowSurface.blit(string,stringbox)
                                value=1
                            elif b==2:
                                CurrentTab=Tab3
                                def texting():
                                    string=ManageFont.render('Hi Page 3',True,WHITE)
                                    stringbox=string.get_rect(center=(500,500))
                                    windowSurface.blit(string,stringbox)
                                value=2
                            elif b==3:
                                CurrentTab=Tab4
                                def texting():
                                    string=ManageFont.render('Hi page 4',True,WHITE)
                                    stringbox=string.get_rect(center=(500,500))
                                    windowSurface.blit(string,stringbox)
                                value=3
                            else:
                                pass


        pygame.display.flip()

#Manage()
