import random,pygame
from Properties import *
from Players import *

'''
size=(1024,768)

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
GOOJchest=1'''


class AI:
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
        
    def Propertyland(self,Players): #need to set conditions for buying/auctioning
        '''def Propertyland(self):
            to buy property when
            (check)i) AI has lot of money,
            (check)ii) having same colour already,
            (check)iii) corner grouping - light blue with pink, orange and red, yellow and green, dark blue and purple (don't give much preference to the 2 group property),
            (check)iv) whole side grouping - purple and light blue, pink and orange, red and yellow, green and dark blue
            v) same colour not owned by any body, first check group property (prefer least ownersip on one group), then check single property

            else auction, if owned, pay rent'''
        positives=0 #either an advantage or an interest
        negatives=0 #either a disadvantage or disinterest
        adjcheck=False #to check adjacent colour condition only once
        colourcheck=False #checking condition v)

#CHECK ALL CONDITIONS THROUGH ONCE AGAIN!!
        
        for i in Properties:
            if self.Position==i.Position:
                if i.Owner==None:                    
                    if self.Cash>i.Price: #condition i)
                        positives+=1
                    else:
                        negatives+=2 #more weight to the fact that there's no cash
                        
                    for prop in self.Owned:
                        index=ColoursList.index(i.Colour)
                        if index==len(ColoursList)-1:
                            index=-1
                        if adjcheck==False:
                            if prop.Colour in [ColoursList[index-1], ColoursList[index+1]]: #conditions iv) and iii) checks only once
                                positives+=1
                                adjcheck=True

                        if prop.Colour==i.Colour: #condition ii)
                            positives+=1
                            break
                    

                    #CHECK THIS PART!!!!!! 
                    if colourcheck=False: #for condition v)
                        for Group in ColourProps:
                            if i in Group:
                                for Place in Group:
                                    if Place.Owner!=None:
                                        if Place.Owner==self.Name: #has same colour prop
                                            positives+=1
                                        else: 
                                            positives+=0.5 #little positive if someone already owns same colour
                                        colourcheck=True
                                        break                                
                                else:
                                    positives+=1 #more positive if nobody else owns
                                    
                    if positives>negatives: #CHECK THIS PART!!!
                        i.Buy()
                        self.Cash-=i.Price
                        self.Owned.append(i)
                        i.Owner=self.Name
                    else:
                        i.Auction(Players)
                        

    def SMEland(self):
        print 'Visual display You have collected one SME point'
        self.SME+=1

    def Chance(self,Players,windowSurface):
        global GOOJchance #counter of GOOJ card
        global Chances
        heavy=Chances[0]
        if heavy==0:
            print 'Visual Advance To Go'
            self.Cash+=200
            self.Position=1
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
        if heavy==1:#Lanercost
            print 'Advance to Lanercost'
            if self.Position==37:
                self.Cash+=200              #Advances through Go
            self.Position=25
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            self.Propertyland(Players)
            
        if heavy==2: #Roselake
            print 'Advance to Roselake'
            if self.Position==37 or self.Position==23:
                self.Cash+=200
            self.Position=12
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            self.Propertyland(Players)
            
        if heavy==3:  #Next Star Space
            print 'Visual Go to SME point'
            if self.Position==8:
                self.Position=13       
            if self.Position==23:
                self.Position=29                
            if self.Position==37:
                self.Position=13
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
                GOOJchance-=1
            else:
                self.Chance(Players,windowSurface)
        if heavy==6:
            print 'Visual Go back three Spaces!'
            self.Position-=3
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #break
        if heavy==7:
            print 'Visual Go to Jail. Do not collect money from Go!'
            self.Position='Jail'
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #self.Jail()
            #break
        if heavy==8:
            print 'Visual General repairs on all your property. Each house =25$   Each Hotel =100$'
            #Houses and Hotel                                                                                                                               #Houses and Hotel Variables
        if heavy==9:
            print 'Visual Pay Poor tax!'
            self.Cash-=15
            FreeParking.Loot+=15
            #break
        if heavy==10:
            print 'Visual You inherit $100 from the bank!'
            self.Cash+=100
            #break
        if heavy==11: #Hartlepool
            print 'Advance to Hartlepool'
            self.Position=40
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            self.Propertyland(Players)
            #break
        if heavy==12:
            print 'Visual you have been elected as Chairman of the Board;ive 50$ each to all players'         #Variable for number of players
            self.Cash-=(len(Players)-1)*50
            for i in Players:
                if i!=self:
                    i.Cash+=50
            #break
        if heavy==13:
            print 'Visual Your building Loan Matures!! Collect $150'
            self.Cash+=150
            #break
        if heavy==15:
            print 'Visual NEW ACHIEVEMENT!! BONUS GAME UNLOCKED!!!!!!!'
            R=random.randint(1,2)
            '''if R==1:
                #coin fall game
            if R==2:
                #SEARCH! game'''
            #break
        if heavy==14:
            print 'Visual Scratch Lottery Card'
            Amount=random.randrange(50,350,50)
            self.Cash+=Amount            
        Chances.pop(0)
        if heavy!=5:
            Chances.append(heavy)
        
            

    def Communitychest(self,Players,windowSurface):
        global Chest
        global GOOJchest
        heavy=Chest[0]
        if heavy==0:
            print 'Visual Advance To Go'
            self.Cash+=200
            self.Position=1
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
        if heavy==1:
            print 'Visual Bank Error in your favor. Collect 200$'
            self.Cash+=200
            #break
        if heavy==2:
            print 'Visual Sale of Stock, you get 50$'
            self.Cash+=50
            #break
        if heavy==3:            
            if GOOJchest>0:
                self.GOOJ+=1
                print 'Visual You have got one Get out of Jail Card'
                print 'GOOJ card can be traded or used when in trouble!'
                GOOJchest-=1
            else:
                self.Communitychest(Players,windowSurface)            
            #break

        if heavy==4: 
            print 'Visual You have been JAILED!'
            self.Position='Jail'
            BoardDisplay(windowSurface)
            for person in Players:
                person.PlayerSpaces(windowSurface)
                pygame.display.flip()
            #self.Jail()
            #break
        
        if heavy==5:    
            print 'Visual Grand Opening Night; Collect 50$ from every player for opening seats!'                    #No of players variable
            self.Cash+=(len(Players)-1)*50
            for i in Players:
                if i!=self:
                    i.Cash-=50
            #break
        

        if heavy==6:
            print 'Visual Your Holiday Xmas  Fund matures! Collect $100'
            self.Cash+=100
            #break
        if heavy==7:
            print 'Visual Income Tax Refund! Collect 20$'
            self.Cash+=20
            #break
        if heavy==8:
            print 'Its your Birthday!!! Collect 10$ from each player'     #No of players variable
            self.Cash+=(len(Players)-1)*10
            for i in Players:
                if i!=self:
                    i.Cash-=10
            #break
                                                                                                                                                                    
        if heavy==9:
            print 'Visual Your Insurance Matures! Collect 100$'
            self.Cash+=100
            #break
        if heavy==10:
            print 'Visual Pay school Fees of 150$!'
            self.Cash-=150
            FreeParking.Loot+=150
            #break
        if heavy==11: 
            print 'Visual Pay 20$ Hospital Fee!'
            self.Cash-=20
            #break
        if heavy==12:
            print 'Visual you are asessed for street repairs! 40$ per house ,115$ per hotel   '                #Houses and Hotel Variables
            #self.Cash-=(40*noofhouses)+(115*noofhotel)
            #break
        if heavy==13:
            print 'You have won 2nd prize in a Beauty Contest! Collect 10$'
            self.Cash+=10
            #break
        if heavy==15:
            print'Visual NEW ACHIEVEMENT!! BONUS GAME UNLOCKED!!!!!!!'
            R=random.randint(1,2)
            '''if R==1:
                #coin fall game
            if R==2:
                #SEARCH! game'''
            #break
        if heavy==14:
            print 'Visual Scratch Lottery Card'
            Amount=random.randrange(50,350,50)
            self.Cash+=Amount
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
            text=basicFont.render('CPU'+str(Players.index(self))+'is',True,BLACK)
            box=text.get_rect(center=(size[0]/2,45*size[1]/100))
            windowSurface.blit(text,box)
            text=basicFont.render('choosing a stop',True,BLACK)
            box=text.get_rect(center=(size[0]/2,size[1]/2))
            windowSurface.blit(text,box)
            pygame.display.flip()
            for event in pygame.event.get(): #replace this with decisions to teleport!
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
                        

'''
    def Jail(self):
        when only 7-8 properties are unowned, play late style (irrespective of cash amount)
            play all doubles only
            trade on either (1)2nd or (2)3rd turn or (3)don't (randomly choose an option with most preferred (3)don't) and same rule for trade
            
        else, try to get out as early
            if also large amount of assets, pay immediately.
            if half of the properties left or cash not so much, play one doubles roll, make double probability most for AI (cheat here)
            if not enough cash or the row ahead has other player's properties, play all doubles
            
        
        change self.Position=11
        moving not allowed. other actions are allowed so trading jail card is within the option
        keep variable that counts number of turns till 3
        define options
        i) pay 50$, allow to roll dice and out.     
        ii) roll doubles and break out
            if doubles come, immediately move that many turns, and stop. 
            if all turns finish go to option (i)
        iii)If having get out of jail, self.GOOJ-=1 and break
        iv) If someone has GOOJ card, trade at beginning of turn, if successful, get out, else, continue
        Note: AI doesn't play mini-game. 

        
    def Teleportland(self):
    
    to teleport to a place on a row, prefer:
    i) least owned properties by others on a side
    ii) the side with most owned properties of the AI
    iii) if every side has owned properties, the side with least owned colour sets by others and with least houses built
    
        visual: point arrows at all teleports
        ask click input from user on self.Position
        change on click, it will be either of these [6,16,26,36]

    def Chance(self):
    if mini game, just generate random prize money for AI
    if scratch card, auto scratch for money
    
        point arrow, ask user to click
        use random to generate one of the cards
        proceed further to define each card.

    def Communitychest(self):
    if mini game, just generate random prize money for AI
    if scratch card, auto scratch for money
    
        point arrow, ask user to click
        use random to generate one of the cards
        proceed further to define each card.
'''
