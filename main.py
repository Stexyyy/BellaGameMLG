import pygame

pygame.init()
pygame.display.set_caption("Bella game!") 
screen = pygame.display.set_mode((500, 500))
shootl = pygame.image.load('BellaShoot.jpg')
shoot = pygame.image.load('InverseShoot.jpg')
image2 = pygame.image.load('AFKBella.jpg')
imageR = pygame.image.load('BellaRight.jpg')
imageL = pygame.image.load('BellaLeft.jpg')
imageU = pygame.image.load('BellaUP.jpg')
imageD = pygame.image.load('BellaDown.jpg')
imageded = pygame.image.load('BellaDed.jpg')
WalkLeft = pygame.image.load('Cheebs.jpg')
WalkRight = pygame.image.load('inverted.jpg')
FloatLeft = pygame.image.load('FatDogLeft.jpg')
FloatRight= pygame.image.load('FatDogRight.jpg')
Bash  = pygame.image.load('BellaStick3.png')
Bash2  = pygame.image.load('BellaStick2.png')
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
isdead = False
Bossn = 1



class enemy:
    
    
    def __init__(self, cxpos, cypos):
        self.cxpos = cxpos
        self.cypos = cypos
        self.alive = True
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


        #REFLECTION
        if self.cxpos < 0 or self.cxpos + 100 > 500:
          self.vx *= -1

        self.cxpos += self.vx
        self.cypos += self.vy

    def collision(self,x, y):
        if Bossn == 1:
            if y + 100 > self.cypos and x < self.cxpos + 100 and x + 100 > self.cxpos and y < self.cypos + 100:
                return True
        if Bossn == 2:
            if y + 100 > self.cypos - 100 and x < self.cxpos + 100 and x + 100 > self.cxpos and y < self.cypos -10:
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

    def bash(self, stickx, sticky):
        if Bossn == 1:
            if sticky + 100 > self.cypos and stickx < self.cxpos + 100 and stickx + 50 > self.cxpos and sticky < self.cypos + 50:
                return True
        if Bossn == 2:
          if sticky + 100 > self.cypos - 100 and stickx < self.cxpos + 100 and stickx + 100 > self.cxpos and sticky < self.cypos -10 :
                return True
   
    def bashl(self, stickxl, sticky):
        if Bossn == 1:
          if sticky + 50 > self.cypos and stickxl < self.cxpos + 100 and stickxl + 50 > self.cxpos and sticky < self.cypos + 100:
              return True

        if Bossn == 2:
          if sticky + 100 > self.cypos - 100 and stickxl < self.cxpos + 100 and stickxl + 100 > self.cxpos and sticky < self.cypos -10 :
              return True
   
    def death (self, cheebshp):
        if cheebshp <= 0:
            self.alive = False
            return True
        




cheeb = enemy(250,250)

#game states
START = 0
PLAYING = 1
GAMEOVER = 2


#key presses
PLAY = 0
CONTINUE = 1
QUITG = 2
DED = 3

game_state = START

pressed = [False, False, False, False]


font = pygame.font.SysFont("comicsansms", 16)
text1 = font.render("start screen. press p to play.", True, (0, 228, 0))

text4 = font.render("Gameover! Press r to continue or q to quit! ", True, (0, 228, 0))

doExit = False

while not doExit:
    clock.tick(60)

#sprite keys---------------------------------------------------------
    text2 = font.render("Player hp is ", True, (0, 228, 0))
    text3 = font.render(str(int(playerhp)), 1, (0,200,200))
    text5 = font.render("Enemy hp is ", True, (0, 228, 0))
    text6 = font.render(str(int(cheebshp)), 1, (0,200,200))
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
        playerhp -=.5 
        


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
            playerhp = 100
            cheebhp = 100
            isdead = False
            game_state = PLAYING
            
    



    screen.fill((5, 5, 100))

    pygame.draw.rect(screen, (255, 255, 255), (350, 200, 20, 20), 1)

    #keys animation-----------------------------------
    
    
   


    if game_state == START:
        screen.fill((0,0,180))
        screen.blit(text1,(100, 100))

    if game_state == PLAYING:
        screen.fill((0,0,0))
        screen.blit(text2,(100,100))
        screen.blit(text3,(165,100))
        screen.blit(text5,(100,135))
        screen.blit(text6,(165,135))


        if keys[pygame.K_x]:
            screen.blit(shoot, (xpos,ypos))
            screen.blit(Bash, (weaponx, weapony))
            if cheeb.bash(weaponx,weapony):
                cheebshp -=.5


        elif keys[pygame.K_z]:
            screen.blit(shootl, (xpos,ypos))
            screen.blit(Bash2, (weaponlx, weapony))
            if cheeb.bashl(weaponlx,weapony):
                cheebshp -=.5


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
            



    
    if game_state == GAMEOVER:
        screen.fill((0,0,0))
        print("You are dead")
        screen.blit(imageded,(250,350))
        screen.blit(text4,(100,100))





    
    


    pygame.display.flip() 


pygame.quit()