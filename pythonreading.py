from Players import *
from tokenselect import tokenlist

tokennames=['Car','Dog','Thimble','Trolley','Ship','Iron','Hat','Shoe']

load_profile = open('pythontest.txt','r')

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            #print i,l prints line number from 0 with content in each line! 
            pass
    return i + 1 #number of lines (counts from 0) 

read_it = load_profile.read().splitlines()

playerno=file_len('pythontest.txt')/2

print playerno

Players=[]

for i in range(playerno):
    Players.append(Player('name','peg'))


count=0
for i in range(2*playerno):
    print read_it[i],
    if i%2==0:
        tempo=read_it[i]
    else:
        Players[count].Name=tempo
        #Players[count].Peg=read_it[i]
        for j in range(8):
            if tokennames[j]==read_it[i]:
                Players[count].Peg=tokenlist[j]
        count+=1


