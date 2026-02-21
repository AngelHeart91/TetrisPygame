import pygame, sys

from game.grid import Grid
from game.tetromino import Tetromino

pygame.init()
screen = pygame.display.set_mode((500, 600))    #screen display size
pygame.display.set_caption('Tetrice')

game_on = True
grid = Grid()
tetromino = Tetromino()

while game_on:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            sys.exit()
    screen.fill('#8DB0B5')
    grid.draw_grid(screen)
    tetromino.draw_tetromino(screen, grid.cell_size)
    pygame.display.update()