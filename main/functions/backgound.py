# import 3rd part libs
import tkinter
import pygame
from pygame.locals import *

#getting screen size
app = tkinter.Tk()
W = app.winfo_screenwidth()
H = app.winfo_screenheight()

#init screen
screen = pygame.display.set_mode((W,H))

#images path
image_list=[]
current_image = 0
image_list.append("C:\\Users\\josso\Downloads\\tower-game-main\\tower-game-main\\main\\assets\\background0.png")
image_list.append("C:\\Users\\josso\Downloads\\tower-game-main\\tower-game-main\\main\\assets\\background1.png")
image_list.append("C:\\Users\\josso\Downloads\\tower-game-main\\tower-game-main\\main\\assets\\background2.png")


#loads selected image from image path
def background(image,W,H,screen):
    #loads the image
    image = pygame.image.load(image_list[current_image])
    #scales the image to fit the screen, even tho all back ground art will be made for 16:9 ratio
    scaled_image = pygame.transform.scale(image, (W, H))
    #draws the the screen
    screen.blit(scaled_image, (0, 0))

def next_image(image,W,H,screen):
    global current_image
    if len(image_list)>current_image+1:
        current_image +=1
        
    background(image,W,H,screen)

def prev_image(image,W,H,screen):
    global current_image
    if len(image_list)>current_image:
        current_image -=1
    background(image,W,H,screen)

