import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BG_COLOR = WHITE  # Changed to black
LINE_COLOR = (23, 145, 135)
BUTTON_COLOR = (23, 145, 135)
FONT = pygame.font.Font(None, 40)

# Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Board
board = [[None] * 3 for _ in range(3)]

def draw_lines():
    # Draws game board lines
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, BLACK, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures():
    # Draws 'O' and 'X' on the board
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, GREEN, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, RED, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)

def mark_square(row, col, player):
    board[row][col] = player

def available_square(row, col):
    return board[row][col] is None

def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] is None:
                return False
    return True

def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = None

def main_menu():
    start_button = pygame.Rect(WIDTH // 4, HEIGHT // 3, WIDTH // 2, 50)
    options_button = pygame.Rect(WIDTH // 4, 2 * HEIGHT // 3, WIDTH // 2, 50)
    while True:
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, BLACK, start_button)
        pygame.draw.rect(screen, BLACK, options_button)
        draw_text('Start', start_button)
        draw_text('Options', options_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main_game()
                elif options_button.collidepoint(event.pos):
                    print("Options Menu")  # Placeholder for options functionality

        pygame.display.update()

def draw_text(text, rect):
    text_surface = FONT.render(text, True, RED)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main_game():
    player = 'X'
    running = True
    game_over = False
    restart()
    play_again_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 - 25, WIDTH // 2, 50)  # Positioned higher
    main_menu_button = pygame.Rect(WIDTH // 4, HEIGHT // 2 + 50, WIDTH // 2, 50)   # Positioned lower
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    mouseX = event.pos[0]  # x
                    mouseY = event.pos[1]  # y
                    clicked_row = int(mouseY // SQUARE_SIZE)
                    clicked_col = int(mouseX // SQUARE_SIZE)
                    if available_square(clicked_row, clicked_col):
                        mark_square(clicked_row, clicked_col, player)
                        draw_figures()
                        if check_win(player):
                            game_over = True
                            outcome_text = f'{player} wins!'
                        elif is_board_full():
                            game_over = True
                            outcome_text = 'Game Draw!'
                        player = 'X' if player == 'O' else 'O'

                if game_over:
                    if play_again_button.collidepoint(event.pos):
                        game_over = False
                        restart()
                    elif main_menu_button.collidepoint(event.pos):
                        main_menu()

        if game_over:
            draw_game_over(outcome_text, play_again_button, main_menu_button)

        pygame.display.update()

def draw_game_over(outcome_text, play_again_button, main_menu_button):
    screen.fill(BG_COLOR)
    draw_lines()
    draw_figures()
    draw_text(outcome_text, pygame.Rect(0, HEIGHT // 4, WIDTH, HEIGHT // 6))
    pygame.draw.rect(screen, BLACK, play_again_button)
    pygame.draw.rect(screen, BLACK, main_menu_button)
    draw_text('Play Again', play_again_button)
    draw_text('Main Menu', main_menu_button)


def main_menu():
    start_button = pygame.Rect(WIDTH // 4, HEIGHT // 3, WIDTH // 2, 50)
    options_button = pygame.Rect(WIDTH // 4, 2 * HEIGHT // 3, WIDTH // 2, 50)
    while True:
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, BLACK, start_button)
        pygame.draw.rect(screen, BLACK, options_button)
        draw_text('Start', start_button)
        draw_text('Options', options_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    main_game()
                elif options_button.collidepoint(event.pos):
                    print("Options Menu")  # Placeholder for options functionality

        pygame.display.update()



# Start the application
main_menu()
