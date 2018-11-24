import random, pygame
from Properties import *
from battleshipthingy import *
size=(1024,768)
pygame.init()
basicFont = pygame.font.SysFont(None, 48)
BLACK = (0, 0, 0)

position=(size[0]-size[1])/2 + size[1]-70
positionx = (size[0]-size[1])/2 + (0.904947916667*size[1])
positiony=size[1]-(0.065104166667*size[1])

sixtythree=0.08203125*size[1] #because in 1024x768, the step value for token is 63

#idea : use {'position number: coordinates'}!!!! 1 is GO
posdict={1:(positionx,positiony),2:(positionx-sixtythree,positiony),3:(positionx-2*sixtythree,positiony),4:(positionx-3*sixtythree,positiony),5:(positionx-4*sixtythree,positiony),6:(positionx-5*sixtythree,positiony),7:(positionx-6*sixtythree,positiony),8:(positionx-7*sixtythree,positiony),9:(positionx-8*sixtythree,positiony),10:(positionx-9*sixtythree,positiony),11:(positionx-10*sixtythree,positiony+sixtythree/3),'Jail':(positionx-10*sixtythree,positiony-sixtythree/3),12:(positionx-11*sixtythree+(sixtythree/2),positiony-2*sixtythree+(sixtythree/2))}
posdict[13]=(posdict[12][0],posdict[12][1]-sixtythree)
for i in range(14,22):
    posdict[i]=(posdict[i-1][0],posdict[i-1][1]-sixtythree)
posdict[22]=(posdict[21][0]+2*sixtythree-(sixtythree/2),posdict[21][1])
for i in range(23,31):
    posdict[i]=(posdict[i-1][0]+sixtythree,posdict[i-1][1])
posdict[31]=(posdict[30][0]+2*sixtythree-(sixtythree/2),posdict[30][1])
for i in range(32,41):
    posdict[i]=(posdict[i-1][0],posdict[i-1][1]+sixtythree)

#this is the property card with position dictionary
poscard={}
for i in Properties:
    card=pygame.image.load('Images//The Cards/Property Cards/'+i.Name+'.png')
    poscard[i.Position]=card

buy=pygame.image.load('Images/buy icon.png')
auction=pygame.image.load('Images/auction icon.png')

boardimg=pygame.image.load('Images/boardimg.jpg')
def BoardDisplay(windowSurface):
    windowSurface.blit(pygame.transform.scale(boardimg,(size[1],size[1])),((size[0]-size[1])/2,0))

#maybe changes are required for class definitions

#chance random list
Chances=[]
while len(Chances)<16:
    number=random.randint(0,15)
    if number not in Chances:
        Chances.append(number)

#Comm.Chest list
Chest=[]
while len(Chest)<16:
    number=random.randint(0,15)
    if number not in Chest:
        Chest.append(number)

#GOOJ cards limit counter
GOOJchance=1 #because one in chest, one in chance
GOOJchest=1


class Player:
    def __init__(self,Name,Peg): #position number with reference to board, and Go is marked 1
        self.Name=Name
        self.Peg=Peg #this is going to be the peg's image associated with it
        self.Cash=1500
        self.Owned=[]
        self.Mortgaged=[] #mortgaging and unmortgaging means transferring from these two lists
        self.SME=0
        self.GOOJ=0 #Get Out Of Jail
        self.Position=1 #initially, it changes with time
        self.Turns=0 #just for referring to number of turns played, for zero turns no Go money.
        self.Doublecount=0


    def PlayerSpaces(self,windowSurface):  #will only work after completion, variables adjusted
        box=self.Peg.get_rect(center=posdict[self.Position])
        windowSurface.blit(self.Peg,box)



    def Move(self,dicenumbers,Players,windowSurface):
        if self.Doublecount<3:
            #this is for dice roll, two variables give dice effect
            a=random.randint(1,6)
            b=random.randint(1,6)
#dice icons
            diceA=dicenumbers[a-1]
            diceB=dicenumbers[b-1]
            Abox=diceA.get_rect(center=(posdict[13][0]+2*sixtythree,posdict[13][1]))
            Bbox=diceB.get_rect(center=(posdict[13][0]+7*sixtythree/2,posdict[13][1]))
            if a==b:
                self.Doublecount+=1
            Roll=a+b
            if self.Doublecount==3:
                print 'self.Jail()'
            else: #visual of token movement
                q=self.Position
                p=1
                while p<=Roll:
                    if q==40:
                        q=0
                        self.Cash+=200
                    o=q
                    self.Position=o+1
                    BoardDisplay(windowSurface)
                    for person in Players:
                        person.PlayerSpaces(windowSurface)
                    windowSurface.blit(diceA,Abox)
                    windowSurface.blit(diceB,Bbox)
                    self.PlayerSpaces(windowSurface)
                    pygame.display.flip()
                    pygame.time.delay(300)
                    q+=1
                    p+=1 #end of token visual
                #action decide
                if self.Position in [6,16,26,36]:
                    self.Teleportland(Players,windowSurface)
                    #break
                if self.Position in [13,29]:
                    self.SMEland()
                    #break
                if self.Position in [8,23,37]:
                    self.Chance(Players,windowSurface)
                    #break
                if self.Position in [3,18,34]:
                    self.Communitychest(Players,windowSurface)
                    #break
                if self.Position in [5,39]:
                    self.Tax()
                    #break
                if self.Position in [1,11]:
                    pass
                if self.Position==31:
                    print 'self.Jail()'
                    #break
                if self.Position==21:
                    self.FreeParking()
                    #break
                else:
                    self.Propertyland(Players)
                    #break
        if a==b:
            pygame.time.delay(1500)
            print 'rolling again...'
            pygame.time.delay(100)
            self.Move(dicenumbers,Players,windowSurface)

    def Propertyland(self,Players):
        for i in Properties:
            if self.Position==i.Position:
                print 'owner:',i.Owner
                if i.Owner!=None:
                    print i.Owner
                    ownedby=i.Owner
                    print ownedby, 'is the owner'
                    """for person in Players:
                        if person.Name==ownedby:
                            presentcash=int(person.Cash)"""
                    payment=i.Rent(Players)
                    print payment, 'is the rent'
                    print self.Cash
                    self.Cash-=payment
                    print self.Cash
                else:
                    windowSurface.blit(poscard[i.Position],poscard[i.Position].get_rect(center=(size[0]/2,size[1]/2)))
                    #Purple 145,90,243 Red 229,44,58 Orange 255,114,36 Yellow 244,184,6 Green 76,175,80 LBlue 0,187,211 DBlue 56,79,146 Pink 239,67,138
                    if i.Position in [j.Position for j in Purple]:
                        boxcolour=(145,90,243)
                    elif i.Position in [j.Position for j in LightBlue]:
                        boxcolour=(0,187,211)
                    elif i.Position in [j.Position for j in Red]:
                        boxcolour=(229,44,58)
                    elif i.Position in [j.Position for j in Orange]:
                        boxcolour=(255,114,36)
                    elif i.Position in [j.Position for j in Yellow]:
                        boxcolour=(244,184,4)
                    elif i.Position in [j.Position for j in Green]:
                        boxcolour=(76,175,80)
                    elif i.Position in [j.Position for j in DarkBlue]:
                        boxcolour=(56,79,146)
                    elif i.Position in [j.Position for j in Pink]:
                        boxcolour=(239,67,138)
                    pygame.draw.rect(windowSurface, boxcolour, (size[0]/2-139,size[1]/2 + 178,280,42))
                    buyrect=buy.get_rect(center=(size[0]/2-50, size[1]/2+200))
                    windowSurface.blit(buy,buyrect)
                    auctionrect=auction.get_rect(center=(size[0]/2+50, size[1]/2+200))
                    windowSurface.blit(auction,auctionrect)
                    pygame.display.flip()
                    done=False
                    while not done:
                        for event in pygame.event.get():
                            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                                pos=event.pos
                                if buyrect.collidepoint(pos):
                                    #if ask=='buy':
                                    i.Buy()
                                    self.Cash-=i.Price
                                    self.Owned.append(i)
                                    i.Owner=self.Name
                                elif auctionrect.collidepoint(pos):
                                    #if ask=='auction':
                                    i.Auction(Players)
                                done=True
                                break

                    """ask=raw_input('buy/auction??:')
                    if ask=='buy':
                        i.Buy()
                        self.Cash-=i.Price
                        self.Owned.append(i)
                        i.Owner=self.Name
                    if ask=='auction':
                        i.Auction(Players)"""




    def SMEland(self):
        print 'Visual display You have collected one SME point'
        self.SME+=1

    def Chance(self,Players,windowSurface):
        arrowL=pygame.image.load('Images/arrow.png')
        arrowLbox=arrowL.get_rect(center=(500,230))
        basicFont = pygame.font.SysFont(None, 32)
        text=basicFont.render('Pick a chance card',True,BLACK)
        box=text.get_rect(center=(650,230))
        done=False
        while not done:
            windowSurface.blit(arrowL,arrowLbox)
            windowSurface.blit(text,box)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    x,y=event.pos
                    if 278<=x<=430 and 160<=y<=311:
                        done=True
        BoardDisplay(windowSurface)
        pygame.display.flip()
        global GOOJchance #counter of number of GOOJ cards
        global Chances
        heavy=Chances[0]
        if heavy==0:
            print 'Visual Advance To Go'
            self.Cash+=200
            self.Position=1
            BoardDisplay(windowSurface)
            card=pygame.image.load('Images//The Cards/Chance/Advance to Go.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
        if heavy==1:#Lanercost
            print 'Advance to Lanercost'
            if self.Position==37:
                self.Cash+=200              #Advances through Go
            self.Position=25
            card=pygame.image.load('Images//The Cards/Chance/Lanercost.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #self.Propertyland(Players)

        if heavy==2: #Roselake
            print 'Advance to Roselake'
            if self.Position==37 or self.Position==23:
                self.Cash+=200
            self.Position=12
            card=pygame.image.load('Images//The Cards/Chance/Roselake.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #self.Propertyland(Players)

        if heavy==3:  #Next Star Space
            print 'Visual Go to SME point'
            if self.Position==8:
                self.Position=13
            if self.Position==23:
                self.Position=29
            if self.Position==37:
                self.Position=13
            card=pygame.image.load('Images//The Cards/Chance/Advance to Next Star Space.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            self.SMEland()
        if heavy==4:  #Next Teleport
            print 'Visual Choose your next destination to Telelport'
            if self.Position==8:
                self.Position=16
            if self.Position==23:
                self.Position=26
            if self.Position==37:
                self.Position=6
            card=pygame.image.load('Images//The Cards/Chance/Advance to nearest Teleport.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            self.Teleportland(Players,windowSurface)
        if heavy==5:   # Get out of jail Card
            if GOOJchance>0:
                self.GOOJ+=1
                print 'Visual You have got one Get out of Jail Card'
                print 'GOOJ card can be traded or used when in trouble!'
                card=pygame.image.load('Images//The Cards/Chance/Get out of Jail Card.png')
                cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
                windowSurface.blit(card,cardbox)
                pygame.display.flip()
                pygame.time.delay(3000)
                GOOJchance-=1
            else:
                self.Chance(Players,windowSurface)
        if heavy==6:
            print 'Visual Go back three Spaces!'
            self.Position-=3
            card=pygame.image.load('Images//The Cards/Chance/Go Back Three Spaces.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #break
        if heavy==7:
            print 'Visual Go to Jail. Do not collect money from Go!'
            card=pygame.image.load('Images//The Cards/Chance/Go Directly to Jail.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            self.Position='Jail'
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #self.Jail()
            #break
        if heavy==8:
            print 'Visual General repairs on all your property. Each house =25$   Each Hotel =100$'
            card=pygame.image.load('Images//The Cards/Chance/General Repairs.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            housecount=0
            hotelcount=0
            for prop in self.Owned:
                if prop not in self.Mortgaged:
                    if prop.Houses==5:
                        hotelcount+=1
                    else:
                        housecount+=prop.Houses
            self.Cash-=(25*housecount + 100*hotelcount)

            #Houses and Hotel                                                                                                                               #Houses and Hotel Variables
        if heavy==9:
            print 'Visual Pay Poor tax!'
            card=pygame.image.load('Images//The Cards/Chance/Poor Tax.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            self.Cash-=15
            FreeParking.Loot+=15
            #break
        if heavy==10:
            print 'Visual You inherit $100 from the bank!'
            card=pygame.image.load('Images//The Cards/Chance/Inherit $100 from the Bank.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            self.Cash+=100
            #break
        if heavy==11: #Hartlepool
            print 'Advance to Hartlepool'
            self.Position=40
            card=pygame.image.load('Images//The Cards/Chance/Advance to Hartlepool.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #self.Propertyland(Players)
            #break
        if heavy==12:
            print 'Visual you have been elected as Chairman of the Board;ive 50$ each to all players'         #Variable for number of players
            card=pygame.image.load('Images//The Cards/Chance/Chairman of the Board!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash-=(len(Players)-1)*50
            for i in Players:
                if i!=self:
                    i.Cash+=50
            #break
        if heavy==13:
            print 'Visual Your building Loan Matures!! Collect $150'
            card=pygame.image.load('Images//The Cards/Chance/Building loan matures.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash+=150
            #break
        if heavy==15:
            print 'Visual NEW ACHIEVEMENT!! BONUS GAME UNLOCKED!!!!!!!'
            card=pygame.image.load('Images//The Cards/Chance/Bonus Game Unlocked.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            windowSurface.fill((0,0,0))
            #insert intro screen and instructions
            R=random.randint(1,2)
            if R==1:
                #coin fall game
                execfile('coinfallthingy.py')
                result=0
                print result, 'before'
                #Play()
                print 'points earned=', A.Points

            if R==2:
                #SEARCH! game
                paisa=SEARCH(otherturn,otherversion)
                self.Cash+=paisa


            #break
        if heavy==14:
            print 'Visual Scratch Lottery Card'
            #break
            #Bonus Game
        Chances.pop(0)
        if heavy!=5:
            Chances.append(heavy)



    def Communitychest(self,Players,windowSurface):
        arrowL=pygame.image.load('Images/arrow.png')
        arrowR=pygame.transform.rotate(arrowL,180)
        arrowRbox=arrowR.get_rect(center=(520,560))
        basicFont = pygame.font.SysFont(None, 32)
        text=basicFont.render('Pick a community chest card',True,BLACK)
        box=text.get_rect(center=(405,495))
        done=False
        while not done:
            windowSurface.blit(arrowR,arrowRbox)
            windowSurface.blit(text,box)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    x,y=event.pos
                    if 595<=x<=750 and 470<=y<=620:
                        done=True
        BoardDisplay(windowSurface)
        pygame.display.flip()
        global Chest
        global GOOJchest
        heavy=Chest[0]
        if heavy==0:
            print 'Visual Advance To Go'
            self.Cash+=200
            self.Position=1
            BoardDisplay(windowSurface)
            card=pygame.image.load('Images//The Cards/Community Chest/Advance to Go!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
        if heavy==1:
            print 'Visual Bank Error in your favor. Collect 200$'
            card=pygame.image.load('Images//The Cards/Community Chest/Bank Error in your Favor.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash+=200
            #break
        if heavy==2:
            print 'Visual Sale of Stock, you get 50$'
            card=pygame.image.load('Images//The Cards/Community Chest/Sold your Stock!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash+=50
            #break
        if heavy==3:
            if GOOJchest>0:
                self.GOOJ+=1
                print 'Visual You have got one Get out of Jail Card'
                print 'GOOJ card can be traded or used when in trouble!'
                card=pygame.image.load('Images//The Cards/Community Chest/Get out of Jail Card.png')
                cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
                windowSurface.blit(card,cardbox)
                pygame.display.flip()
                pygame.time.delay(3000)
                GOOJchest-=1
            else:
                self.Communitychest(Players,windowSurface)
            #break

        if heavy==4:
            print 'Visual You have been JAILED!'
            card=pygame.image.load('Images//The Cards/Community Chest/Go Directly to Jail.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            self.Position='Jail'
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #self.Jail()
            #break

        if heavy==5:
            print 'Visual Grand Opening Night; Collect 50$ from every player for opening seats!'                    #No of players variable
            card=pygame.image.load('Images//The Cards/Community Chest/Grand opening of Opera.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            self.Cash+=(len(Players)-1)*50
            for i in Players:
                if i!=self:
                    i.Cash-=50
            BoardDisplay(windowSurface)
            #break


        if heavy==6:
            print 'Visual Your Holiday Xmas  Fund matures! Collect $100'
            card=pygame.image.load('Images//The Cards/Community Chest/Your Holiday Fund Matures!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash+=100
            #break
        if heavy==7:
            print 'Visual Income Tax Refund! Collect 20$'
            self.Cash+=20
            card=pygame.image.load('Images//The Cards/Community Chest/Income Tax Refund.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            #break
        if heavy==8:
            print 'Its your Birthday!!! Collect 10$ from each player'     #No of players variable
            card=pygame.image.load('Images//The Cards/Community Chest/Its your Birthday!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash+=(len(Players)-1)*10
            for i in Players:
                if i!=self:
                    i.Cash-=10
            #break

        if heavy==9:
            print 'Visual Your Insurance Matures! Collect 100$'
            card=pygame.image.load('Images//The Cards/Community Chest/Life Insurance Matures!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash+=100
            #break
        if heavy==10:
            print 'Visual Pay school Fees of 150$!'
            card=pygame.image.load('Images//The Cards/Community Chest/School Fee Tax!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash-=150
            FreeParking.Loot+=150
            #break
        if heavy==11:
            print 'Visual Pay 20$ Hospital Fee!'
            card=pygame.image.load('Images//The Cards/Community Chest/Pay $20 as Hospital Fees!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            self.Cash-=20
            #break
        if heavy==12:
            print 'Visual you are asessed for street repairs! 40$ per house ,115$ per hotel   '                #Houses and Hotel Variables
            card=pygame.image.load('Images//The Cards/Community Chest/Assessed For Street Repairs!.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            housecount=0
            hotelcount=0
            for prop in self.Owned:
                if prop not in self.Mortgaged:
                    if prop.Houses==5:
                        hotelcount+=1
                    else:
                        housecount+=prop.Houses
            self.Cash-=(40*housecount + 115*hotelcount)

            #self.Cash-=(40*noofhouses)+(115*noofhotel)
            #break
        if heavy==13:
            print 'You have won 2nd prize in a Beauty Contest! Collect 10$'
            self.Cash+=10
            card=pygame.image.load('Images//The Cards/Community Chest/2nd Prize in Beauty Contest.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            BoardDisplay(windowSurface)
            #break
        if heavy==15:
            print'Visual NEW ACHIEVEMENT!! BONUS GAME UNLOCKED!!!!!!!'
            card=pygame.image.load('Images//The Cards/Community Chest/Bonus Game Unlocked.png')
            cardbox=card.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(card,cardbox)
            pygame.display.flip()
            pygame.time.delay(3000)
            windowSurface.fill((0,0,0))
            #insert intro screen and instructions
            R=random.randint(1,2)
            if R==1:
                #coin fall game
                execfile('coinfallthingy.py')
                result=0
                print result, 'before'
                #Play()
                print 'points earned=', A.Points

            if R==2:
                #SEARCH! game
                paisa=SEARCH(otherturn,otherversion)
                self.Cash+=paisa

            #break
        if heavy==14:
            print 'Visual Scratch Lottery Card'
            #break

        Chest.pop(0)
        if heavy!=3:
            Chest.append(heavy)



    def Tax(self):
        if self.Position==5:
            self.Cash-=200               #200 is income tax
            print 'Visual Income Tax'
            #break
        else:
            self.Cash-=100
            FreeParking.Loot+=100
            print 'Visual Money goes to Free Parking'


    def FreeParking(self):
        self.Cash+=FreeParking.Loot
        print 'you got:',FreeParking.Loot,'!'
        FreeParking.Loot=0

    def Teleportland(self,Players,windowSurface): #insert visuals
        arrowL=pygame.image.load('Images/arrow.png') #left side
        arrowLbox=arrowL.get_rect(center=(posdict[16][0]+2*sixtythree,posdict[16][1]))
        arrowU=pygame.transform.rotate(arrowL,270)
        arrowUbox=arrowU.get_rect(center=(posdict[26][0],posdict[26][1]+3*sixtythree/2))
        arrowR=pygame.transform.rotate(arrowU,270)
        arrowRbox=arrowR.get_rect(center=(posdict[36][0]-2*sixtythree,posdict[36][1]))
        arrowD=pygame.transform.rotate(arrowR,270)
        arrowDbox=arrowD.get_rect(center=(posdict[6][0],posdict[6][1]-3*sixtythree/2))
        exitcheck=0
        while True:
            windowSurface.blit(arrowL,arrowLbox)
            windowSurface.blit(arrowU,arrowUbox)
            windowSurface.blit(arrowR,arrowRbox)
            windowSurface.blit(arrowD,arrowDbox)
            text=basicFont.render('Click arrow to',True,BLACK)
            box=text.get_rect(center=(size[0]/2,45*size[1]/100))
            windowSurface.blit(text,box)
            text=basicFont.render('choose your stop',True,BLACK)
            box=text.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(text,box)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    pos=event.pos
                    print 'clicked arrow'
                    arrowboxes=[arrowLbox,arrowUbox,arrowDbox,arrowRbox]
                    for i in range(4):
                        if arrowboxes[i].collidepoint(pos):
                            if i==0:
                                self.Position=16
                            elif i==1:
                                self.Position=26
                            elif i==2:
                                self.Position=6
                            elif i==3:
                                self.Position=36
                            done=False
                            BoardDisplay(windowSurface)
                            for person in Players:
                                person.PlayerSpaces(windowSurface)
                                pygame.display.flip()
                            exitcheck=1
            if exitcheck==1:
                break



#notes and waste about Propertyland and TeleportLand
"""
for i in Properties.Properties:
if self.Position==i.Position:
if unowned:
ask to buy-
i.Buy()
i.Owner=self.Name
self.Cash-=i.Price


or auction-
i.Auction()
break #at the end of it
else:
if unmortgaged and not owned by you:
pay rent - call i.Rent()
break #at the end of it '''


def Teleportland(self):
img=pygame.image.load('Temp/Cursor.gif')
'''VISUAL loop on teleporting locations'''
fps=30
imgx=10    #Coordinates of all four plots on the board
imgy=10    #Coordinates of all four plots on the board
pixmove=4
fpstime=pygame.time.Clock()
while true:
if movement =='down':
imgy+=pixmove
if imgy>8:
movement == 'up'

setDisplay.blit(img,(imgx,imgy))
'''Visual Single click on place to teleport'''
#Incomplete

ask click input from user on self.Position
change on click, it will be either of these [6,16,26,36]
"""

#SME manage mode
"""
        if self.SME==3:                  #Praveena
            '''Visual display Option to increase rent by 5%'''
            '''If Mousebutton.down on yes'''
            self.SME-=3
            '''If Entered Mousebutton.Down on No'''
            break
        '''Visual to convert SME points into money'''
        '''If yes'''
         self.Cash+=(200*self.SME)

        show display message on how many collected
        '''VISUAL Show how many SME points collected at right side'''

"""

#Jail function needs to be worked on!!
"""
    def Jail(self):
        a=1
        b=2
        count=3
        '''Visual UNLUCKY...  YOU ARE JAILED'''
        if self.GOOJ==1:
            '''Visual to choose Option to play randomly generated game'''
                    iv)Pay 20$ play a randomly generated mini-game.
                    for 1st turn, 20$    ,count-=1
                    for 2nd turn, 30$    ,count-=1
                    for 3rd turn, 40$    ,count-=1
            '''Visual Do you want to spend your GOOJ card'''
            '''If yes'''
            if count==0:
                '''Show visual play 50 to get out''' # no other options
            self.GOOJ-=1
            break
        '''Visual Continue Roll?'''
        a=random.randint(1,6)
        b=random.randint(1,6)
        if a==b:
            '''Visual Double, You are a free man!'''
            roll=a+b
            for i in range(roll):
                self.position+=1

        moving not allowed. other actions are allowed so trading jail card is within the option

        ii) roll doubles and break out
            if doubles come, immediately move that many turns, and stop.
            if all turns finish go to option (i)

"""
