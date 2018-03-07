def Jail(self):
    '''To be inserted: (Visual) YOU ARE IN JAIL'''

    #hi Pravi cute girl 30! Here's your task...
    
    #Objective: just make the statements!!!!!!!!
   

    #keep variable count as 0, at end of every turn add it by 1
    #at the end of the third turn, when count will become 3 then break out of
    #function with whatever outcome there is
    

    #keep variable minigamecash for checking option 2
    #set it however you are making the code
    
    #make the list of options here below
    #like how we do in menu driven right?
    #if elif statements and else

    """option 1: Roll doubles"""
    #to be inserted: rolling action

    #make the below if statements and comment them
    #if double or not

    
    """option 2: Spend cash to play mini game"""
    #to be inserted: mini games

    #(for 1st turn) if count==0
    #(for 2nd turn) if count==1
    #(for 3nd turn) if count==2

    #Note :remember, count becomes 3 at the END of everything.
    #because we start from 0

    #if person wins: return
    
    """option 3: use get out of jail card"""
    #check if self.GOOJ>0:
        #self.GOOJ-=1           @that variable keeps count of Jail card
        #return    

    """option 4: Pay 50 get out"""
    

    #increment count with 1,
    #increment minigamecash by 10
    #then check if count==3 for getting out of jail

def Jail(self):
    count=0
    s=0
    self.GOOJ()
    while s==0:
        print "1. roll doubles "
        print "2.Spend cash to play mini game"
        print "3. use get out of jail card"
        print "4. Pay 50 get out"
        print
        option=input ("input your choice:")
        if option==1:
            count=count+1
            


        if option==2:
            #self.minigames
            #if self.minigames =0:
            #  if lost
            if self.minigames==1:
                return
            cash=20
            if count ==0:
                #self.playerscash-=cash
             if count ==1:
                #self.playerscash-=cash*count

             if count ==2:
                #self.playerscash-=cash*count
             if count ==3:
                break
            count=0
        if option==3:
            if self.GOOJ>0:
                self.GOOJ-=1
                return
        if option==4:
            count=count+1
            if count==3:
                return
            self.minicash+=10
        else:
            s=1
            
