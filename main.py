import pygame, sys

from game.grid import Grid
from game.tetromino import Tetromino

pygame.init()
screen = pygame.display.set_mode((500, 600))    #screen display size
pygame.display.set_caption('Tetrice')
clock = pygame.time.Clock()

game_on = True
grid = Grid()
tetromino = Tetromino()

last_fall_time = 0
fall_delay = 300  # en millisecondes

while game_on:
    clock.tick(60)
    screen.fill('#8DB0B5')
    grid.draw_grid(screen)
    tetromino.draw_tetromino(screen, grid.cell_size)
    # add a tempo for tetromino fall down more slowly
    current_time = pygame.time.get_ticks()
    if current_time - last_fall_time > fall_delay:
        if grid.tetromino_position(tetromino, tetromino.x, tetromino.y + 1):
            tetromino.move_down()
        last_fall_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if grid.tetromino_position(tetromino, tetromino.x - 1, tetromino.y):
                    tetromino.move_left()
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if grid.tetromino_position(tetromino, tetromino.x + 1, tetromino.y):
                    tetromino.move_right()

    pygame.display.update()