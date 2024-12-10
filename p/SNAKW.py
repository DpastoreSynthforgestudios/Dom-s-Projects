import pygame
import sys
import random
from collections import deque

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Smooth Snake Game')
    return screen

def load_assets():
    return {
        'font': pygame.font.Font(None, 36),
        'clock': pygame.time.Clock(),
        'eat_sound': pygame.mixer.Sound('eat.wav'),
        'game_over_sound': pygame.mixer.Sound('game_over.wav')
    }
def load_spritesheet(file_path, sprite_size):
    """Loads a spritesheet and returns a list of sprites."""
    spritesheet = pygame.image.load(file_path).convert_alpha()
    num_sprites = spritesheet.get_width() // sprite_size
    return [spritesheet.subsurface(pygame.Rect((i * sprite_size, 0), (sprite_size, sprite_size))) for i in range(num_sprites)]

def draw_snake(screen, snake, sprites):
    """Draws the snake using sprites from the loaded spritesheet."""
    # For simplicity, let's just use the first sprite for the head and the second for the body
    screen.blit(sprites[0], (snake[0].x, snake[0].y))  # Head
    for segment in snake[1:]:
        screen.blit(sprites[1], (segment.x, segment.y))  # Body



def draw_apple(screen, apple_position, apple_image):
    screen.blit(apple_image, (apple_position.x, apple_position.y))

def random_apple_position(snake):
    possible_positions = [
        pygame.Vector2(x, y)
        for x in range(0, WIDTH, CELL_SIZE)
        for y in range(0, HEIGHT, CELL_SIZE)
        if pygame.Vector2(x, y) not in snake
    ]
    return random.choice(possible_positions) if possible_positions else None

def show_game_over(screen, font, assets):
    assets['game_over_sound'].play()
    game_over_text = font.render('Game Over - Press any key to restart', True, WHITE)
    text_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(game_over_text, text_rect)
    pygame.display.flip()
    wait_for_key()
def handle_key(key, current_direction, direction_queue):
    directions = {pygame.K_UP: UP, pygame.K_DOWN: DOWN, pygame.K_LEFT: LEFT, pygame.K_RIGHT: RIGHT}
    opposite_direction = -current_direction
    new_direction = directions.get(key)

    if new_direction and new_direction != opposite_direction and (not direction_queue or new_direction != direction_queue[-1]):
        direction_queue.append(new_direction)
def main():
    screen = init_pygame()
    assets = load_assets()
    apple_image = pygame.image.load('apple.png').convert_alpha()
    snake_sprites = load_spritesheet('Snake_spritesheet.png', CELL_SIZE)
    direction_queue = deque()
    high_score = load_high_score()

    reset_game = True
    while reset_game:
        snake = [pygame.Vector2(WIDTH // 2, HEIGHT // 2)]
        direction = UP
        direction_queue.append(direction)
        apple_position = random_apple_position(snake)
        snake_length = 1
        move_time = 0
        score = 0

        running = True
        while running:
            dt = assets['clock'].tick(FRAME_RATE) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    handle_key(event.key, direction, direction_queue)

            move_time += dt * 1000
            if move_time >= MOVE_INTERVAL:
                move_time %= MOVE_INTERVAL
                running, direction, snake_length, apple_position = update_snake(direction_queue, snake, snake_length, apple_position, direction, assets)

            screen.fill(BLACK)
            draw_apple(screen, apple_position, apple_image)
            draw_score(screen, assets['font'], score, high_score)
            draw_snake(screen, snake, snake_sprites)
            pygame.display.update()

        show_game_over(screen, assets['font'], assets)
        if score > high_score:
            high_score = score
            save_high_score(high_score)
        reset_game = True  # Set to False if you want the game to end after game over

def update_snake(direction_queue, snake, snake_length, apple_position, direction, assets):
    if direction_queue:
        direction = direction_queue.popleft()
    new_head = snake[0] + direction * CELL_SIZE
    if new_head.x < 0 or new_head.x >= WIDTH or new_head.y < 0 or new_head.y >= HEIGHT or new_head in snake:
        return False, direction, snake_length, apple_position
    snake.insert(0, new_head)
    if len(snake) > snake_length:
        snake.pop()
    if snake[0] == apple_position:
        snake_length += 1
        apple_position = random_apple_position(snake)
        snake.append(snake[-1])  # Add a new segment at the same position as the last one
        assets['eat_sound'].play()
    return True, direction, snake_length, apple_position

def draw_score(screen, font, score, high_score):
    score_text = font.render(f'Score: {score} High Score: {high_score}', True, WHITE)
    screen.blit(score_text, (10, 10))

def load_high_score():
    try:
        with open("high_score.txt", "r") as file:
            return int(file.read())
    except (IOError, ValueError):
        return 0

def save_high_score(high_score):
    with open("high_score.txt", "w") as file:
        file.write(str(high_score))

# Constants
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
FRAME_RATE = 60
MOVE_INTERVAL = 100
UP = pygame.Vector2(0, -1)
DOWN = pygame.Vector2(0, 1)
LEFT = pygame.Vector2(-1, 0)
RIGHT = pygame.Vector2(1, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

if __name__ == '__main__':
    main()
