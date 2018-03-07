import random
Chance=[]
while len(Chance)<16:
    number=random.randint(0,15)
    if number not in Chance:
        Chance.append(number)



while True:
    print 'chance list:'
    print Chance
    print
    a=raw_input("dare to take a chance?:")
    while a.lower()!='y':
        a=raw_input("dare to take a chance?:")
    b=Chance[0]
    Chance.pop(0)
    Chance.append(b)
    print
