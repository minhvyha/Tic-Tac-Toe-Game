import pygame
from board import Board, Block


# initialize pygame library
pygame.init() 

# Window set up
WIDTH = 700
HEIGHT = 700
BOARD_WIDTH = 400
BOARD_HEIGHT = 400

FONT = pygame.font.SysFont('comicsans', 20)
FONT_WIN = pygame.font.SysFont('comicsans', 50)


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sudoku')

# GLOBAL VARIABLE
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 60

# Set up the board
EXTRA_PADDING = 70
board = Board(WIN, BOARD_WIDTH, BOARD_HEIGHT, WIDTH - BOARD_WIDTH, EXTRA_PADDING)


WIN_TEXT = 100

def main():
    isRun = True
    winner = None
    X = 0
    O = 0
    tie = 0
    winner = None
    # Loop forever to draw up the window every second
    while isRun:
        
        # Get any event from user such as mouse click, key pressed
        
        # pygame.event.get() = [click (50, 100)]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRun = False
                break
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] and winner != None:
                winner = None
                board.reset()
            if winner == None and pygame.mouse.get_pressed()[0]:
                x, y = pygame.mouse.get_pos()
                if x < (WIDTH - BOARD_WIDTH) // 2 or x > (WIDTH - BOARD_WIDTH) // 2 + BOARD_WIDTH - 5:
                    continue
                if y < (WIDTH - BOARD_WIDTH) // 2 + EXTRA_PADDING or y > (WIDTH - BOARD_WIDTH) // 2 + BOARD_WIDTH + EXTRA_PADDING - 5:
                    continue
                winner = board.tick(x, y)
                if winner:
                    if winner == 'X':
                        X += 1
                    elif winner == 'O':
                        O += 1
                    else:
                        tie += 1

        if winner != None:
            draw_win(winner, X, O, tie)
            continue
        draw(X, O, tie)
    pygame.quit()


#Function to draw the window
def draw(X, O, tie):

    # Make changes to the window
    WIN.fill((BLACK))
    board.draw()
    draw_score(X, O, tie)
    # Update and display all the changes
    pygame.display.update()

def draw_win(winner, X, O, tie):
    # Make changes to the window
    WIN.fill((BLACK))
    board.draw()
    draw_score(X, O, tie)
    if winner == 'Tie':
        winner = FONT_WIN.render('Tie!', 1, WHITE)
    else:
        winner = FONT_WIN.render(f'{winner} WIN!', 1, WHITE)
    
    # Update and display all the changes
    WIN.blit(winner, (WIDTH // 2 - winner.get_width() // 2, WIN_TEXT))
    pygame.display.update()     


def draw_score(X, O, tie):
    x_player = FONT.render('PLAYER X', 1, WHITE)
    X = FONT.render(f'{X}', 1, WHITE)
    o_player = FONT.render('PLAYER O', 1, WHITE)
    O = FONT.render(f'{O}', 1, WHITE)
    TIE = FONT.render('TIE', 1, WHITE)
    tie = FONT.render(f'{tie}', 1, WHITE)
    WIN.blit(x_player, (150, 15))
    WIN.blit(X, (188, 50))
    WIN.blit(o_player, (550 - o_player.get_width(), 15))
    WIN.blit(O, (492, 50))
    WIN.blit(TIE, (WIDTH // 2 - TIE.get_width() // 2, 15))
    WIN.blit(tie, (WIDTH // 2 - tie.get_width() // 2, 50))

# Execute all the code
if __name__ == '__main__':
    main()