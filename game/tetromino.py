import random,pygame
from game.shape import SHAPES

class Tetromino:
    def __init__(self):
        self.kind = random.choice(list(SHAPES.keys()))
        self.shape = SHAPES[self.kind]
        self.x = 4                      #4 for the middle to the display / 0 to the top-left
        self.y = 0
        self.rotation = 0
        self.current = self.shape[self.rotation]

    #function who draw the tetromino on the display
    def draw_tetromino(self, screen, cell_size):
        for i in range(len(self.current)):
            for j in range(len(self.current[i])):
                if self.current[i][j] == 1:
                    rect_tetromino = pygame.Rect((self.x + j) * cell_size, (self.y + i) * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, pygame.Color('#F04626'), rect_tetromino)

    def move_down(self):
        self.y += 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def rotate(self):
        self.rotation = (self.rotation + 1) % 4
        self.current = self.shape[self.rotation]