import pygame
import player
import os
clear = lambda: os.system('cls')
clear()

pygame.init()

SCREEN_WIDTH = 800
SCEEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCEEN_HEIGHT))
p = player.Player(0,0,50,50,(0, 0, 255))

run = True
while run:

    screen.fill((0, 0, 0))
    
    p.update(screen)
    p.render(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()