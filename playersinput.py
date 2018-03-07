import pygame,sys,random,time,eztext
from tokenselect import *
from pygame.locals import *
pygame.init()

#setup the window display
windowSurface = pygame.display.set_mode((960,640), 0, 32) #the tuple has pixels #display is a module within pygame 
pygame.display.set_caption('Super Mumbo Epicness') #the title of window
windowSurface.set_alpha(None)

#setup font
basicFont = pygame.font.SysFont(None, 32)

#set colors R,G,B code
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
VIOLET = (148,0,221)
ORANGE = (255,140,0)

clock=pygame.time.Clock()

blah=0 #links with main program, just a ref.  variable

#finally done logic
#textbox definitions should be outside loop
#NEED TO WORK ON TYPING SPEED!!!!!!

playername=pygame.image.load('Images/bgggs.jpg')
ok=pygame.image.load('Images/ok.jpg')
back=pygame.image.load('Images/back.png')
bg1=pygame.image.load('Images/bg1.jpg')
                      

#error messages for more than 4 players pop up/wrong inputs
Error=basicFont.render('Enter again, total players on board not more than 4',True,ORANGE)
Message=Error.get_rect(center=(650,100))
Error2=basicFont.render('Enter a number only',True,ORANGE)
Message2=Error2.get_rect(center=(480,100))
Error3=basicFont.render('Enter a positive number',True,ORANGE)
Message3=Error3.get_rect(center=(480,100))
Error4=basicFont.render('Enter again, at least 2 players on board needed',True,ORANGE)
Message4=Error4.get_rect(center=(650,100))
#setting instances as per playerno and CPU number (total 4 max)

CPUno=eztext.Input(maxlength=20, color=(255,0,0), prompt='Number of CPU players:')
CPUno.set_pos(460,200)

MEGALIST=[]

def Playerinput(playerno):
    BIG=0 #whole loop variable
    loop=1 #internal loop for text input
    p=0 #for reference to lists and for player number
    CPUloop=1
    lala=0
    #loop for CPU player count if less than 4 human players
    step=0
    global blah #links with main program, just a ref.  variable
    global MEGALIST #to link with token selection
    
    while step==0:
        while BIG==0:
            backbutton=back.get_rect(center=(400+20,200+10))
            okbox=ok.get_rect(center=(480+420+20,200+10))
            print "YAYAYAYA"
            if playerno<4:
                while CPUloop==1:
                    clock.tick(30)
                    for event in pygame.event.get():   
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()

                        mouse=pygame.mouse.get_pressed()
                        if mouse[0]:
                            try:
                                pos=event.pos
                            except AttributeError:
                                pass
                            if backbutton.collidepoint(pos):
                                pygame.time.delay(500)
                                print "hallelujah"
                                blah=1 #to link with main program
                                return blah
                            
                            if okbox.collidepoint(pos):
                                print "entered"
                                try:
                                    CPU=int(CPUno.value)
                                    if CPU<0:
                                        windowSurface.blit(Error3,Message3)
                                        pygame.display.flip()
                                        clock.tick(15)
                                        time.sleep(2)
                                        CPUno.value=''
                                        CPUloop=1
                                    elif CPU+playerno<2:
                                        windowSurface.blit(Error4,Message4)
                                        pygame.display.flip()
                                        clock.tick(15)
                                        time.sleep(2)
                                        CPUno.value=''
                                        CPUloop=1
                                    else:                                            
                                        if CPU+playerno>4:                    
                                            windowSurface.blit(Error,Message)
                                            pygame.display.flip()
                                            clock.tick(15)
                                            time.sleep(2)
                                            CPUno.value=''
                                            CPUloop=1
                                        else:
                                            out=basicFont.render('Number of CPU players:'+str(CPUno.value), True, BLACK)
                                            Cout=out.get_rect(center=(480+117+20,200+10))
                                            
                                            windowSurface.blit(out,Cout)
                                            
                                            CPUloop=2
                                            BIG=2
                                    
                                except ValueError:
                                    if CPUno.value=='':
                                        pass
                                    else:
                                        windowSurface.blit(Error2,Message2)
                                        pygame.display.flip()
                                        clock.tick(15)
                                        time.sleep(2)
                                        CPUno.value=''
                                        CPUloop=1

                        
                        #intend this block here
                        
                        windowSurface.blit(pygame.transform.scale(playername, (960,640)), (0,0))
                        
                        windowSurface.blit(ok,okbox)
                        
                        windowSurface.blit(back,backbutton)
                        CPUno.update(pygame.event.get())
                        CPUno.draw(windowSurface)
                        pygame.display.flip()
                
            
                TOTAL=CPU+playerno
                

            else:
                TOTAL=4
                BIG=2
            
        if BIG==2:
            #setting lists for text input instances and names
            Ptextbox=[]
            Playername=[]
            for i in range(TOTAL):
                Ptextbox.append('null')
                Playername.append(0)

            #the lists 
            print Playername
            print Ptextbox
                    
            #making input instances for number of players                
            while p<playerno:
                print "doing"
                Ptextbox[p]=eztext.Input(maxlength=20, color=(255,0,0), prompt='Player '+str(p+1)+' name:')
                p+=1

            BIG=1
            

            

        #reset p
        p=0
        #for position of text inputs
        i=250

        #text input loop
        while BIG==1:
            if p<playerno:
                clock.tick(30)
                '''for event in pygame.event.get():   
                    if event.type==QUIT:
                        pygame.quit()
                        sys.exit()

                    
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        pos=event.pos
                        if okbox.collidepoint(pos):
                            loop=2
                        if backbutton.collidepoint(pos):
                            if p>0:
                                p-=1
                                i-=50
                                continue
                            if p==0:
                                if playerno==4:
                                    pos=event.pos
                                    if backbutton.collidepoint(pos):
                                        pygame.time.delay(500)
                                        print "hallelujah"
                                        blah=1 #to link with main program
                                        return blah
                                else:
                                    BIG=0
                                    CPUloop=1
                                    break''' 
                for event in pygame.event.get():
                    mouse=pygame.mouse.get_pressed()
                    if mouse[0]:
                        try:
                            pos=event.pos
                        except AttributeError:
                            pass
                        if okbox.collidepoint(pos):
                            loop=2
                        if backbutton.collidepoint(pos):
                            if p>0:
                                p-=1
                                i-=50
                                continue
                            if p==0:
                                if playerno==4:
                                    pos=event.pos
                                    if backbutton.collidepoint(pos):
                                        pygame.time.delay(500)
                                        print "hallelujah"
                                        blah=1 #to link with main program
                                        return blah
                                else:
                                    BIG=0
                                    CPUloop=1
                                    break                
                                                 
                        
                #text inputs   WHERE TO INTEND THIS BLOCK!!!!!   
                    if loop==1:
                        clock.tick(30)
                        try:
                            Ptextbox[p].set_pos(480+20,i)
                        except AttributeError:
                            pass
                        
                        windowSurface.blit(pygame.transform.scale(playername, (960,640)), (0,0))
                        if playerno<4:
                            windowSurface.blit(out,Cout)
                        q=p
                        a=q
                        j=i-(p+1)*50
                        if q>=1:
                            q=0
                            while q<a:
                                Playertext=basicFont.render('Player '+str(q+1)+' name: '+str(Ptextbox[q].value), True, BLACK)
                                Playerbox=Playertext.get_rect(center=(480+116+20,j+61))
                                windowSurface.blit(Playertext,Playerbox)
                                q+=1
                                j+=50
                        okbox=ok.get_rect(center=(480+420+20,j+58))
                        windowSurface.blit(ok,okbox)
                        backbutton=back.get_rect(center=(400+20,j+58))
                        windowSurface.blit(back,backbutton)
                        Ptextbox[p].draw(windowSurface)
                        Ptextbox[p].update(pygame.event.get())
                        pygame.display.flip()
                        
                    #reset value    
                    if loop==2:
                        print "entered"
                        print Ptextbox[p].value     #value of entered text (module definition)
                        Playername[p]=Ptextbox[p].value
                        print "Player",p+1,"name:", Playername[p]     
                        loop=1
                        i+=50
                        p+=1
                        pygame.display.flip() #INSERTED NOW
                #exitting loop once done
            if p==playerno:
                for event in pygame.event.get():   
                    mouse=pygame.mouse.get_pressed()
                    if mouse[0]:
                        try:
                            pos=event.pos
                        except AttributeError:
                            pass
                        if okbox.collidepoint(pos):
                            BIG=3
                            loop=9
                            break
                        if backbutton.collidepoint(pos):
                            p-=1
                            i-=50
                            break
                    Playertext=basicFont.render('Player '+str(p)+' name: '+str(Ptextbox[p-1].value), True, BLACK)
                    Advance=basicFont.render('Click OK to continue, or go back and edit', True, BLUE)
                    white=basicFont.render(105*' ', True, WHITE, (254,254,215)) #just to cover up the text input display instead of clearing screen again
                    space=white.get_rect(center=(700,i-37))
                    pygame.draw.rect(windowSurface,(254,254,215), (space.left-5, space.top-15, space.width, space.height+20))#(254,254,215)
                    okbox=ok.get_rect(center=(480+420+20,j+58+40+15))
                    windowSurface.blit(ok,okbox)
                    backbutton=back.get_rect(center=(400+20,j+58+40+15))
                    windowSurface.blit(back,backbutton)
                    Advancebox=Advance.get_rect(center=(480+116+20,j+200))
                    Playerbox=Playertext.get_rect(center=(480+116+20,j+61))
                    windowSurface.blit(Playertext,Playerbox)
                    windowSurface.blit(Advance,Advancebox)
                    pygame.display.flip()
                                          
        if BIG==3:
            print 'biggy 3'
            k=1
            for i in range(TOTAL):
                if Ptextbox[i]=='null':
                    Ptextbox[i]="CPU"+str(k)
                    Playername[i]=Ptextbox[i]
                    k+=1
            print
            print "Players list:", Playername
            MEGALIST=Playername
            print 'over', MEGALIST
            BIG=5

        while BIG==5:
            print 'hi my name is vineet nice to mee you'
            a=tokenselect(playerno,MEGALIST) #need to do this as a variable else it does again and again
            print 'OHOOOOOOOOOOOOOOO'
            BIG=6
            break
        
        if BIG==6:
            print 'token done'
            if a==10001:
                print "dude we're going back"
                BIG=1
                step=0
                loop=1
                p=playerno
                
            if a==10002:
                BIG=15000
                print 'ya ya this one'
                step=13000
                return
            
#playerno=2
#Playerinput(playerno)
