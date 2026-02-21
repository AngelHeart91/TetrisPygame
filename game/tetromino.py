import random,pygame

class Tetromino:
    shape = [
        [[1, 1, 1, 1], [0, 0, 0, 0]],  # shape straight
        [[1, 1, 0, 0], [1, 1, 0, 0]],  # shape square
        [[1, 1, 1, 0], [1, 0, 0, 0]],  # shape L
        [[1, 1, 1, 0], [0, 1, 0, 0]],  # shape T
        [[1, 1, 0, 0], [0, 1, 1, 0]]   # shape skew
    ]
    def __init__(self):
        self.shape = random.choice(Tetromino.shape)
        self.x = 0
        self.y = 0
        self.rotation = 0

    def draw_tetromino(self, screen, cell_size):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    rect_tetromino = pygame.Rect(j * cell_size, i * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, pygame.Color('#F04626'), rect_tetromino)