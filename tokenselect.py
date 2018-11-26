import pygame, sys, random,time, eztext
from pygame.locals import *

pygame.init()

#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32)
pygame.display.set_caption('Super Mumbo Epicness') #the title of window

#setup font
basicFont = pygame.font.SysFont(None, 48)

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148,0,221)
YELLOW=(255,215,0)

#Token images
Car=pygame.image.load('Images//Tokens/Car.jpeg')
Dog=pygame.image.load('Images//Tokens/Dog.jpeg')
Thimble=pygame.image.load('Images//Tokens/Thimble.jpeg')
Trolley=pygame.image.load('Images//Tokens/Trolley.jpeg')
Ship=pygame.image.load('Images//Tokens/Ship.jpeg')
Iron=pygame.image.load('Images//Tokens/Iron.jpeg')
Hat=pygame.image.load('Images//Tokens/Hat.jpeg')
Shoe=pygame.image.load('Images//Tokens/Shoe.jpeg')

#Other image assets
back=pygame.image.load('Images/back.png')
backbox=back.get_rect(center=(40,18.5))
ok=pygame.image.load('Images/ok.jpg')
okbox=ok.get_rect(center=(920,640-18.5))
BG=pygame.image.load('Images/tokenselectbg.jpg')

tokenlist=[Car, Dog, Thimble, Trolley, Ship, Iron, Hat, Shoe]

def tokenselect(playerno,Playernames):
    PLAYERTOKENS=[]
    names_and_icons=[0 for i in range(4)] #names_and_icons which contains tuples of name and image

    #list to store rects for all 8 token images / integer corresponding to player number in place if player selected token
    rectangles=['null' for i in range(8)]

    idx=1
    q=0
    while 0<idx<=playerno+1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                pos=event.pos
                if backbox.collidepoint(pos):
                    if idx>0:
                        idx-=1
                        if idx==0: #goes back to playersinput
                            return 0, [], []
                            break
                        q-=1
                        for l in rectangles:
                            if l==idx:
                                rectangles[rectangles.index(l)]='changed' #temporarily replace the integer till rect is assigned for drawing black/white rectangles later
                        break
                if idx>playerno:
                    if okbox.collidepoint(pos):
                        v=1
                        while v<=playerno:
                            for i in range(8):
                                if type(rectangles[i])==int: #i.e. token is chosen by that player
                                    if rectangles[i]==v: #v-th player has chosen that token
                                        PLAYERTOKENS.append(tokenlist[i])
                                        v+=1
                        idx = playerno + 2

                if idx<=playerno:
                    for rec in rectangles:
                        if type(rec)!=int: #i.e. 'clickable rect'
                            if rec.collidepoint(pos):
                                names_and_icons[q]=(Playernames[idx-1], rec)
                                idx+=1
                                q+=1
                                rectangles[rectangles.index(rec)]=idx-1 #change rectangle type to current player number
                                break

            j=130
            k=0
            windowSurface.blit(pygame.transform.scale(BG, (960,640)), (0,0))
            for e in range(8):
                if e<4:
                    k=240
                if e==4:
                    j=130
                if e>=4:
                    k=400
                buttonclick=tokenlist[e].get_rect(center=(j,k))

                if type(rectangles[e])==int: #is an already selected rect, colour it black
                    pygame.draw.rect(windowSurface, BLACK, (buttonclick.left, buttonclick.top, buttonclick.width, buttonclick.height))
                else: #is not selected yet, make rect
                    rectangles[e]=buttonclick
                    pygame.draw.rect(windowSurface, WHITE, (buttonclick.left, buttonclick.top, buttonclick.width, buttonclick.height))
                windowSurface.blit(tokenlist[e],buttonclick)
                j+=240

            if idx>playerno:
                finish=basicFont.render('Click OK to proceed to game!', True, VIOLET)
                finishbox=finish.get_rect(center=(500,600))
                windowSurface.blit(finish,finishbox)
                windowSurface.blit(ok,okbox)
            else:
                prompts = basicFont.render('Player '+str(idx)+" "+Playernames[q]+' choose your token', True, VIOLET)
                box=prompts.get_rect(center=(500,600))
                windowSurface.blit(prompts,box)
            windowSurface.blit(back,backbox)
            pygame.display.flip()
        pygame.display.flip()

    if len(Playernames)>playerno: #Assigning random CPU tokens
        diff=len(Playernames)-playerno
        for i in range(diff):
            R=random.randint(0,7)
            while tokenlist[R] in PLAYERTOKENS:
                R=random.randint(0,7)
            PLAYERTOKENS.append(tokenlist[R])
    return 1, PLAYERTOKENS, names_and_icons
