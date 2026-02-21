import random,pygame

class Tetromino:
    shape = [
        [[1, 1, 1, 1], [0, 0, 0, 0]],   # shape straight
        [[1, 1, 0, 0], [1, 1, 0, 0]],   # shape square
        [[1, 1, 1, 0], [1, 0, 0, 0]],   # shape L
        [[1, 1, 1, 0], [0, 1, 0, 0]],   # shape T
        [[1, 1, 0, 0], [0, 1, 1, 0]]    # shape skew
    ]
    def __init__(self):
        self.shape = random.choice(Tetromino.shape)
        self.x = 4                      #4 for the middle to the display / 0 to the top-left
        self.y = 0
        self.rotation = 0

    #function who draw the tetromino on the display
    def draw_tetromino(self, screen, cell_size):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j] == 1:
                    rect_tetromino = pygame.Rect((self.x + j) * cell_size, (self.y + i) * cell_size, cell_size, cell_size)
                    pygame.draw.rect(screen, pygame.Color('#F04626'), rect_tetromino)

    def move_down(self):
        self.y += 1