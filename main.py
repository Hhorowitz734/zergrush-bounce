#Import modules
import pygame
from entities import *

#Module controls
pygame.init()


#Game variables
running = True
screen = pygame.display.set_mode((500, 500))

#Entity variables
player = Player(screen)



#Game loop
while running:
    player.erase()
    player.handle_movements()
    player.blit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.movements[event.key] = True
        if event.type == pygame.KEYUP:
            player.movements[event.key] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.movements[pygame.MOUSEBUTTONDOWN] = True
    
    for bullet in player.bullets:
        bullet.erase()
        bullet.move()
        bullet.blit()
    
    
    pygame.display.update()

pygame.quit()
