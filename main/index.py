#3rd party libaries import
import sys

import pygame
from pygame.locals import *

import random
from random import *

from classes.playerClass import Player
from classes.enemyClass import Enemy
from classes.wallClass import Wall

from win32api import GetSystemMetrics


#init pygame
pygame.init()

#geting tick rate for the game time
fps = 60
fpsClock = pygame.time.Clock()
 
#getting height and width for the game window
W = GetSystemMetrics(0)
H = GetSystemMetrics(1)
screen = pygame.display.set_mode((W,H))

#init player from Player class
player = Player()
wall = Wall((randint(20,GetSystemMetrics(0)),randint(20,GetSystemMetrics(1))))

#create sprite group
spriteGroup1 = pygame.sprite.Group()

#add player to sprite group
spriteGroup1.add(player)
spriteGroup1.add(wall)


 
# Game loop
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():

    #makes it so you can either press esc or the x button to quit
    if event.type == QUIT or event.type == KEYDOWN:
      #press esc to exit pygame
      if event.key == K_ESCAPE:

        pygame.quit()
        sys.exit()

  keys = pygame.key.get_pressed()
  for sprite in spriteGroup1:
      sprite.update(keys)

  for sprite in spriteGroup1:
      screen.blit(sprite.surface,sprite.rect)
  

  #updates the screen ever 60 ticks. This is set in fpsClock
  pygame.display.update()
  fpsClock.tick(fps)

