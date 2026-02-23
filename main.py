from struct import pack_into

import pygame, sys

from game.grid import Grid
from game.tetromino import Tetromino

pygame.init()
screen = pygame.display.set_mode((500, 600))    #screen display size
pygame.display.set_caption('Tetrice')
fps = pygame.time.Clock()

game_on = True
grid = Grid()
tetromino = Tetromino()

print(len(tetromino.current))

fall_timer = 0
fall_delay = normal_delay = 500    # en millisecondes
fast_fall_delay = 150

while game_on:
    dt = fps.tick(60)
    keys = pygame.key.get_pressed()
    screen.fill('#8DB0B5')
    grid.draw_grid(screen)
    tetromino.draw_tetromino(screen, grid.cell_size)
    # add a tempo for tetromino fall down more slowly

    fall_timer += dt
    while fall_timer >= fall_delay:
        if grid.tetromino_position(tetromino, tetromino.x, tetromino.y + 1):
            tetromino.move_down()
        else:
            grid.lock_tetromino(tetromino)
            tetromino = Tetromino()
        fall_timer -= fall_delay
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
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                old_rotation = tetromino.rotation
                old_current = tetromino.current
                tetromino.rotate()
                if not grid.tetromino_position(tetromino, tetromino.x, tetromino.y):
                    tetromino.rotation = old_rotation
                    tetromino.current = old_current
            elif event.key == pygame.K_SPACE:
                while grid.tetromino_position(tetromino, tetromino.x, tetromino.y + 1):
                    tetromino.move_down()
    pygame.display.update()