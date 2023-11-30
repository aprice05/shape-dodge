import pygame
import random
from engi1020.arduino.api import *
import time
def findhighscore():
    scorefile=open('highscore.txt', 'r')
    highscore=0
    for line in scorefile.readlines():
        try:
            num = int(line)
        except ValueError:
            num=0
        if num>highscore:
            highscore=num
    scorefile.close()
    return highscore
caption2=str((findhighscore()))


def main():
    
 
    pygame.init()
 
    pygame.display.set_caption('1020 Game, High score:'+caption2)
    screen = pygame.display.set_mode((800,600))
    
    screen.fill((125,201,196))
    red=(255,0,0)
    orange=(255,128,0)
    yellow=(255,255,0)
    green=(0,255,0)
    blue=(0,0,255)
    indigo=(25,0,51)
    purple=(128,0,128)
    black=(0,0,0)
    white=(255,255,255)
    brown=(102,51,0)
    
    colors=[red,orange,yellow,green,blue,indigo,purple,black,white,brown]

    screen_width=800
    screen_height=600
    
    #player variables
    pygame.display.flip()
    xpos = 250
    ypos = 250
    step_x=15
    step_y=15
    
    #bouncing object variables
    objcolor1=random.choice(colors)
    objx1=random.randint(0,45)
    objy1=random.randint(500,550)
    xposo1=objx1
    yposo1=objy1
    step1_x=5
    step1_y=5
    
    objcolor2=random.choice(colors)
    objx2=random.randint(0,45)
    objy2=random.randint(500,550)
    xposo2=objx2
    yposo2=objy2
    step2_x=random.randint(5,10)
    step2_y=random.randint(5,10)
    
    objcolor3=random.choice(colors)
    objx3=random.randint(0,45)
    objy3=random.randint(500,550)
    xposo3=objx3
    yposo3=objy3
    step3_x=random.randint(10,15)
    step3_y=random.randint(10,15)
    
    objcolor4=random.choice(colors)
    objx4=random.randint(0,45)
    objy4=random.randint(500,550)
    xposo4=objx4
    yposo4=objy4
    step4_x=random.randint(15,20)
    step4_y=random.randint(15,20)
    
    objcolor5=random.choice(colors)
    objx5=random.randint(0,45)
    objy5=random.randint(500,550)
    xposo5=objx5
    yposo5=objy5
    step5_x=5
    step5_y=5
    
    #spike variables
    spikespeed=20
    spike_y=0
    spike_y = 0
    spike_x = random.randrange(20,780)

    spike_y2 = 0
    spike_x2 = random.randrange(20, 780)

    spike_y3 = 0
    spike_x3 = random.randrange(20, 780)

    spike_y4 = 0
    spike_x4 = random.randrange(20, 780)

    misslespeed = 40

    missle_y = 0
    missle_x = random.randrange(20, 780)
    
    #powerup variables
    puspawntime = random.randrange(30, 60)
    puspawntime2 = random.randrange(30, 60)
    spawnchance = 1
    spawnchance2 = 1
    
    purt_x = random.randrange(20, 780)
    purt_y = random.randrange(20, 580)
    
    purt_x2 = random.randrange(20, 780)
    purt_y2 = random.randrange(20, 580)
    
    pygame.time.delay(3000)
    running=True
    while running:
        pygame.time.delay(50)
        
        time=pygame.USEREVENT+1
        global clock
        clock=int((pygame.time.get_ticks())/1000)-3
        gametime=clock*difficulty

        for event in pygame.event.get():          
            if event.type == pygame.QUIT:
                running = False
            if event.type == time:
                clock+=1
       
        key=pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if xpos<0:
                xpos+=step_x
            else:
                xpos-=step_x
        
        if key[pygame.K_RIGHT]:
            if xpos<screen_width-30:
                xpos+=step_x
            else:
                xpos-=step_x
        if key[pygame.K_UP]:
            if ypos<0:
                ypos+=step_y
            else:
                ypos-=step_y
        if key[pygame.K_DOWN]:
            if ypos>screen_height-30:
                ypos-=step_y
            else:
                ypos+=step_y
        pygame.draw.rect(screen,red,[xpos,ypos,30,30],0)
        player=pygame.Rect((xpos,ypos),(30,30))
        
        if xposo1>screen_width-20 or xposo1<0:
            step1_x= -step1_x    
        if yposo1>screen_height-20 or yposo1<0:
            step1_y= -step1_y
        xposo1+=step1_x
        yposo1+=step1_y
        
        if gametime>=10:
               
            if xposo2>screen_width-25 or xposo2<0:
                step2_x= -step2_x    
            if yposo2>screen_height-25 or yposo2<0:
                step2_y= -step2_y
            xposo2+=step2_x
            yposo2+=step2_y
            
            pygame.draw.rect(screen,objcolor2,[(xposo2),(yposo2),25,25],0)
            obj2=pygame.Rect((xposo2,yposo2),(25,25))
            
            if gametime>=20:
                if xposo3>screen_width-20 or xposo3<0:
                    step3_x= -step3_x    
                if yposo3>screen_height-20 or yposo3<0:
                    step3_y= -step3_y
                xposo3+=step3_x
                yposo3+=step3_y
                
                pygame.draw.rect(screen,objcolor3,[(xposo3),(yposo3),20,20],0)
                obj3=pygame.Rect((xposo3,yposo3),(20,20))
            
            if gametime>=30:
                if xposo4>screen_width-30 or xposo4<0:
                    step4_x= -step4_x    
                if yposo4>screen_height-30 or yposo4<0:
                    step4_y= -step4_y
                xposo4+=step4_x
                yposo4+=step4_y
                
                pygame.draw.rect(screen,objcolor4,[(xposo4),(yposo4),30,30],0)
                obj4=pygame.Rect((xposo4,yposo4),(30,30))
                
            if gametime>=40:
                if xposo5>screen_width-50 or xposo5<0:
                    step5_x= -step5_x    
                if yposo5>screen_height-50 or yposo5<0:
                    step5_y= -step5_y
                xposo5+=step5_x
                yposo5+=step5_y
                
                pygame.draw.rect(screen,objcolor5,[(xposo5),(yposo5),50,50],0)
                obj5=pygame.Rect((xposo5,yposo5),(50,50))
       
        spike_y+=spikespeed
        if spike_y > screen_height:
            spike_x = random.randrange(20,740)
            spike_y=-25
        pygame.draw.rect(screen,black,[(spike_x),(spike_y),40,40],8)
        objspike=pygame.Rect((spike_x,spike_y),(30,30))
        
        if gametime>15:
         
            pygame.draw.rect(screen,black,[(spike_x2),(spike_y2),40,40],8)
            objspike2=pygame.Rect((spike_x2,spike_y2),(30,30))
            
            spike_y2+=spikespeed
            if spike_y2>screen_height:
                spike_x2=random.randrange(20,740)
                spike_y2= -25
        if gametime>30:
            pygame.draw.rect(screen,black,[(spike_x3),(spike_y3),40,40],8)
            objspike3=pygame.Rect((spike_x3,spike_y3),(30,30))
            
            spike_y3+=spikespeed
            if spike_y3>screen_height:
                spike_x3=random.randrange(20,740)
                spike_y3=-25
        if gametime>45:
            pygame.draw.rect(screen,black,[(spike_x4),(spike_y4),40,40],8)
            objspike4=pygame.Rect((spike_x4,spike_y4),(30,30))
            
            spike_y4+=spikespeed
            if spike_y4>screen_height:
                spike_x4=random.randrange(20,740)
                spike_y4=-25
        if gametime>60:
            pygame.draw.rect(screen,black,[(missle_x),(missle_y),40,40],8)
            objmissle=pygame.Rect((missle_x,missle_y),(30,30))
            missle_y+=misslespeed
            if missle_y>screen_height:
                missle_x=random.randrange(20,740)
                missle_y=-25
    
        if gametime<10:
            obj2=pygame.Rect((1000,1000),(1,1))
        if gametime<15:
            objspike2=pygame.Rect((1000,1000),(1,1))
        if gametime <20:
            obj3=pygame.Rect((1000,1000),(1,1))
        if gametime <30:
            obj4=pygame.Rect((1000,1000),(1,1))
            objspike3=pygame.Rect((1000,1000),(1,1))
        if gametime <40:
            obj5=pygame.Rect((1000,1000),(1,1))
        if gametime<45:
            objspike4=pygame.Rect((1000,1000),(1,1))
        if gametime<60:
            objmissle=pygame.Rect((1000,1000),(1,1))
    
        pygame.draw.rect(screen,objcolor1,[(xposo1),(yposo1),20,20],0)
        obj1=pygame.Rect((xposo1,yposo1),(20,20))
        
        pygame.Rect.move(obj1,(xposo1,yposo1))
        pygame.display.update()
        screen.fill((125,201,196))
    
        
        if spawnchance == 1:
            if gametime >= puspawntime:
                pygame.draw.circle(screen, blue, [purt_x, purt_y], 12, 10)
                objantispeed=pygame.Rect((purt_x,purt_y),(24,24))
                if pygame.Rect.colliderect(player,objantispeed) == True:
                    spikespeed-=5
                    misslespeed-=10
                    purt_y = 1000
     
        if spawnchance2 == 1:
            if gametime >= puspawntime2:
                pygame.draw.circle(screen, red, [purt_x2, purt_y2], 24, 10)
                objspeed=pygame.Rect((purt_x2,purt_y2),(48,48))
                if pygame.Rect.colliderect(player,objspeed) == True:
                    spikespeed+=10
                    misslespeed+=10
                    purt_y2 = 1000

            
        if (pygame.Rect.colliderect(player,obj1))==True or (pygame.Rect.colliderect(player,obj2))==True or (pygame.Rect.colliderect(player,obj3))==True or (pygame.Rect.colliderect(player,obj4))==True or (pygame.Rect.colliderect(player,obj5))==True:
            running=False
            
        if pygame.Rect.colliderect(player,objspike)== True or pygame.Rect.colliderect(player,objspike2)== True or pygame.Rect.colliderect(player,objspike3)==True or pygame.Rect.colliderect(player,objspike4)==True:
            running=False
               
while True:
    oled_clear()
    difficulty=round((analog_read(0)+381)/862,2)
    oled_print('Gamespeed is:')
    oled_print(difficulty)
    oled_print('Hold button to start!')
    time.sleep(3)
    if digital_read(6)==True:
        break
    
main()

oled_clear()
digital_write(4,True)
buzzer_note(5,500,2)
oled_print('Your final score was:') 
oled_print(clock)
scorefile=open('highscore.txt', 'a+')
scorefile.write('\n'+str(clock))
scorefile.close()




    