#finished this!! :D 
import pygame, sys, random,time
from pygame.locals import *
from howtoplay import *
#initialize pygame
pygame.init()
size=(1024,768)
windowSurface = pygame.display.set_mode((size), 0, 32)  
pygame.display.set_caption('Super Mumbo Epicness') #the title of window
Colour2=(182,143,182) #BOX COLOUR
Colour2L=(215,194,215) #BG COLOUR

yes=pygame.image.load('Images/Yes.png')
no=pygame.image.load('Images/No.png')
ok=pygame.image.load('Images/ok.jpg')
background=pygame.image.load('Images/background.png')

SettingFont = pygame.font.SysFont(None, 40)

def Settings():
    templist=['Back to game', 'Restart game', 'Help', 'SFX and Music', 'Exit game']
    tempboxes=[0 for i in range(5)]
    e=size[0]/10.0 + 70
    for word in templist:
        text=basicFont.render(word,True,WHITE)
        box=text.get_rect(center=(size[0]/2,e))
        tempboxes[templist.index(word)]=box
        e+=70
    done=False
    while not done:
        windowSurface.blit(background,background.get_rect())
        pygame.draw.rect(windowSurface,BLACK,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],0.78125*size[1]),5)
        purble=pygame.draw.rect(windowSurface,Colour2,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],0.78125*size[1]))
        for b in range(5):
            w=pygame.draw.rect(windowSurface,Colour2L,(tempboxes[b].left,tempboxes[b].top-5,tempboxes[b].width,tempboxes[b].height+10))
            text=basicFont.render(templist[b],True,WHITE)
            windowSurface.blit(text,tempboxes[b])
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                for b in range(5):                
                        if tempboxes[b].collidepoint(pos):
                            if b==0: #back to game
                                done=True
                                print 'done'
                                return 1
                            if b==1: #restart game                                
                                #pop up asking if you want to restart, start GAME from top
                                restart=pygame.image.load('Images/restart.png')
                                norestart=pygame.image.load('Images/norestart.png')
                                buttons=[restart,norestart]
                                buttonlist=[0,0]
                                exitcheck=0
                                while True:
                                    windowSurface.blit(background,background.get_rect())
                                    pygame.draw.rect(windowSurface,BLACK,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],(0.78125*size[1])/2),5)
                                    purble=pygame.draw.rect(windowSurface,Colour2,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],(0.78125*size[1])/2))
                                    question='Are you sure you want to restart the game?'
                                    questionmark=SettingFont.render(question,True,WHITE)
                                    e=size[0]/10+70
                                    questionbox=questionmark.get_rect(center=(size[0]/2,e))
                                    windowSurface.blit(questionmark,questionbox)
                                    e+=120
                                    fraction=0.34
                                    for i in buttons:
                                        press=i.get_rect(center=(fraction*size[0],e))
                                        buttonlist[buttons.index(i)]=press
                                        windowSurface.blit(i,press)
                                        fraction+=0.32                                        
                                    pygame.display.flip()
                                    for event in pygame.event.get():
                                        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                            pos=event.pos
                                            for i in range(2):
                                                if buttonlist[i].collidepoint(pos):
                                                    if i==0:
                                                        print 'yes'
                                                        return 2
                                                    if i==1:
                                                        print 'no'
                                                        exitcheck=1
                                    if exitcheck==1:
                                        break
                                                    
                            if b==2: #help
                                howtoplay((1024,768))
                                done=True
                                break
                            if b==3: #SFX and Music
                                SFXboxes=[0,0]
                                checkdict={'SFX':yes,'Music':yes}
                                returning=0
                                while True:
                                    windowSurface.blit(background,background.get_rect())
                                    pygame.draw.rect(windowSurface,BLACK,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],(0.78125*size[1])/2),5)
                                    purble=pygame.draw.rect(windowSurface,Colour2,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],(0.78125*size[1])/2))                                    
                                    texts=['SFX Toggle:', 'Background Music:']                                    
                                    e=size[0]/10+70
                                    yesrect=yes.get_rect(center=(6*size[0]/10,e))
                                    norect=no.get_rect(center=(6*size[0]/10,e+100))
                                    for i in texts:
                                        text=SettingFont.render(i,True,WHITE)
                                        box=text.get_rect(center=((size[0]-250)/2,e))
                                        SFXboxes[texts.index(i)]=box
                                        w=pygame.draw.rect(windowSurface,Colour2L,(box.left,box.top-5,box.width,box.height+10))
                                        windowSurface.blit(text,box)                                                                              
                                        e+=100
                                    okbox=ok.get_rect(center=(7.3*size[0]/10,e))
                                    windowSurface.blit(ok,okbox)
                                    windowSurface.blit(checkdict['SFX'],yesrect)
                                    windowSurface.blit(checkdict['Music'],norect)
                                    pygame.display.flip()
                                    for event in pygame.event.get():
                                        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                            pos=event.pos
                                            if yesrect.collidepoint(pos):
                                                print 'SFX toggles'
                                                if checkdict['SFX']==yes:
                                                    checkdict['SFX']=no
                                                else:
                                                    checkdict['SFX']=yes
                                            if norect.collidepoint(pos):
                                                print 'MUSIX toggles'
                                                if checkdict['Music']==yes:
                                                    checkdict['Music']=no
                                                    pygame.mixer.music.pause()
                                                else:
                                                    checkdict['Music']=yes
                                                    pygame.mixer.music.unpause()
                                            if okbox.collidepoint(pos):
                                                print 'going back'
                                                returning=1
                                    if returning==1:
                                        break                                                                                            
                                        
                            if b==4: #exit game
                                #pop up asking if you want to restart #go back to SUPER MUMBO EPICNESS file from the top
                                restart=pygame.image.load('Images/exitmain.png')
                                norestart=pygame.image.load('Images/norestart.png')
                                buttons=[restart,norestart]
                                buttonlist=[0,0]
                                exitcheck=0
                                while True:
                                    windowSurface.blit(background,background.get_rect())
                                    pygame.draw.rect(windowSurface,BLACK,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],(0.78125*size[1])/2),5)
                                    purble=pygame.draw.rect(windowSurface,Colour2,(size[0]/2-((0.78125*size[1])/2), size[0]/10.0, 0.78125*size[1],(0.78125*size[1])/2))
                                    question='Do you want to exit to main menu?'
                                    questionmark=SettingFont.render(question,True,WHITE)
                                    e=size[0]/10+70
                                    questionbox=questionmark.get_rect(center=(size[0]/2,e))
                                    windowSurface.blit(questionmark,questionbox)
                                    e+=120
                                    fraction=0.368
                                    for i in buttons:
                                        press=i.get_rect(center=(fraction*size[0],e))
                                        buttonlist[buttons.index(i)]=press
                                        windowSurface.blit(i,press)
                                        fraction+=0.3                                       
                                    pygame.display.flip()
                                    for event in pygame.event.get():
                                        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                            pos=event.pos
                                            for i in range(2):
                                                if buttonlist[i].collidepoint(pos):
                                                    if i==0:
                                                        print 'yes'
                                                        pygame.mixer.music.stop()
                                                        pygame.time.delay(1500)
                                                        execfile('SUPER MUMBO EPICNESS.py')
                                                    if i==1:
                                                        print 'no'
                                                        exitcheck=1
                                    if exitcheck==1:
                                        break
                                
                            else:
                                pass
            
        pygame.display.flip()

#Settings()
