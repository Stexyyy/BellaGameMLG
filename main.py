import pygame
import Introcutscene

pygame.init()
pygame.display.set_caption("Bella game!") 
screen = pygame.display.set_mode((500, 500))
shootl = pygame.image.load('images/BellaShoot.jpg')
shoot = pygame.image.load('images/InverseShoot.jpg')
image2 = pygame.image.load('images/AFKBella.jpg')
imageR = pygame.image.load('images/BellaRight.jpg')
imageL = pygame.image.load('images/BellaLeft.jpg')
imageU = pygame.image.load('images/BellaUP.jpg')
imageD = pygame.image.load('images/BellaDown.jpg')
imageded = pygame.image.load('images/BellaDed.jpg')
# Bella is entirely Simons dog
WalkLeft = pygame.image.load('images/Cheebs.jpg')
WalkRight = pygame.image.load('images/inverted.jpg')
#first boss cheebs aka a modified version of cheems
FloatLeft = pygame.image.load('images/FatDogLeft.jpg')
FloatRight= pygame.image.load('images/FatDogRight.jpg')
#this is just a random picture of a corgi air paddling
Bash  = pygame.image.load('images/BellaStick3.png')
Bash2  = pygame.image.load('images/BellaStick2.png')
DogeLeft = pygame.image.load('images/dogeleft.jpg')
DogeRight = pygame.image.load('images/dogeright.jpg')
#this is meme of the 2010's doge, being the famous dog Kabosu in her funny random pose
Woof1 = pygame.image.load('images/woofLeft.jpg')
Woof2 = pygame.image.load('images/woofRight.jpg')
#This is funny epic meme gabe 
WhatsappR = pygame.image.load('images/WhatRight.jpg')
WhatsappL = pygame.image.load('images/WhatLeft.jpg')
#whatsapp dog meme
PunDogL = pygame.image.load('images/PunL.jpg')
PunDogR = pygame.image.load('images/PunR.jpg')
#funny pun dog
CheemsL = pygame.image.load('images/CheemsLeft.jpg')
CheemsR = pygame.image.load('images/CheemsRight.jpg')
#funny epic boss
WoodL = pygame.image.load('images/WoodL.png')
WoodR = pygame.image.load('images/WoodR.png')
#wood swords
StoneL = pygame.image.load('images/StoneL.png')
StoneR = pygame.image.load('images/StoneR.png')
#stone swords
IronL = pygame.image.load('images/IronL.png')
IronR = pygame.image.load('images/IronR.png')
#Iron swords
DiamondL = pygame.image.load('images/DiamondL.png')
DiamondR = pygame.image.load('images/DiamondR.png')
#diamond swords
NetherL = pygame.image.load('images/NetherL.png')
NetherR = pygame.image.load('images/NetherR.png')
#Netherite swords
clock = pygame.time.Clock()

#variables
xpos = 400
ypos = 100
direction = 0
fall = 0
isOnGround = False
Vx = 0 #player left/right speed
Vy = 0 #player up/down speed
playerhp = 100
cheebshp = 100
flyingcorgihp = 200
Dogehp = 400
Gabehp = 800
Appdoghp = 1600
Punhp = 3200
weapon = 1
Bossn = 1
Cheemhp = 6400
moners = 0
healthplus = 0
bought =False
#kevin wants to kidnapp me


class enemy:
    
    
    def __init__(self, cxpos, cypos):
        self.cxpos = cxpos
        self.cypos = cypos
        self.counter = 0
        self.vx = 2
        self.vy = 0
        self.isOnGround = False
    def draw(self, Bossn):
        if Bossn == 1:
            if self.vx > 0:
                screen.blit(WalkRight, (self.cxpos, self.cypos))
            if self.vx < 0:
                screen.blit(WalkLeft,(self.cxpos, self.cypos))
        if Bossn == 2:
                if self.vx > 0:
                    screen.blit(FloatRight, (self.cxpos, self.cypos- 100))
                if self.vx < 0:
                    screen.blit(FloatLeft,(self.cxpos, self.cypos-100))
        if Bossn == 3:
                if self.vx > 0:
                    screen.blit(DogeRight, (self.cxpos, self.cypos))
                if self.vx < 0:
                    screen.blit(DogeLeft,(self.cxpos, self.cypos))
        if Bossn == 4:
                if self.vx > 0:
                    screen.blit(Woof1, (self.cxpos, self.cypos))
                if self.vx < 0:
                    screen.blit(Woof2,(self.cxpos, self.cypos))
        if Bossn == 5:
                if self.vx > 0:
                    self.cxpos += 4
                    screen.blit(WhatsappR, (self.cxpos, self.cypos))
                if self.vx < 0:
                    self.cxpos -= 4
                    screen.blit(WhatsappL,(self.cxpos, self.cypos))
        if Bossn == 6:
                if self.vx > 0:
                    self.cxpos += 4
                    screen.blit(PunDogR, (self.cxpos, self.cypos))
                    
                if self.vx < 0:
                    self.cxpos -= 4
                    screen.blit(PunDogL,(self.cxpos, self.cypos))
        if Bossn == 7:
                if self.vx > 0:
                    self.cxpos +=5
                    screen.blit(CheemsR, (self.cxpos, self.cypos))
                    
                if self.vx < 0:
                    self.cxpos -=5
                    screen.blit(CheemsL,(self.cxpos, self.cypos))
                    


        #REFLECTION
        if self.cxpos < 0 or self.cxpos + 100 > 500:
          self.vx *= -1

        self.cxpos += self.vx
        self.cypos += self.vy

    def collision(self,x, y):

        if Bossn == 2:
            if y + 100 > self.cypos - 100 and x < self.cxpos + 100 and x + 100 > self.cxpos and y < self.cypos -10:
                return True
        else:
            if y + 100 > self.cypos and x < self.cxpos + 100 and x + 100 > self.cxpos and y < self.cypos + 100:
                return True
        
    def gravity(self, Bossn):

      #GRAVITY
        if Bossn == 1:
            if self.cypos > 500 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 500 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.2 #if not on ground, fall downwards
        if Bossn == 2:
            self.vy=0
        if Bossn == 3:
            if self.cypos > 500 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 500 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.2 #if not on ground, fall downwards
            if self.isOnGround == True:
                self.vy-=4
        if Bossn == 4:
            if self.cypos > 500 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 500 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.2 #if not on ground, fall downwards
            if self.isOnGround == True:
                self.vy-=10
        if Bossn == 5:
            if self.cypos > 500 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 500 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.2 #if not on ground, fall downwards
        if Bossn == 6:
            if self.cypos > 500 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 500 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.10 #if not on ground, fall downwards
            if self.isOnGround == True:
                self.vy-=6
        if Bossn == 7:
            if self.cypos > 500 - 100: #check if your feet are on the ground
                self.isOnGround = True
                self.cypos = 500 - 100
                self.vy = 0 #stot falling if on ground
            else:
                self.isOnGround = False
            if self.isOnGround == False:
                self.vy+=.2 #if not on ground, fall downwards
            if self.isOnGround == True:
                self.vy-=10
            

    def bash(self, stickx, sticky):
        if weapon == 1:
            if Bossn == 2:
                if sticky + 100 > self.cypos - 100 and stickx < self.cxpos + 100 and stickx + 100 > self.cxpos and sticky < self.cypos -10 :
                        return True
            else:
                if sticky + 100 > self.cypos and stickx < self.cxpos + 100 and stickx + 50 > self.cxpos and sticky < self.cypos + 50:
                    return True
        else:
            if Bossn == 2:
                if sticky + 150 > self.cypos - 100 and stickx < self.cxpos + 100 and stickx + 150 > self.cxpos and sticky < self.cypos -10 :
                        return True
            else:
                if sticky + 150 > self.cypos and stickx < self.cxpos + 100 and stickx + 100 > self.cxpos and sticky < self.cypos + 50:
                    return True
   
    def bashl(self, stickxl, sticky):
        if weapon == 1:
            if Bossn == 2:
                if sticky + 100 > self.cypos - 100 and stickxl < self.cxpos + 100 and stickxl + 100 > self.cxpos and sticky < self.cypos -10 :
                    return True
        
            else:
                if sticky + 50 > self.cypos and stickxl < self.cxpos + 100 and stickxl + 50 > self.cxpos and sticky < self.cypos + 100:
                    return True
        
        else:
            if Bossn == 2:
                if sticky + 150 > self.cypos - 100 and stickxl < self.cxpos + 100 and stickxl + 150 > self.cxpos and sticky < self.cypos -10 :
                    return True
        
            else:
                if sticky + 100 > self.cypos and stickxl < self.cxpos + 150 and stickxl + 100 > self.cxpos and sticky < self.cypos + 150:
                    return True
   
    def death (self, cheebshp):
        if cheebshp <= 0:
            return True
    def death2(self, flyingcorgihp):
        if flyingcorgihp <= 0:
            return True
    def death3(self, Dogehp):
            if Dogehp <= 0:
                return True
    def death4(self, Gabehp):
            if Gabehp <= 0:
                return True
    def death5(self, Appdoghp):
            if Appdoghp <= 0:
                return True
    def death6(self, Punhp):
            if Punhp <= 0:
                return True
    def death7(self, Cheemhp):
            if Cheemhp <= 0:
                return True

    
        

#hi
#hello
#da baby
#NOOOOOOOOOOOOOOOOOOo a
#trust the process
#i shall trust it

#Introcutscene.PlayCheems()

cheeb = enemy(250,250)

#game states
START = 0
PLAYING = 1
GAMEOVER = 2
SHOPPING = 3


#key presses
PLAY = 0
CONTINUE = 1
QUITG = 2
DED = 3
SHOP = 4
WEAPON = 5
HELTH = 6

game_state = START

pressed = [False, False, False, False, False, False, False]


font = pygame.font.SysFont("comicsansms", 16)
text1 = font.render("Start screen. Your goal is to defeat cheems and take all his cash to get rich!", True, (0, 228, 0))
textscren = font.render("Press p to play. Z and X to attack! Arrow keys to move!", True, (0, 228, 0))

text4 = font.render("Gameover! Press r to continue or q to quit! ", True, (0, 228, 0))

textshop = font.render("Press s to go to the shop", True, (0, 228, 0))

textinshop = font.render("Press r to go back to the game", True, (0, 228, 0))

if bought == False:
    textlel = font.render("Thanks for coming!", True, (0, 228, 0))
if bought == True:
    textlel = font.render("Thanks for buying!", True, (0, 228, 0))

textinshop1 = font.render("Pay 10 shmackaroonies to increase your health ( click h to buy)", True, (0, 228, 0))


doExit = False

while not doExit:
    clock.tick(60)

#sprite keys---------------------------------------------------------
    text2 = font.render("Player hp is ", True, (0, 228, 0))
    text3 = font.render(str(int(playerhp)), 1, (0,200,200))
    if Bossn == 1:
        text5 = font.render("Cheebs the destroyer hp is ", True, (0, 228, 0))
        text6 = font.render(str(int(cheebshp)), 1, (0,200,200))
    elif Bossn == 2:
        text5 = font.render("Evil flying corgi hp is ", True, (0, 228, 0))
        text6 = font.render(str(int(flyingcorgihp)), 1, (0,200,200))
    elif Bossn == 3:
       text5 = font.render("Nefarious Doge hp is ", True, (0, 228, 0))
       text6 = font.render(str(int(Dogehp)), 1, (0,200,200))
    elif Bossn == 4:
       text5 = font.render("Angel of Doom Gabe hp is", True, (0, 228, 0))
       text6 = font.render(str(int(Gabehp)), 1, (0,200,200))
    elif Bossn == 5:
       text5 = font.render("Appdog the funny hp is", True, (0, 228, 0))
       text6 = font.render(str(int(Appdoghp)), 1, (0,200,200))
    elif Bossn == 6:
       text5 = font.render("Pun dog the equivoque hp is", True, (0, 228, 0))
       text6 = font.render(str(int(Punhp)), 1, (0,200,200))
    elif Bossn == 7:
       text5 = font.render("Cheems the cheese dog hp is", True, (0, 228, 0))
       text6 = font.render(str(int(Cheemhp)), 1, (0,200,200))
    
    textsh = font.render("Money:", True, (0, 228, 0))
    textsh2 = font.render(str(int(moners)), 1, (0,200,200))

    if weapon == 1:
        textlol = font.render("To buy Wooden sword is 100 money (click w to buy!)", True, (0, 228, 0))
    if weapon == 2:
        textlol = font.render("To buy Stone sword is 500 money (click w to buy!)", True, (0, 228, 0))
    if weapon == 3:
        textlol = font.render("To buy Iron sword is 1000 money (click w to buy!)", True, (0, 228, 0))
    if weapon == 4:
        textlol = font.render("To buy Diamond sword is 2000 money (click w to buy!)", True, (0, 228, 0))
    if weapon == 5:
        textlol = font.render("To buy Netherite sword is 4000 money (click w to buy!)", True, (0, 228, 0))
    if weapon == 6:
        textlol = font.render("You bought all the swords! good job! now go beat up cheems!", True, (0, 288, 0))

    weaponx = xpos + 95
    weapony = ypos + 5
    weaponlx = xpos - 45
#input/output section
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        direction = 0
        Vx=-2

    elif keys[pygame.K_RIGHT]:
        Vx=+2
    
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if isOnGround == True: #comment this to ensable double jumping
            Vy -= 15 #impact velocity instead

    xpos+= Vx
    ypos+= Vy

    #GRAVITY
    if ypos > 500 - 100: #check if your feet are on the ground
        isOnGround = True
        fall = 0
        ypos = 500 - 100
        Vx = 0 #stot falling if on ground
        y = 0
    else:
        isOnGround = False
    if isOnGround == False:
        fall = 1
        Vy+=.2 #if not on ground, fall downwards





    if cheeb.collision(xpos, ypos):
        playerhp -= (1 * Bossn)
        


  #----------------------------------------------------------------------

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.quit:
            doExit = True


    keys = pygame.key.get_pressed() 
    if keys[pygame.K_p]:
        pressed[PLAY]=True
    else:
        pressed[PLAY]=False
    
    if keys[pygame.K_r]:
        pressed[CONTINUE]=True
    else:
        pressed[CONTINUE]=False
    
    if keys[pygame.K_q]:
        pressed[QUITG]=True
    else:
        pressed[QUITG]=False

    if keys[pygame.K_s]:
            pressed[SHOP]=True
    else:
            pressed[SHOP]=False
    
    if keys[pygame.K_w]:
            pressed[WEAPON]=True
    else:
            pressed[WEAPON]=False

    if keys[pygame.K_h]:
            pressed[HELTH]=True
    else:
            pressed[HELTH]=False

    
    
    if playerhp < 0:
      pressed[DED]=True
    else:
      pressed[DED]=False



    if game_state == START:
        if pressed[PLAY] == True:
            game_state = PLAYING


    if game_state == PLAYING:
        if pressed[DED] == True:
            game_state = GAMEOVER

    if game_state == GAMEOVER:
        if pressed[QUITG] == True:
            doExit = True

    if game_state == GAMEOVER:
        if pressed[CONTINUE] == True:
            playerhp = 100 + healthplus
            Bossn = 1
            cheebshp = 100
            flyingcorgihp = 200
            Dogehp = 400
            Gabehp = 800
            Appdoghp = 1600
            Punhp = 3200
            Cheemhp = 6400
            
            game_state = PLAYING

    if game_state == GAMEOVER:
        if pressed[SHOP] == True:
            game_state = SHOPPING
    
    if game_state == SHOPPING:
        if pressed[CONTINUE] == True:
            playerhp = 100 + healthplus
            Bossn = 1
            cheebshp = 100
            flyingcorgihp = 200
            Dogehp = 400
            Gabehp = 800
            Appdoghp = 1600
            Punhp = 3200
            Cheemhp = 6400
            
            game_state = PLAYING

        if pressed[WEAPON] == True:
            if weapon == 1:
                if moners >= 100:
                    moners -= 100
                    weapon = weapon + 1
                    bought = True
            if weapon == 2:
                if moners >= 500:
                    moners -= 500
                    weapon = weapon + 1
                    bought = True
            if weapon == 3:
                if moners >= 1000:
                    moners -= 1000
                    weapon = weapon + 1
                    bought = True
            if weapon == 4:
                if moners >= 2000:
                    moners -= 2000
                    weapon = weapon + 1
                    bought = True
            if weapon == 5:
                if moners >= 4000:
                    moners -= 4000
                    weapon = weapon + 1
                    bought = True
        if pressed [HELTH] == True:
            if moners >= 10:
                moners -= 10
                healthplus += 10
                bought = True
        
       
       

        
        
            
    



    screen.fill((5, 5, 100))

    pygame.draw.rect(screen, (255, 255, 255), (350, 200, 20, 20), 1)

    #keys animation-----------------------------------
    
    
   


    if game_state == START:
        screen.fill((0,0,180))
        screen.blit(text1,(50, 100))
        screen.blit(textscren, (100,120))

    if game_state == PLAYING:
        screen.fill((0,0,0))
        screen.blit(text2,(100,100))
        screen.blit(text3,(165,100))
        screen.blit(text5,(100,135))
        if Bossn == 1:
            screen.blit(text6,(243,135))
        if Bossn == 2:
            screen.blit(text6,(215,135))
        if Bossn == 3:
            screen.blit(text6,(215,135))
        if Bossn == 4:
            screen.blit(text6,(250,135))
        if Bossn == 5:
            screen.blit(text6,(230,135))
        if Bossn == 6:
            screen.blit(text6,(255,135))
        if Bossn == 7:
            screen.blit(text6,(265,135))

        if keys[pygame.K_x]:
            screen.blit(shoot, (xpos,ypos))
            if weapon == 1:
                screen.blit(Bash, (weaponx, weapony))
            if weapon == 2:
                screen.blit(WoodR,(weaponx, weapony))
            if weapon == 3:
                screen.blit(StoneR,(weaponx, weapony))
            if weapon == 4:
                screen.blit(IronR,(weaponx, weapony))
            if weapon == 5:
                screen.blit(DiamondR,(weaponx, weapony))
            if weapon == 6:
                screen.blit(NetherR,(weaponx, weapony))
            if cheeb.bash(weaponx,weapony):
                if Bossn == 1:
                    cheebshp -= (1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 2:
                    flyingcorgihp -=(1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 3:
                    Dogehp -=(1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 4:
                    Gabehp -= (1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 5:
                    Appdoghp -=(1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 6:
                    Punhp -=(1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 7:
                    Cheemhp -= (1 * weapon)
                    moners += (1 * weapon)

       # deez
        elif keys[pygame.K_z]:
            screen.blit(shootl, (xpos,ypos))
            if weapon == 1:
                screen.blit(Bash2, (weaponlx, weapony))
            if weapon == 2:
                screen.blit(WoodL,(weaponlx - 35, weapony))
            if weapon == 3:
                screen.blit(StoneL,(weaponlx- 35, weapony))
            if weapon == 4:
                screen.blit(IronL,(weaponlx- 35, weapony))
            if weapon == 5:
                screen.blit(DiamondL,(weaponlx- 35, weapony))
            if weapon == 6:
                screen.blit(NetherL,(weaponlx- 35, weapony))
            if cheeb.bashl(weaponlx,weapony):
                if Bossn == 1:
                   cheebshp -= (1 * weapon)
                   moners +=(1 * weapon)
                if Bossn == 2:
                   flyingcorgihp -= (1 *weapon)
                   moners += (1 * weapon)
                if Bossn == 3:
                    Dogehp -= (1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 4:
                    Gabehp -= (1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 5:
                    Appdoghp -=(1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 6:
                    Punhp -= (1 * weapon)
                    moners += (1 * weapon)
                if Bossn == 7:
                    Cheemhp -= (1 * weapon)
                    moners += (1 * weapon)


        elif keys[pygame.K_RIGHT]:
          screen.blit(imageR, (xpos,ypos))#swag beller
        elif keys[pygame.K_LEFT]:
            screen.blit(imageL, (xpos,ypos))

        elif keys[pygame.K_UP]:
            screen.blit(imageU, (xpos,ypos))
        elif fall == 1:
            screen.blit(imageD, (xpos,ypos))
        else:
            screen.blit(image2, (xpos,ypos))
        cheeb.draw(Bossn)
        cheeb.gravity(Bossn)
        if cheeb.death(cheebshp):
            Bossn = 2
        if cheeb.death2(flyingcorgihp):
            Bossn = 3
        if cheeb.death3(Dogehp):
            Bossn = 4
        if cheeb.death4(Gabehp):
            Bossn = 5
        if cheeb.death5(Appdoghp):
            Bossn = 6
        if cheeb.death6(Punhp):
            Bossn = 7
        if cheeb.death7(Cheemhp):
            Introcutscene.PlayVictory()
            



    
    if game_state == GAMEOVER:
        screen.fill((0,0,0))
        print("You are dead")
        screen.blit(imageded,(250,350))
        screen.blit(text4,(100,100))
        screen.blit(textshop,(125,125))
        

    if game_state == SHOPPING:
        screen.fill((0,0,0))
        screen.blit(textinshop, (100, 200))
        screen.blit(textsh, (100, 225))
        screen.blit(textsh2, (142, 225))
        screen.blit(textlol, (100, 300))
        screen.blit(textinshop1, (100, 250))
        screen.blit(textlel, (300, 100))





    
    


    pygame.display.flip() 


pygame.quit()