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
FONT = pygame.font.SysFont('comicsans', 25)


# An object 
class Board:
    def __init__(self, WIN, width, height, padding) -> None:
        # 9 x 9 sudoku board
        self.board = [[Block(WIN, row, col, width, height) for row in range(9)]for col in range(9)]
        # Get the reference for the window
        self.WIN = WIN
        self.width = width
        self.height = height
        self.padding = padding


    # Draw the board into the window
    def draw(self) -> None:

        # Draw row
        for i in range(2):
            thickness = 5
            pygame.draw.line(self.WIN, WHITE, (self.padding // 2, (i + 1) * self.height // 3 + self.padding // 2 + 30), (self.width + self.padding // 2, (i + 1) * self.height // 3 + self.padding // 2 + 30), thickness)

        # Draw col
        for i in range(2):
            thickness = 5
            pygame.draw.line(self.WIN, WHITE, ((i + 1) * self.width // 3 + self.padding // 2, self.padding // 2 + 30), ((i + 1) * self.width // 3 + self.padding // 2, self.width + self.padding // 2 + 30), thickness)


class Block:
    def __init__(self, WIN, row, col, width, height):
        self.width = width
        self.height = height
        self.WIN = WIN
        self.row = row
        self.col = col
        self.value = 0

    def draw(self):
        if self.value != -1:
            num = FONT.render(f'{self.value}', 1, BLACK)
            self.WIN.blit(num, (self.width // 9 * self.row + (self.width // 9 // 2) - num.get_width() // 2, + (self.height // 9) * self.col + self.height // 9 // 2 - num.get_height() // 2))
            
