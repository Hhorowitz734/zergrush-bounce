#Importing modules
import pygame
import time
import math

class Player():
    

    def __init__(self, screen, lives = 3):
        #Visual attributes
        playImgLoad = pygame.image.load("player.png")
        self.player = pygame.transform.scale(playImgLoad, (15, 15))


        #Game attributes
        self.lives = lives
        self.screen = screen 

        #Positional and rotational attributes
        self.xpos = screen.get_width() / 2
        self.ypos = screen.get_height() / 2
        self.rotation = 0   

        self.movements = {
            pygame.K_w: False,
            pygame.K_a: False,
            pygame.K_s: False,
            pygame.K_d: False,
            pygame.K_SPACE: False,
            pygame.MOUSEBUTTONDOWN: False
        }



    def blit(self): #Draws the player rectangle
        self.screen.blit(self.player, (self.xpos, self.ypos))

    def handle_movements(self):
        erasex = self.xpos
        erasey = self.ypos

        if self.movements[pygame.K_w]:
            self.ypos -= 5
        if self.movements[pygame.K_a]:
            self.xpos -= 5
        if self.movements[pygame.K_s]:
            self.ypos += 5
        if self.movements[pygame.K_d]:
            self.xpos += 5
        if self.movements[pygame.MOUSEBUTTONDOWN]:
            print('Insert shooting logic here') #Insert shooting logic here
        
    def erase(erasex, erasey):
        pass #Create a rect in the shape of the player, and then blit it in black on the screen


    
    def rotate_to_mouse(self, mousex, mousey): #Rotates player position to mouse coords
        pass



