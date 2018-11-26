import pygame, sys, eztext
from tokenselect import *
from pygame.locals import *

pygame.init()

#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32)
pygame.display.set_caption('Super Mumbo Epicness')
windowSurface.set_alpha(None)

#setup font
basicFont = pygame.font.SysFont(None, 32)

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255,140,0)

#load images
playerinputbg=pygame.image.load('Images/playerinputbg.jpg')
ok=pygame.image.load('Images/ok.jpg')
back=pygame.image.load('Images/back.png')

#error messages
Error=basicFont.render('Enter again, total players on board not more than 4', True, ORANGE)
Message=Error.get_rect(center=(650,100))
Error2=basicFont.render('Enter a number only', True, ORANGE)
Message2=Error2.get_rect(center=(480,100))
Error3=basicFont.render('Enter a positive number', True, ORANGE)
Message3=Error3.get_rect(center=(480,100))
Error4=basicFont.render('Enter again, at least 2 players on board needed', True, ORANGE)
Message4=Error4.get_rect(center=(650,100))

#Prompt for number of CPU players
CPUnumber_prompt=eztext.Input(maxlength=20, color=(255,0,0), prompt='Number of CPU players: ')
CPUnumber_prompt.set_pos(460,200)

def Playerinput(playerno):
    option = 0
    loop=1 #internal loop for text input
    while True:
        if option==0: #If entering number of CPU Players
            backbutton=back.get_rect(center=(420,210))
            okbox=ok.get_rect(center=(920,210))
            if playerno<4: #Run below loop to consider filling CPU players
                pygame_events = pygame.event.get()
                for event in pygame_events:
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                        pos=event.pos
                        if backbutton.collidepoint(pos): #click back button
                            return 0, [], []
                        if okbox.collidepoint(pos): #click ok button
                            try:
                                CPUno=int(CPUnumber_prompt.value)
                                if CPUno<0: #Negative number error
                                    windowSurface.blit(Error3,Message3)
                                    pygame.display.flip()
                                    pygame.time.delay(1000)
                                    CPUnumber_prompt.value=''
                                elif CPUno+playerno<2: #Insufficient players error
                                    windowSurface.blit(Error4,Message4)
                                    pygame.display.flip()
                                    pygame.time.delay(1000)
                                    CPUnumber_prompt.value=''
                                elif CPUno+playerno>4: #Excess players error
                                    windowSurface.blit(Error,Message)
                                    pygame.display.flip()
                                    pygame.time.delay(1000)
                                    CPUnumber_prompt.value=''
                                else: #Set CPU number
                                    CPUnumber_msg = basicFont.render('Number of CPU players: '+str(CPUnumber_prompt.value), True, BLACK)
                                    CPUnumber_msgbox = CPUnumber_msg.get_rect(center=(617,210))
                                    windowSurface.blit(CPUnumber_msg, CPUnumber_msgbox)
                                    TOTAL=CPUno+playerno
                                    option=2
                            except ValueError:
                                if CPUnumber_prompt.value=='':
                                    pass
                                else: #Entered value not a number
                                    windowSurface.blit(Error2,Message2)
                                    pygame.display.flip()
                                    pygame.time.delay(1000)
                                    CPUnumber_prompt.value=''

                windowSurface.blit(pygame.transform.scale(playerinputbg, (960,640)), (0,0))
                windowSurface.blit(ok,okbox)
                windowSurface.blit(back,backbutton)
                CPUnumber_prompt.update(pygame_events)
                CPUnumber_prompt.draw(windowSurface)
                pygame.display.flip()
            else:
                TOTAL=4
                option=2

        if option==2:
            #initializing lists for text input instances and names
            Ptextbox=['null' for i in range(TOTAL)]
            Playername=[0 for i in range(TOTAL)]

            #making input instances for number of players
            for i in range(playerno):
                Ptextbox[i]=eztext.Input(maxlength=20, color=(255,0,0), prompt='Player '+str(i+1)+' name: ')
            option=1

        #variable indicating current player name input
        current_p=0

        #for position of text inputs
        i=250

        #text input loop
        while option==1:
            if current_p<playerno: #players still left to input name
                pygame_events = pygame.event.get()
                for event in pygame_events:
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                        pos=event.pos
                        if okbox.collidepoint(pos): #confirmed player name input
                            loop=2
                        if backbutton.collidepoint(pos): #clicked back button
                            if current_p>0: #to go back to previous player input
                                current_p-=1
                                i-=50
                                continue
                            if current_p==0:
                                if playerno==4:
                                    pos=event.pos
                                    if backbutton.collidepoint(pos): #return to number of players screen since there's no CPU number input
                                        return 0, [], []
                                else: #go back to number of CPU input
                                    option=0
                                    break

                #current player text input
                if loop==1:
                    try:
                        Ptextbox[current_p].set_pos(500,i)
                    except AttributeError:
                        pass
                    windowSurface.blit(pygame.transform.scale(playerinputbg, (960,640)), (0,0)) #draw bg image
                    if playerno<4:
                        windowSurface.blit(CPUnumber_msg, CPUnumber_msgbox) #write set CPU number message
                    j=i-(current_p+1)*50
                    if current_p>=1:
                        q=0
                        while q<current_p: #write set player names from before
                            Playertext=basicFont.render('Player '+str(q+1)+' name: '+str(Ptextbox[q].value), True, BLACK)
                            Playerbox=Playertext.get_rect(center=(616,j+61))
                            windowSurface.blit(Playertext, Playerbox)
                            q+=1
                            j+=50
                    okbox=ok.get_rect(center=(920,j+58))
                    windowSurface.blit(ok,okbox)
                    backbutton=back.get_rect(center=(420,j+58))
                    windowSurface.blit(back,backbutton)
                    Ptextbox[current_p].update(pygame_events)
                    Ptextbox[current_p].draw(windowSurface)
                    pygame.display.flip()

                #player name ok
                if loop==2:
                    Playername[current_p]=Ptextbox[current_p].value #value = entered text
                    loop=1 #go to player name input for next player
                    i+=50
                    current_p+=1
                    pygame.display.flip()

            if current_p==playerno: #Entered for all players
                for event in pygame.event.get():
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                        pos=event.pos
                        if okbox.collidepoint(pos): #ok -> go to token select
                            option=3
                            break
                        if backbutton.collidepoint(pos):
                            current_p-=1
                            i-=50
                            break
                if current_p!=0: #if only one player and clicks back
                    Playertext=basicFont.render('Player '+str(current_p)+' name: '+str(Ptextbox[current_p-1].value), True, BLACK)
                    Advance=basicFont.render('Click OK to continue, or go back and edit', True, BLUE)
                    white=basicFont.render(105*' ', True, WHITE, (254,254,215)) #just to cover up the text input display instead of clearing screen again
                    space=white.get_rect(center=(700,i-37))
                    pygame.draw.rect(windowSurface,(254,254,215), (space.left-5, space.top-15, space.width, space.height+20))
                    okbox=ok.get_rect(center=(920,j+113))
                    windowSurface.blit(ok,okbox)
                    backbutton=back.get_rect(center=(420,j+113))
                    windowSurface.blit(back,backbutton)
                    Advancebox=Advance.get_rect(center=(616,j+200))
                    Playerbox=Playertext.get_rect(center=(616,j+61))
                    windowSurface.blit(Playertext,Playerbox)
                    space=white.get_rect(center=(700,i+102))
                    pygame.draw.rect(windowSurface,(254,254,215), (space.left-5, space.top-15, space.width, space.height+20))
                    windowSurface.blit(Advance,Advancebox)
                    pygame.display.flip()

        if option==3:
            k=1
            for i in range(TOTAL):
                if Ptextbox[i]=='null': #change nulls to CPU names
                    Ptextbox[i]="CPU"+str(k)
                    Playername[i]=Ptextbox[i]
                    k+=1
            tokenselectdone, PLAYERTOKENS, names_and_icons = tokenselect(playerno,Playername)
            if not tokenselectdone:
                option=1
                loop=1
                current_p=playerno
            if tokenselectdone:
                return 1, PLAYERTOKENS, names_and_icons

#playerno=2
#Playerinput(playerno)
