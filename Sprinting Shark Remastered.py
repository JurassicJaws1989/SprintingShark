import pygame
import time
import math
import random


pygame.init()



#game window...

window = pygame.display.set_mode((800,600))
pygame.display.set_caption("Sprinting Shark! -- 1.0.0.2")

#colors
blue = (0,0,100)
red =(139,26,26,255)
white = (255,255,255)
butColor = (132,180,255,255)
clickColor = (135,225,250,255)
green = (84,139,84,255)

#sounds
endSound = pygame.mixer.Sound('end.wav')
eat = pygame.mixer.Sound('eat.wav')
ammoSound = pygame.mixer.Sound('ammo.wav')
shootSound = pygame.mixer.Sound('shoot.wav')
killSound = pygame.mixer.Sound('kill.wav')
hitSound = pygame.mixer.Sound('hit.wav')
screamSound = pygame.mixer.Sound('scream.wav')
popSound = pygame.mixer.Sound('pop.wav')
boomSound = pygame.mixer.Sound('boom.wav')
dolphinSound = pygame.mixer.Sound('dolphin.wav')
squidSound = pygame.mixer.Sound('squid.wav')



#sound functions
def playMusic():
    playlist = list()
    playlist.append ("underwater.wav")
    pygame.mixer.music.load( playlist.pop() )
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)

def end():
    pygame.mixer.Sound.play(endSound)

def eating():
    pygame.mixer.Sound.play(eat)
def ammo():
    pygame.mixer.Sound.play(ammoSound)
def shoot():
    pygame.mixer.Sound.play(shootSound)
def killed():
    pygame.mixer.Sound.play(killSound)
def hit():
    pygame.mixer.Sound.play(hitSound)
def scream():
    pygame.mixer.Sound.play(screamSound)
def pop():
    pygame.mixer.Sound.play(popSound)
def boom():
    pygame.mixer.Sound.play(boomSound)
def dolphSound():
    pygame.mixer.Sound.play(dolphinSound)
def squidsSound():
    pygame.mixer.Sound.play(squidSound)
    
#STD Variables
width = window.get_width()
height = window.get_height()
mouse = pygame.mouse.get_pos()
clock = pygame.time.Clock()

#images

background = pygame.image.load('Background.png')
menu = pygame.image.load('Menu.png')
deadShark = pygame.image.load('deadshark.png')

#highscore
def highscore(scor):
    
    file_object = open("Score.txt", "r")
    
    
    old = file_object.read()
    olde = int(old)
    if scor > olde:
        new = str(scor)
        file = open("Score.txt", "w+")
        file.write(new)
        file_object.close()
        file.close()
        
    else:
        file_object.close()


#menu text

def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()
def text_objects2(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

#Button Function
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(window, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(window, ic,(x,y,w,h))

    smallText = pygame.font.Font('freesansbold.ttf',12)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    window.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

#Main Menu
def intro():
    playMusic()

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        file = open("Score.txt", "r")
        scor = file.read()
                
        window.fill(blue)
        window.blit(menu, [0,0])

        
        lgtext = pygame.font.Font('freesansbold.ttf',24)
        smtext = pygame.font.Font('freesansbold.ttf',16)

        TextSurf, TextRect = text_objects("High Score: " + scor, smtext)
        TextRect.center = (400,225)
        window.blit(TextSurf, TextRect)

                    
        TextSurf, TextRect = text_objects("Sprinting Shark!", lgtext)
        TextSurf2, TextRect2 = text_objects2("Sprinting Shark!", lgtext)
        TextRect.center = (400,150)
        window.blit(TextSurf, TextRect)
        TextRect2.center = (400,155)
        window.blit(TextSurf2, TextRect2)
        
        

        button("Play",350,275,100,50,butColor,clickColor,gameLoop)
        button("Quit",350,375,100,50,butColor,clickColor,quitgame)
        

    
        pygame.display.update()
        clock.tick(15)

#Screen Score
def score(count):
    
    font = pygame.font.SysFont(None,22)
    text = font.render("Score: "+str(count), True, red)
    window.blit(text, (0,10))

#lasers

def lasers(count):

    font = pygame.font.SysFont(None,22)

    if count == 0:
        text = font.render("Lasers: "+str(count), True, red)
        window.blit(text, (700,30))
    elif count > 0:
        text = font.render("Lasers: "+str(count), True, green)
        window.blit(text, (700,30))
        
        

#Health       
def sharkHealth(health, x, y):
    dx = x
    dy = y
    death = 0
    
    font = pygame.font.SysFont(None,22)
    fonts = pygame.font.SysFont(None,36)

    if health >= 50:
        
        text = font.render("Health: "+str(health)+"%", True, green)
        window.blit(text, (700,10))

    elif health < 50:

        text = font.render("Health: "+str(health)+"%", True, red)
        window.blit(text, (700,10))

    elif health > 100:

        health = 100

    elif health < 0:
        health = 0


    
        

    #elif health == 0:

        #text = font.render("Shark is Dead!", True, red)
        #window.blit(text, (300,300))
        
        
        
        #pygame.time.wait(2000)
        #intro()

#Extra Variables
swimcount = 0
count = 0
xcount = 0

#images

shark = [pygame.image.load('shark_0.png'), pygame.image.load('shark_1.png'), pygame.image.load('shark_2.png'), pygame.image.load('shark_3.png'), pygame.image.load('shark_4.png')]
turtle = [pygame.image.load('turtle_0.png'), pygame.image.load('turtle_1.png'), pygame.image.load('turtle_2.png'), pygame.image.load('turtle_3.png')]
blood = pygame.image.load('blood.png')
crate = pygame.image.load('crate.png')
laser = pygame.image.load('laser.png')
barrel = pygame.image.load('barrel.png')
man = [pygame.image.load('man_0.png'), pygame.image.load('man_1.png'), pygame.image.load('man_2.png'), pygame.image.load('man_3.png')]
puffer = pygame.image.load('puffer.png')
fish = pygame.image.load('fish.png')
dolphin = [pygame.image.load('dolphin_0.png'), pygame.image.load('dolphin_1.png'), pygame.image.load('dolphin_2.png'), pygame.image.load('dolphin_3.png')]
squid = [pygame.image.load('squid_0.png'), pygame.image.load('squid_1.png'), pygame.image.load('squid_2.png'), pygame.image.load('squid_3.png')]


#Swimming Shark (Character)    
def sharkdraws(x,y):
    global swimcount
    

    
        

    if swimcount == 0:
        window.blit(shark[0], (x,y))
        swimcount += 1

    elif swimcount == 1:
        window.blit(shark[1], (x,y))
        swimcount += 1

    elif swimcount == 2:
        window.blit(shark[2], (x,y))
        swimcount += 1
    elif swimcount == 3:
        window.blit(shark[3], (x,y))
        swimcount += 1
    elif swimcount == 4:
        window.blit(shark[4], (x,y))
        swimcount += 1
   
 

    else:
        window.blit(shark[0], (x,y))
        swimcount = 0

def thingdraws(x,y,thing):
    
    
    global xcount

    
      

    if xcount == 0:
        window.blit(thing[0], (x,y))
        xcount += 1

    elif xcount == 1:
        window.blit(thing[1], (x,y))
        xcount += 1

    elif xcount == 2:
        window.blit(thing[2], (x,y))
        xcount += 1
    elif xcount == 3:
        window.blit(thing[3], (x,y))
        xcount += 1
    
   
    else:
        window.blit(thing[0], (x,y))
        xcount = 0

def movescreen(x,y):
    window.blit(background, (x,y))

def dead(x, y, x2, y2):

    font = pygame.font.SysFont(None,36)
    fonts = pygame.font.SysFont(None,36)

    death = 0
    end()
    window.blit(background, [x2,y2])
    while death < 30:
        window.blit(background, [x2,y2])
        
        window.blit(deadShark, [x,y])

        y -=20
        
        
        pygame.time.wait(250)
        pygame.display.update()
        death += 1

    
    pygame.time.wait(3000)
    intro()


    
    
    
   
                    


def gameLoop():
    

    

    x = 100
    y = 150
    bgx = 0
    bgy = 0
    bgx2 = 2400
    bgy2 = 0
    x_change = 0
    y_change = 0
    vel = 5
    swimcount = 0
    bgx_change = 0
    bgy_change = 0
    health = 100
    count = 0
    swimcount = 0
    death = 0
    turtx = 2000
    turty = random.randrange(25,575)
    turtCount = 0
    laserCount = 0
    lasx = 10000
    lasy = 550
    shot = False
    lx = -1000
    ly = -1000
    bx = 4000
    by = random.randrange(25,575)
    bv = 10
    bCount = 0
    manx = 15000
    many = random.randrange(25,575)
    manCount = 0
    px = 10000
    py = random.randrange(25,575)
    fx = 2000
    fy = random.randrange(25,575)
    dolx = 15000
    doly = random.randrange(25,575)
    sx = 20000
    sy = random.randrange(25,575)
    
    

    gameExit = False

    #Char Movement

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = 0
                    bgx_change = 0
                elif event.key == pygame.K_RIGHT:
                    bgx_change = -15
                    x_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -15
                    
                elif event.key == pygame.K_DOWN:
                    y_change = 15

                elif event.key == pygame.K_SPACE:
                    lx = x + 200
                    ly = y
                    shootCount = 50
                    if laserCount > 0:
                        shoot()
                        laserCount -= 1
                        while shootCount > 0:
                            
                            window.blit(laser, [lx,ly])
                            lx += 10
                            shootCount -= 1
                            pygame.display.update()
                            #turtle death
                            if ly < turty + 32 and ly+50 > turty:
                                if lx+32 > turtx and lx < turtx+32:
                    
                                    count += 10
                                    turtx = 2500
                                    turty = random.randrange(25,575)
                                    killed()

                            #barrel death

                            if ly < by + 32 and ly+50 > by:
                                if lx+32 > bx and lx < bx+32:
                    
                                    count += 50
                                    bx = 1000
                                    by = random.randrange(25,575)
                                    bv += 3
                                    boom()

                            #man death

                            if ly < many + 32 and ly+50 > many:
                                if lx+32 > manx and lx < manx+32:
                    
                                    count += 25
                                    manx = 8000
                                    by = random.randrange(25,575)
                                    bv = 15
                                    scream()

                            #puffer death

                            if ly < py + 32 and ly+50 > py:
                                if lx+32 > px and lx < px+32:
                    
                                    count += 25
                                    px = 10000
                                    py = random.randrange(25,575)
                                    
                                    pop()

                            #fish death

                            if ly < fy + 32 and ly+50 > fy:
                                if lx+32 > fx and lx < fx+32:
                    
                                    count += 10
                                    fx = 2000
                                    fy = random.randrange(25,575)
                                    
                                    killed()

                            #dolphin death

                            if ly < doly + 32 and ly+50 > doly:
                                if lx+32 > dolx and lx < dolx+32:
                    
                                    count += 100
                                    dolx = 10000
                                    doly = random.randrange(25,575)
                                    
                                    dolphSound()

                            #squid death

                            if ly < sy + 32 and ly+50 > sy:
                                if lx+32 > sx and lx < sx+32:
                    
                                    count += 1000
                                    sx = 20000
                                    sy = random.randrange(25,575)
                                    
                                    squidsSound()
                           
                    
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                    bgx_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0




        x += x_change
        y += y_change
        bgx += bgx_change
        bgx2 += bgx_change
        bgy += bgy_change
        window.fill(blue)
        window.blit(background, [bgx,bgy])
        window.blit(background, [bgx2,bgy2])
        sharkdraws(x,y)

        #turtle
        thingdraws(turtx,turty,turtle)
        turtx = (turtx - 20)
        if turtx <= -500:
            turtx = 2500
            turty = random.randrange(25,575)

        if y < turty + 32 and y+50 > turty:
            if x+200 > turtx and x < turtx+32:
                health += 15
                count += 15
                turtx = 2500
                turty = random.randrange(25,575)
                eating()
                
                
                if health >= 100:
                    health = 100

        #man
        thingdraws(manx,many,man)
        manx = (manx - 15)
        if manx <= -500:
            manx = 8000
            many = random.randrange(25,575)

        if y < many + 32 and y+50 > many:
            if x+200 > manx and x < manx+32:
                health += 50
                count += 100
                bv = 10
                manx = 8000
                many = random.randrange(25,575)
                scream()
                
                
                if health >= 100:
                    health = 100

        #dolphin
        thingdraws(dolx,doly,dolphin)
        dolx = (dolx - 15)
        if dolx <= -500:
            dolx = 10000
            doly = random.randrange(25,575)

        if y < doly + 32 and y+50 > doly:
            if x+200 > dolx and x < dolx+32:
                health -= 25
                count += 10
                bv = 10
                dolx = 10000
                doly = random.randrange(25,575)
                dolphSound()
                
                
                if health >= 100:
                    health = 100

        #squid
        thingdraws(sx,sy,squid)
        sx = (sx - 15)
        if sx <= -500:
            sx = 20000
            sy = random.randrange(25,575)

        if y < sy + 32 and y+50 > sy:
            if x+200 > sx and x < sx+32:
                health -= 75
                count += 10
                bv = 10
                sx = 20000
                sy = random.randrange(25,575)
                squidsSound()
                
                
                if health >= 100:
                    health = 100


        #barrels
        window.blit(barrel, [bx,by])
        bx = (bx - bv)
        if bx <= -500:
            bx = 1000
            bv = bv + 3
            count += 10
            by = random.randrange(25,575)

        if y < by + 32 and y+50 > by:
            if x+200 > bx and x < bx+32:
                
                hit()
                bx = 1000
                bv = bv + 3
                by = random.randrange(25,575)
                health -= 50

        #puffer
        window.blit(puffer, [px,py])
        px = (px - 20)
        if px <= -500:
            px = 10000
            
            count += 10
            py = random.randrange(25,575)

        if y < py + 32 and y+50 > py:
            if x+200 > px and x < px+32:
                health -= 25
                pop()
                px = 10000
                
                py = random.randrange(25,575)


        #fish
        window.blit(fish, [fx,fy])
        fx = (fx - 10)
        if fx <= -500:
            fx = 2000
            
            
            fy = random.randrange(25,575)

        if y < fy + 32 and y+50 > fy:
            if x+200 > fx and x < fx+32:
                health += 10
                eating()
                fx = 2000
                count += 15
                fy = random.randrange(25,575)
                if health >= 100:
                    health = 100
                
                
                
                
                
                
                
        

        
            
            

        #lasers
        window.blit(crate, [lasx,lasy])
        lasx = (lasx - 15)
        if lasx <= -500:
            lasx = 10000
            

        if y < lasy + 32 and y+50 > lasy:
            if x+200 > lasx and x < lasx+32:
                
                count += 25
                lasx = 10000
                laserCount += 5
                ammo()
                
                turtCount = 0
                if health >= 100:
                    health = 100
        


        score(count)
        sharkHealth(health, x, y)
        highscore(count)
        lasers(laserCount)


        pygame.display.update()
        clock.tick(30)

    
        #Cross Screen Movement

        if x <= -200:
            x = 690

        if x >= 700:
            x = -210

        if y <= 10:
            y = 15

        if y >= 550:
            y = 545

        if bgx < background.get_width() * -1:
            bgx = background.get_width() - 100
            

        if bgx2 < background.get_width() * -1:
            bgx2 = background.get_width() - 100
            

        if bgx == 0:
            bgx2 = background.get_width() * -1


        if health <= 0:
            bgx = 0
            bgy = 0
            dead(x,y,bgx,bgy)
            
        

        pygame.display.update()
        
    

        
                    
        


        
    
    








intro()
gameLoop()
pygame.quit()
quit()

