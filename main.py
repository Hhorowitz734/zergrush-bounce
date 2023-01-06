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
bullets = Bullets()

frame = -1


#Game loop
while running:
    player.erase()
    player.handle_movements(bullets)
    player.blit()
    if bullets.num_collisions(player):
        frame = 0
    if frame != -1:
        player.blit(True)
        player.speed = 2
        frame += 1
    if frame == 20:
        frame = -1
        player.speed = 5


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.movements[event.key] = True
        if event.type == pygame.KEYUP:
            player.movements[event.key] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.movements[pygame.MOUSEBUTTONDOWN] = True
    
    bullets.handle_all()
    if bullets.num_collisions(player) > 0:
        print('HIT!')
    
    pygame.display.update()

pygame.quit()
