import pygame, sys

from game.Grid import Grid

pygame.init()
screen = pygame.display.set_mode((500, 600))    #screen display size
pygame.display.set_caption('Tetrice')

game_on = True
grid = Grid()

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            sys.exit()
    screen.fill('#8DB0B5')
    grid.draw_grid(screen)
    pygame.display.update()