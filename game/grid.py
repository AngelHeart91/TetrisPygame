import pygame

class Grid:
    def __init__(self):
        self.nb_rows = 20
        self.nb_cols = 11
        self.cell_size = 30
        self.cells = [[0 for _ in range(self.nb_cols)] for _ in range(self.nb_rows)]

    def draw_grid(self,screen):
        for i in range (0, self.nb_rows):
            for j in range (0, self.nb_cols):
                rect_grid = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, '#1A388A', rect_grid,1)
                if self.cells[i][j] != 0:
                    pygame.draw.rect(screen, "#F04626", rect_grid)

    #testing the position of tetromino if he is in the end of grid -> return False
    def tetromino_position(self, tetromino, new_x, new_y):
        for i in range(len(tetromino.current)):
            for j in range(len(tetromino.current[i])):
                if tetromino.current[i][j] == 1:
                    grid_y = new_y + i
                    grid_x = new_x + j
                    if grid_y >= self.nb_rows:
                        return False
                    elif grid_x >= self.nb_cols:
                        return False
                    elif grid_x < 0:
                        return False
                    elif self.cells[grid_y][grid_x] != 0:
                        return False
        return True

    def lock_tetromino(self, tetromino):
        for i in range(len(tetromino.current)):
            for j in range(len(tetromino.current[i])):
                if tetromino.current[i][j] == 1:
                    grid_y = tetromino.y + i
                    grid_x = tetromino.x + j
                    if 0 <= grid_y < self.nb_rows and 0 <= grid_x < self.nb_cols:
                        self.cells[grid_y][grid_x] = 1