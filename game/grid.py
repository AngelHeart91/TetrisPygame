import pygame

class Grid:
    def __init__(self):
        self.nb_rows = 20
        self.nb_cols = 10
        self.cell_size = 30
    def draw_grid(self,screen):
        for i in range (0, self.nb_rows):
            for j in range (0, self.nb_cols):
                rect_grid = pygame.Rect(j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, '#1A388A', rect_grid,1)