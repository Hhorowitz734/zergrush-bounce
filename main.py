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

    player.blit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.movements[event.key] = True
        if event.type == pygame.KEYUP:
            player.movements[event.key] = False
    
    player.handle_movements()
    
    pygame.display.update()

pygame.quit()
