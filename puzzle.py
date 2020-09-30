import pygame
import random

# --- constants --- (UPPER_CASE names)

GRID_DIMENSION = 3
SCREEN_DIMENSION = 900
SQUARE_DIMENSION = int(round(SCREEN_DIMENSION / GRID_DIMENSION))

FONT_SIZE = int(round(0.57 * SQUARE_DIMENSION))
LAST = GRID_DIMENSION - 1


BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)

FPS = 30


pygame.init()

screen = pygame.display.set_mode((SCREEN_DIMENSION, SCREEN_DIMENSION))

pygame.display.set_caption("Sliding Puzzle")

# - objects -

x_coords = [_ for _ in range(0, SCREEN_DIMENSION, SQUARE_DIMENSION)]
y_coords = [_ for _ in range(0, SCREEN_DIMENSION, SQUARE_DIMENSION)]
random.shuffle(x_coords)
random.shuffle(y_coords)
board = [[pygame.Rect(x, y, SQUARE_DIMENSION, SQUARE_DIMENSION) for x in x_coords] for y in y_coords]

blank_coords = [board[LAST][LAST].x, board[LAST][LAST].y]
print()

font = pygame.font.SysFont('Arial', FONT_SIZE)

selected = (-1, -1)

# - mainloop -

clock = pygame.time.Clock()

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:               
                for (y, row) in enumerate(board):
                    for (x, piece) in enumerate(row):
                        if piece.collidepoint(event.pos):
                            if (abs(piece.x - blank_coords[0]) + abs(piece.y-blank_coords[1])) <= SQUARE_DIMENSION:
                                temp = board[y][x]
                                board[y][x] = board[LAST][LAST]
                                board[LAST][LAST] = temp
                                blank_coords = [piece.x, piece.y]


    # - draws (without updates) -

    screen.fill(BLACK)
    

    for (y, row) in enumerate(board):
        for (x, piece) in enumerate(row):
            color = WHITE
            if (x + y) % 2 == 0:
                color = RED
            
            if (x, y) == (LAST, LAST):
                color = BLACK

            pygame.draw.rect(screen, color, piece)
            text = font.render(str(4 * y + x + 1), True, BLACK)
            screen.blit(text, (piece.x, piece.y))

    pygame.display.flip()

    # - constant game speed / FPS -

    clock.tick(FPS)

# - end -

pygame.quit()
