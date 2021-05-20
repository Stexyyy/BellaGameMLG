import pygame
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800, 600))

beller = pygame.image.load ("images/AFKBella.jpg")
broke = pygame.image.load("images/BellaShoot.jpg")
schmoney = pygame.image.load("images/Schmoney.jpg")
cheeser = beller.get_rect(topleft = (200,280))
moner = schmoney.get_rect(topleft= (100,280))
bruher = schmoney.get_rect(topleft= (100,280))

def PlayCheems():

  font = pygame.font.SysFont('calibri.ttf', 38)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('This dog has riches and fame', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(beller, cheeser)
      screen.blit(text, (0,100))
      pygame.display.flip()
      time.sleep(20 / 1000)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('This dog has riches and fame', True, (0,0,0), (255,255,255))
      text2 = font.render('But unfortuntely', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(beller, cheeser)
      screen.blit(text, (0,100))
      screen.blit(text2, (0,200))
      pygame.display.flip()
      time.sleep(20 / 1000)
  #this fades both from black to white
  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('This dog has riches and fame', True, (0+x,0+x,0+x), (255,255,255))
      text2 = font.render('But unfortuntely', True, (0+x,0+x,0+x), (255,255,255))
      screen.blit(beller, cheeser)
      screen.blit(text, (0,100))
      screen.blit(text2, (0,200))
      pygame.display.flip()
      time.sleep(10 / 1000)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('Shes broke!', True, (0,0,0), (255,255,255))
      screen.blit(text, (0,100))
      screen.blit(broke, cheeser)
      pygame.display.flip()
      time.sleep(20 / 1000)



def PlayVictory():

  font = pygame.font.SysFont('calibri.ttf', 38)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('You beat Cheems!', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(beller, cheeser)
      screen.blit(text, (0,100))
      pygame.display.flip()
      time.sleep(20 / 1000)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('You beat Cheems!', True, (0,0,0), (255,255,255))
      text2 = font.render('Congradulations!', True, (255-x,255-x,255-x), (255,255,255))
      screen.blit(beller, cheeser)
      screen.blit(text, (0,100))
      screen.blit(text2, (0,200))
      pygame.display.flip()
      time.sleep(20 / 1000)
  #this fades both from black to white
  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('You beat Cheems!', True, (0+x,0+x,0+x), (255,255,255))
      text2 = font.render('Congradulations!', True, (0+x,0+x,0+x), (255,255,255))
      screen.blit(beller, cheeser)
      screen.blit(text, (0,100))
      screen.blit(text2, (0,200))
      pygame.display.flip()
      time.sleep(10 / 1000)

  for x in range(255):
      screen.fill((255, 255, 255))
      text = font.render('Shes rich!', True, (0,0,0), (255,255,255))
      screen.blit(text, (0,100))
      screen.blit(schmoney, moner)
      screen.blit(schmoney, bruher)
      screen.blit(broke, cheeser)
      pygame.display.flip()
      time.sleep(20 / 100)
