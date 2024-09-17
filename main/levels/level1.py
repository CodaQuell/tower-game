import pygame
from pygame.locals import *
import random
import tkinter
from classes.player import player

from classes.playerClass import *
from classes.enemyClass import *
from classes.enemyClass import *
from classes.sheepClass import * 
from classes.wallClass import *
from classes.newLevelClass import *

from functions.spriteGroups import *

app = tkinter.Tk()
W = app.winfo_screenwidth()
H = app.winfo_screenheight()

#renders the entities for each level
def level1():
  #entry points
  upLevelPoint = newLevel((1900,540),1)

  walltop = Wall((20,20),W*2,40)
  wallbottom = Wall((20,H-20),W*2,40)
  wallleft = Wall((20,20),40,H*2)
  wallright1 = Wall((W-20,20),40,H-80)
  wallright2 = Wall((W-20,H),40,H-40)


  #all playes/entities
  spriteGroup1.add(upLevelPoint)
  spriteGroup1.add(player)



  #walls or solid blocks
  spriteGroup3.add(walltop)
  spriteGroup3.add(wallbottom)
  spriteGroup3.add(wallleft)
  spriteGroup3.add(wallright1)
  spriteGroup3.add(wallright2)


  #entry/exit points
  spriteGroup4.add(upLevelPoint)

  spriteGroup5.add(walltop)
  spriteGroup5.add(wallbottom)
  spriteGroup5.add(wallleft)
  spriteGroup5.add(wallright1)
  spriteGroup5.add(wallright2) 
  spriteGroup5.add(upLevelPoint)