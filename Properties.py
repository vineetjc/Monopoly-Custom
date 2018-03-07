'''
VERY IMPORTANT: Colour is spelled with the 'u' whatever we do in this project.

#need to develop this mainly'''
class Property:
    def __init__(self,Name,Colour,Price,BasicRent,House1Rent,House2Rent,House3Rent,House4Rent,HotelRent,Position): 
        self.Name=Name
        self.Owner=None
        self.Colour=Colour
        self.Price=Price
        self.BasicRent=BasicRent
        self.House1Rent=House1Rent
        self.House2Rent=House2Rent
        self.House3Rent=House3Rent
        self.House4Rent=House4Rent
        self.HotelRent=HotelRent
        self.Houses=0
        self.Position=Position #position number with reference to board, and Go is marked 1

    def Buy(self): #pay base price, give Title Deed card to owner, set Owner name
        Unowned.remove(self)
        #Player.cash-=self.Price
        #self.Owner=#Player.Name

    def Rent(self,Players): #calculate new variable rent based on number of houses/hotels, else put basic rent. if SME points were spent, increase hotel rent if any, to 20% extra
        if self.Houses==0:
            Rent=self.BasicRent
        elif self.Houses==1:
            Rent=self.House1Rent
        elif self.Houses==2:
            Rent=self.House2Rent
        elif self.Houses==3:
            Rent=self.House3Rent
        elif self.Houses==4:
            Rent=self.House4Rent
        elif self.Houses==5:
            Rent=self.HotelRent
        for person in Players:
            if self.Owner==person.Name: #checks who's the place owner
                if self not in person.Mortgaged: #checks if place is mortgaged
                    print 'owner has',person.Cash
                    person.Cash+=Rent
                    print person.Cash
        return Rent
        
    def Auction(self,Players): #completed!!! :D B)
        playerno=len(Players)
        #global highest
        highest=0
        backoff=[None for i in range(playerno)]
        Bids=[0 for i in range(playerno)]
        done=False
        while not done:
            for i in range(len(Bids)):
                if backoff[i]!='no bid':
                    choice=raw_input('you wanna bid'+Players[i].Name+'?? y/n: ')
                    while choice not in ['y','Y','n','N']:
                        choice=raw_input('you wanna bid'+Players[i].Name+'?? y/n: ')
                    if choice in ['Y','y']:
                        Bids[i]=input('Place your bid'+Players[i].Name+': ')
                        if Bids[i]<=highest:
                            Bids[i]=input('Enter higher bid'+Players[i].Name+': ')                        
                        highest=Bids[i]

                        for j in Bids: #sets the rest into 0
                            if j!=highest or j!=None:
                                j=0
                                
                    if choice in ['N','n']:
                        Bids[i]=None
                        backoff[i]='no bid'
            count=0
            for i in Bids:
                if i==None:
                    count+=1
            if count==playerno-1:
                #Player.Cash-=highest
                #self.Owner=Player.Name
                print highest,'bid final'
                for i in range(playerno):
                    if backoff[i]==None:
                        print Players[i].Name,'bidded',Bids[i]
                        self.Buy()
                        Players[i].Cash-=highest
                        self.Owner=Players[i].Name
                        Players[i].Owned.append(self)
                        
                done=True

#this still needs work based on each one's houses of same colour
    def Build(self):        #visuals have buttons for 1-4 houses and hotel. if hotel is clicked, then 5
        self.Houses=input("how many houses?? :") #s is 5 to the max
        #Player.Cash-=(self.Houses*i.HouseCost)
        
        #check number of houses, build one implies add to it. if houses are 4, then next hotel
        
    def Mortgage(self):
        #Player.Cash+=self.Houses*(self.HouseCost/2)
        self.Houses=0        
        self.Price=self.Price/2 #half price for now, unmortgage has the 10% 
        self.Owner = "Bank" #NOTE: it's still in the Owned list

        #check for no houses/hotel on it, if there are, sell for their half price;
        #give property to bank for half price
        #switch off rent function
        
    def Unmortgage(self):
        if self.Owner=='Bank':
            #self.Owner=Player.Name
            #Player.Cash-=(self.Price+self.Price/10) #10% of half price 
            for i in Properties:
                if i.Name==self.Name:
                    self.Price=i.Price #resetting self.Price
        
    def Destroy(self):
        selling=input("how many houses to sell?:") #if hotel, then 5-selling
        self.Houses-=selling
         #Player.Cash+=selling*(self.HouseCost/2)       


#------------------------------------------------------------------------------------------------------------------------

#definitions of properties

Solaris=Property('Solaris','Purple',60,2,10,30,90,160,250,2)
BlackHollow=Property('Black Hollow','Purple',60,4,20,60,180,320,450,4)

Purple=[Solaris,BlackHollow]


Warrington=Property('Warrington','Light Blue',100,6,30,90,270,400,550,7)
Armagh=Property('Armagh','Light Blue',100,6,30,90,270,400,550,9)
Willsden=Property('Willsden','Light Blue',120,8,40,100,300,450,600,10)


LightBlue=[Warrington,Armagh,Willsden]

Roselake=Property('Roselake','Pink',140,10,50,150,450,625,750,12)
Myrefall=Property('Myrefall','Pink',140,10,50,150,450,625,750,14)
Larkinge=Property('Larkinge','Pink',160,12,60,180,500,700,900,15)

Pink=[Roselake,Myrefall,Larkinge]


Windmere=Property('Windmere','Orange',180,14,70,200,550,750,950,17)
Frostford=Property('Frostford','Orange',180,14,70,200,550,750,950,19)
Bleakburn=Property('Bleakburn','Orange',200,16,80,220,500,800,1000,20)

Orange=[Windmere,Frostford,Bleakburn]

Veritas=Property('Veritas','Red',220,18,90,250,700,875,1050,22)
Sharpton=Property('Sharpton','Red',220,18,90,250,700,875,1050,24)
Lanercost=Property('Lanercost','Red',240,20,100,300,750,925,1100,25)

Red=[Veritas,Sharpton,Lanercost]

Hewe=Property('Hewe','Yellow',260,22,110,330,800,975,1150,27)
Stanmore=Property('Stanmore','Yellow',260,22,110,330,800,975,1150,28)
Tillicoultry=Property('Tillicoultry','Yellow',280,24,120,360,850,1025,1200,30)

Yellow=[Hewe,Stanmore,Tillicoultry]

Grasmere=Property('Grasmere','Green',300,26,130,390,900,1100,1275,32)
Arcton=Property('Arcton','Green',300,26,130,390,900,1100,1275,33)
Swindon=Property('Swindon','Green',320,28,150,450,1000,1200,1400,35)

Green=[Grasmere,Arcton,Swindon]

Wolfden=Property('Wolfden','Dark Blue',350,35,175,500,1100,1300,1500,38)
Hartlepool=Property('Hartlepool','Dark Blue',400,50,200,600,1400,1700,2000,40)

DarkBlue=[Wolfden,Hartlepool]

Properties=Purple+LightBlue+Pink+Orange+Red+Yellow+Green+DarkBlue #is a list that's for ref. to all standard values, will never be modified

Unowned=Purple+LightBlue+Pink+Orange+Red+Yellow+Green+DarkBlue #this is modified when a property is bought off

for i in Properties:
    if i in Purple or i in LightBlue:
        i.HouseCost=50        
    if i in Pink or i in Orange:
        i.HouseCost=100        
    if i in Red or i in Yellow:
        i.HouseCost=150        
    if i in Green or i in DarkBlue:
        i.HouseCost=200


#Other tiles!

FreeParking=Property('Free Parking', None,None,None,None,None,None,None,None,21)
FreeParking.Loot=0

#names of colours, list
ColoursList=['Purple','LightBlue','Pink','Orange','Red','Yellow','Green','DarkBlue']

#list of colour prop lists, just for easy method
ColourProps=[Purple,LightBlue,Pink,Orange,Red,Yellow,Green,DarkBlue]

#properties by rows
Row1=Purple+LightBlue
Row2=Pink+Orange
Row3=Red+Yellow
Row4=Green+DarkBlue

'''suma=0
for i in Properties:
    suma+=i.Price

print suma'''
