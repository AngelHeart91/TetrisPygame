import pygame

class Grid:
    def __init__(self):
        self.nb_rows = 15
        self.nb_cols = 11
        self.cell_size = 30

    def draw_grid(self,screen):
        for i in range (0, self.nb_rows):
            for j in range (0, self.nb_cols):
                rect_grid = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, '#1A388A', rect_grid,1)

    #testing the position of tetromino if he is in the end of grid -> return False
    def tetromino_position(self, tetromino, new_x, new_y):
        for i in range(len(tetromino.shape)):
            for j in range(len(tetromino.shape[i])):
                if tetromino.shape[i][j] == 1:
                    grid_y = new_y + i
                    if grid_y >= self.nb_rows:
                        return False
        return True