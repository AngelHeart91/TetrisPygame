import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 600))    #screen display size

game_on = True

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            sys.exit()

    pygame.display.update()