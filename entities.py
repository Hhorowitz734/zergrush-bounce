#Importing modules
import pygame
from random import randint, choice
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
        if self.xpos > 485:
            self.xpos = 485
        if self.xpos < 0:
            self.xpos = 0
        if self.ypos > 485:
            self.ypos = 485
        if self.ypos < 0:
            self.ypos = 0
        
    
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



class Zergs():

    def __init__(self, player, screen):
        self.zerglist = []
        self.player = player
        self.screen = screen
        self.cnum = 10
        self.zergspeed = 1

    def handle_all(self):
        for zerg in self.zerglist:
            zerg.erase()
            zerg.move()
        for zerg in self.zerglist:   
            zerg.blit()
        if not self.zerglist:
            self.cnum += 5
            self.zergspeed += .1
            self.generate(self.cnum)
    
    def generate(self, num):
        self.zerglist = [Zerg(self.player, self.screen, self.zergspeed) for n in range(num)]
    
    def kill_check(self, bullets):
        for bullet in bullets.bulletlist:
            for zerg in self.zerglist:
                if pygame.Rect.colliderect(zerg.get_rect(), bullet.get_rect()):
                    zerg.erase()
                if pygame.Rect.colliderect(zerg.get_rect(), self.player.get_rect()):
                    pygame.quit() #Implement logic to move to dead screen here
            self.zerglist = [zerg for zerg in self.zerglist if not pygame.Rect.colliderect(zerg.get_rect(), bullet.get_rect())]



class Zerg():

    def __init__(self, player, screen, speed):
        self.screen = screen
        whichside = randint(0, 3)
        if whichside == 0:  # Top of the screen
            self.xpos = randint(0, 500)
            self.ypos = -50
        elif whichside == 1:  # Right side of the screen
            self.xpos = 550
            self.ypos = randint(0, 500)
        elif whichside == 2:  # Bottom of the screen
            self.xpos = randint(0, 500)
            self.ypos = 550
        else:  # Left side of the screen
            self.xpos = -50
            self.ypos = randint(0, 500)
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.player = player
        self.zerg_hitbox = pygame.Rect(self.xpos, self.ypos, 20, 20) 
        self.speed = speed
    
    def blit(self):
        pygame.draw.circle(self.screen, self.color, (self.xpos, self.ypos), 6)
    
    def erase(self):
        rect_x = self.xpos - 7
        rect_y = self.ypos - 7
        rect_width = 14
        rect_height = 14
        pygame.draw.rect(self.screen, (0,0,0), (rect_x, rect_y, rect_width, rect_height), 0)
    
    def move(self):
        self.angle = math.atan2(self.player.ypos - self.ypos, self.player.xpos - self.xpos)
        
        dx = math.cos(self.angle) * self.speed
        dy = math.sin(self.angle) * self.speed

        self.xpos += dx
        self.ypos += dy
    
    def get_rect(self):
        return pygame.Rect(self.xpos, self.ypos, 14, 14)
    
