from operator import ilshift
from re import X
from turtle import width
import pygame

pygame.init()



# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


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
        row = (y - (self.padding // 2 + self.extra_padding)) // (self.height // 3)
        col = (x - self.padding // 2) // (self.width // 3)
        self.board[row][col].assign()
        if self.checkWin(row, col):
            return Block.Current[1]
        if self.checkTie():
            return 'Tie'
        return None

    def checkWin(self, row, col):
        curr_row = []
        curr_col = []
        diag1 = [(0, 0), (2, 2), (1, 1)]
        diag2 = [(2, 0), (0, 2), (1, 1)]
        for i in range(3):
            curr_row.append(self.board[row][i].value)
            curr_col.append(self.board[i][col].value)
        pos = (row, col)
        diag_right = []
        diag_left = []
        if pos in diag2:
            diag_right.append(self.board[2][0].value)
            diag_right.append(self.board[1][1].value)
            diag_right.append(self.board[0][2].value)
        if pos in diag1:
            for i in range(3):
                diag_left.append(self.board[i][i].value)
        if diag_left:
            for i, value in enumerate(diag_left):
                if value != Block.Current[1]:
                    break
                if i == 2:
                    return True
        if diag_right:
            for i, value in enumerate(diag_right):
                if value != Block.Current[1]:
                    break
                if i == 2:
                    return True
        curr_col = set(curr_col)
        curr_row = set(curr_row)
        if len(curr_col) == 1 and Block.Current[1] in curr_col:
            return True
        if len(curr_row) == 1 and Block.Current[1] in curr_row:
            return True
        return False

    def checkTie(self):
        for i in self.board:
            for j in i:
                if j.value == None:
                    return False
        return True

    def reset(self):
        for i in self.board:
            for j in i:
                j.reset()

class Block:
    Current = ['O', 'X']
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
    
    def assign(self):
        if self.value != None:
            return
        self.value = Block.Current[0]
        Block.Current.append(Block.Current[0])
        Block.Current.pop(0)
    
    def reset(self):
        self.value = None