from operator import ilshift
from re import X
import pygame

pygame.init()



# Color
RED = (255, 0, 0)
GREEN = (60, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 120)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (180, 180, 180)
DGREY = (50, 50, 50)
TURQUOISE = (64, 224, 208)

# Font
FONT = pygame.font.SysFont('comicsans', 85)


# An object 
class Board:
    def __init__(self, WIN, width, height, padding, extra_padding) -> None:
        # Get the reference for the window
        self.WIN = WIN
        self.width = width
        self.height = height
        self.padding = padding
        self.extra_padding = extra_padding
        self.board = [[Block(WIN, row, col, width, height, padding, self.extra_padding) for row in range(3)]for col in range(3)]

    
    # Draw the board into the window
    def draw(self) -> None:

        # Draw row
        for i in range(2):
            thickness = 5
            pygame.draw.line(self.WIN, WHITE, (self.padding // 2, (i + 1) * self.height // 3 + self.padding // 2 + self.extra_padding), (self.width + self.padding // 2, (i + 1) * self.height // 3 + self.padding // 2 + self.extra_padding), thickness)

        # Draw col
        for i in range(2):
            thickness = 5
            pygame.draw.line(self.WIN, WHITE, ((i + 1) * self.width // 3 + self.padding // 2, self.padding // 2 + self.extra_padding), ((i + 1) * self.width // 3 + self.padding // 2, self.width + self.padding // 2 + self.extra_padding), thickness)
        for i in self.board:
            for j in i:
                j.draw()
    
    
    def tick(self, x, y):
        row = (self.width // 3) // (x - self.padding // 2)
        print(row)

class Block:
    def __init__(self, WIN, row, col, width, height, padding ,extra):
        self.width = width
        self.height = height
        self.WIN = WIN
        self.row = row
        self.col = col
        self.padding = padding 
        self.extra = extra
        self.value = None

    def draw(self):
        if self.value != None:
            value = FONT.render(f'{self.value}', 1, WHITE)
            x = self.padding // 2 + (self.width // 3 * self.row) + 35
            y = self.padding // 2 + self.extra + (self.height // 3 * self.col) + 5
            self.WIN.blit(value, (x, y))
    
    def X(self):
        self.value = 'X'
    
    def O(self):
        self.value = 'O'
            
