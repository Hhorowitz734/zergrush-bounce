#Importing modules
import pygame
from random import randint
import math

class Player():
    

    def __init__(self, screen, lives = 3):
        #Visual attributes
        playImgLoad = pygame.image.load("player.png")
        self.player = pygame.transform.scale(playImgLoad, (15, 15))


        #Game attributes
        self.lives = lives
        self.speed = 5
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


    def blit(self, hurt = False): #Draws the player rectangle
        self.screen.blit(self.player, (self.xpos, self.ypos))
        if hurt:
            eraserect = pygame.Rect(self.xpos, self.ypos, 15, 15)
            pygame.draw.rect(self.screen, (255, 0, 0), eraserect)

    def handle_movements(self, bulletsclass):
        if self.movements[pygame.K_w]:
            self.ypos -= self.speed
        if self.movements[pygame.K_a]:
            self.xpos -= self.speed
        if self.movements[pygame.K_s]:
            self.ypos += self.speed
        if self.movements[pygame.K_d]:
            self.xpos += self.speed
        if self.movements[pygame.MOUSEBUTTONDOWN]:
            self.shoot(bulletsclass)
            self.movements[pygame.MOUSEBUTTONDOWN] = False
    
    def shoot(self, bulletsclass):
        x, y = pygame.mouse.get_pos()
        bulletsclass.bulletlist.append(Bullet(self, x, y))
        
    def erase(self):
        eraserect = pygame.Rect(self.xpos, self.ypos, 15, 15)
        pygame.draw.rect(self.screen, (0, 0, 0), eraserect)
    
    def get_rect(self):
        return pygame.Rect(self.xpos, self.ypos, 15, 15)

    
    def hit_by_bullet(self, hits):
        self.lives -= hits #Later take away a heart icon from top of screen
        if hits > 0:
            return True #We will implement logic for this in the main file
        return False
        


class Bullets():

    def __init__(self):
        self.bulletlist = []
    
    def handle_all(self):
        for bullet in self.bulletlist:
            bullet.erase()
            bullet.move()
            bullet.blit()



    def num_collisions(self, player):
        hits = 0
        for bullet in self.bulletlist:
            if pygame.Rect.colliderect(bullet.get_rect(), player.get_rect()):
                hits += 1
        x = player.hit_by_bullet(hits)
        return x




class Bullet():

    def __init__(self, player, targetx, targety):
        #Change these later to reflect direction
        self.xpos = player.xpos + 8
        self.ypos = player.ypos + 8
        self.screen = player.screen

        self.angle = math.atan2(targety - player.ypos, targetx - player.xpos)
        
        self.dx = math.cos(self.angle) * 10 + (randint(-1, 1) / 5)
        self.dy = math.sin(self.angle) * 10 + (randint(-1, 1) / 5)

        self.screen_width, self.screen_height = self.screen.get_size()

        #Change these later to real bullet image
        bulletImgLoad = pygame.image.load("player.png")
        self.bullet = pygame.transform.scale(bulletImgLoad, (5, 5))
    
    def move(self):
        self.xpos += self.dx
        self.ypos += self.dy
        if self.xpos < 0 or self.xpos >= self.screen_width:
            self.dx = -self.dx
        if self.ypos < 0 or self.ypos >= self.screen_height:
            self.dy = -self.dy
    
    def blit(self):
        self.screen.blit(self.bullet, (self.xpos, self.ypos))
    
    def erase(self):
        eraserect = pygame.Rect(self.xpos, self.ypos, 5, 5)
        pygame.draw.rect(self.screen, (0, 0, 0), eraserect)
    
    def get_rect(self):
        return pygame.Rect(self.xpos, self.ypos, 5, 5)


