# Import necessary libraries
import pygame
import time
import random
import sys

# Initialize Pygame and font module
pygame.init()
pygame.font.init()

# Load the death sound effect
GO_sound = pygame.mixer.Sound("gta.mp3")  # Replace with the actual path to your death sound effect file

# Constants
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BACKGROUND_SCROLL_VELOCITY = 1

# Define background variables at the global scope
background_y1, background_y2 = 0, -HEIGHT

# Load images and create masks
BACKGROUND = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))
PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("ship.png"), (40, 60))
STAR_IMAGE = pygame.transform.scale(pygame.image.load("star.png"), (25, 50))
player_mask = pygame.mask.from_surface(PLAYER_IMAGE)
star_mask = pygame.mask.from_surface(STAR_IMAGE)

# Set up font and color
FONT = pygame.font.SysFont("comicsans", 30)
WHITE, RED, BLACK, BLUE, BROWN, YELLOW = (255, 255, 255), (255, 0, 0), (0, 0, 0), (0, 0, 255), (165, 42, 42), (255, 255, 0)

# Define player and star velocities
PLAYER_VELOCITY, Y_VELOCITY = 4, 4
STAR_VELOCITY = 3

# Function to draw elements on the screen
def draw(player, elapsed_time, stars, score):
    WIN.blit(BACKGROUND, (0, background_y1))
    WIN.blit(BACKGROUND, (0, background_y2))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, WHITE)
    score_text = FONT.render(f"Score: {score}", 1, WHITE)  # Add score display


    WIN.blit(time_text, (10, 10))
    WIN.blit(score_text, (10, 50))  # Blit the score text
    WIN.blit(PLAYER_IMAGE, (player.x, player.y))

    for star_x, star_y in stars:
        WIN.blit(STAR_IMAGE, (star_x, star_y))

    pygame.display.update()

# Function to create a new star at a random position
def create_star():
    star_x = random.randint(0, WIDTH - STAR_IMAGE.get_width())
    star_y = -STAR_IMAGE.get_height()
    return star_x, star_y

# Function to handle player movement based on keyboard input
def handle_player_movement(player):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x - PLAYER_VELOCITY >= 0:
        player.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player.x + PLAYER_VELOCITY + player.width <= WIDTH:
        player.x += PLAYER_VELOCITY
    if keys[pygame.K_UP] and player.y - Y_VELOCITY >= 0:
        player.y -= Y_VELOCITY
    if keys[pygame.K_DOWN] and player.y + Y_VELOCITY + player.height <= HEIGHT:
        player.y += Y_VELOCITY

# Function to display the main menu
def main_menu():
    run_menu = True
    selected_option = None

    original_menu_image = pygame.image.load("mm bg.png")
    menu_image = pygame.transform.scale(original_menu_image, (350, 650))
    menu_image_rotated = pygame.transform.rotate(menu_image, -40)

    new_background_image = pygame.image.load("bg still.jpeg")
    new_background_image = pygame.transform.scale(new_background_image, (WIDTH, HEIGHT))

    while run_menu:
        combined_background = pygame.Surface((WIDTH, HEIGHT))
        combined_background.blit(new_background_image, (0, 0))  # Blit the new picture
        combined_background.blit(menu_image_rotated, ((WIDTH - menu_image_rotated.get_width()) // -2,
                                                      (HEIGHT - menu_image_rotated.get_height()) // 1))


        WIN.blit(combined_background, (0, 0))

        title_font = pygame.font.SysFont("bauhaus93", 70)
        title_text = title_font.render("Space Dodge", 1, RED)
        WIN.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 150))

        menu_text = FONT.render("Main Menu", 1, YELLOW)
        start_text = FONT.render("1. Start Game", 1, RED if selected_option == 1 else WHITE)
        controls_text = FONT.render("2. Controls", 1, RED if selected_option == 2 else YELLOW)
        exit_text = FONT.render("3. Exit", 1, RED if selected_option == 3 else WHITE)

        WIN.blit(menu_text, (WIDTH/2 - menu_text.get_width()/2, 250))
        WIN.blit(start_text, (WIDTH/2 - start_text.get_width()/2, 300))
        WIN.blit(controls_text, (WIDTH/2 - controls_text.get_width()/2, 350))
        WIN.blit(exit_text, (WIDTH/2 - exit_text.get_width()/2, 400))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return True
                elif event.key == pygame.K_2:
                    display_controls()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    return False

            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_option = get_selected_option(mouse_x, mouse_y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_option = get_selected_option(mouse_x, mouse_y)
                if selected_option == 1:
                    return True
                elif selected_option == 2:
                    display_controls()
                elif selected_option == 3:
                    return False

    return True

def get_selected_option(mouse_x, mouse_y):
    text_positions = [
        (WIDTH/2 - FONT.size("1. Start Game")[0]/2, 300),
        (WIDTH/2 - FONT.size("2. Controls")[0]/2, 350),
        (WIDTH/2 - FONT.size("3. Exit")[0]/2, 400),
    ]
    for i, (text_x, text_y) in enumerate(text_positions, start=1):
        text_width, text_height = FONT.size(f"{i}. Option")
        if text_x <= mouse_x <= text_x + text_width and text_y <= mouse_y <= text_y + text_height:
            return i
    return None

def display_controls():
    run_controls = True

    while run_controls:
        WIN.fill(BLACK)

        controls_text = FONT.render("Controls", 1, WHITE)
        controls_info = [
            "Use Arrow Keys for Movement:",
            "   - Left: Move left",
            "   - Right: Move right",
            "   - Up: Move up",
            "   - Down: Move down",
            "Press 'B' to go back",
        ]

        for i, line in enumerate(controls_info):
            line_text = FONT.render(line, 1, WHITE)
            WIN.blit(line_text, (WIDTH/2 - line_text.get_width()/2, 200 + i * 40))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run_controls = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    run_controls = False

def game_over_screen(score):
    GO_sound.play()
    WIN.fill(BLACK)

    game_over_font = pygame.font.SysFont("bauhaus93", 70)
    game_over_text = game_over_font.render("Game Over!", 1, RED)
    score_text = FONT.render(f"Score: {score}", 1, BLUE)
    replay_text = FONT.render("1. Play Again", 1, WHITE)
    quit_text = FONT.render("2. Quit", 1, WHITE)
    menu_text = FONT.render("3. Main Menu", 1, WHITE)

    WIN.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/3 - game_over_text.get_height()/2))
    WIN.blit(score_text, (WIDTH/2 - score_text.get_width()/2, HEIGHT/3 + 30))  # Position the score text
    WIN.blit(replay_text, (WIDTH/2 - replay_text.get_width()/2, HEIGHT/2.5 + 20))
    WIN.blit(quit_text, (WIDTH/2 - quit_text.get_width()/2, HEIGHT/2.5 + 60))
    WIN.blit(menu_text, (WIDTH/2 - menu_text.get_width()/2, HEIGHT/2.5 + 100))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "play_again"
                elif event.key == pygame.K_2:
                    pygame.quit()
                    return "quit"
                elif event.key == pygame.K_3:
                    return "main_menu"

        pygame.display.update()

def display_pause_menu():
    WIN.fill(BLACK)

    pause_font = pygame.font.SysFont("comicsans", 60)
    pause_text = pause_font.render("Paused", 1, RED)
    resume_text = FONT.render("1. Resume", 1, WHITE)
    restart_text = FONT.render("2. Restart", 1, WHITE)
    menu_text = FONT.render("3. Main Menu", 1, WHITE)

    WIN.blit(pause_text, (WIDTH/2 - pause_text.get_width()/2, HEIGHT/3 - pause_text.get_height()/2))
    WIN.blit(resume_text, (WIDTH/2 - resume_text.get_width()/2, HEIGHT/2.5 + 20))
    WIN.blit(restart_text, (WIDTH/2 - restart_text.get_width()/2, HEIGHT/2.5 + 60))
    WIN.blit(menu_text, (WIDTH/2 - menu_text.get_width()/2, HEIGHT/2.5 + 100))

    pygame.display.update()

    pygame.time.delay(500)

# Main game loop
def main():
    global background_y1, background_y2

    pygame.mixer.init()
    pygame.mixer.music.load("Resilience.ogg")
    pygame.mixer.music.play(-1)

    paused = False
    spawn_stars = True

    score = 0

    while True:
        clock = pygame.time.Clock()

        if not main_menu():
            pygame.mixer.music.stop()
            break

        # Load game music (space odyssey)
        pygame.mixer.music.load("music.ogg")
        pygame.mixer.music.play(-1)

        start_time = pygame.time.get_ticks()
        elapsed_time = 0
        star_add_increment = 1000
        star_count = 0
        stars = []
        player = pygame.Rect(200, HEIGHT - PLAYER_IMAGE.get_height(), PLAYER_IMAGE.get_width(), PLAYER_IMAGE.get_height())
        game_over = False

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = not paused
                    spawn_stars = not paused

            if not paused:
                star_count += clock.tick(150)
                elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
                score = int(elapsed_time * 150)

                if spawn_stars and star_count > star_add_increment:
                    for _ in range(3):
                        stars.append(create_star())

                    star_add_increment = max(200, star_add_increment - 50)
                    star_count = 0

                handle_player_movement(player)

                new_stars = []
                for star_x, star_y in stars:
                    star_y += STAR_VELOCITY

                    if player_mask.overlap(star_mask, (int(star_x - player.x), int(star_y - player.y))):
                        print("Collision detected with star at:", star_x, star_y)
                        pygame.time.delay(2000)
                        game_over = True
                        break

                    if star_y + STAR_IMAGE.get_height() > 0 and star_y < HEIGHT:
                        new_stars.append((star_x, star_y))

                stars = new_stars

                background_y1 += BACKGROUND_SCROLL_VELOCITY
                background_y2 += BACKGROUND_SCROLL_VELOCITY

                if background_y1 >= HEIGHT:
                    background_y1 = -HEIGHT

                if background_y2 >= HEIGHT:
                    background_y2 = -HEIGHT

            draw(player, elapsed_time, stars, score)

            if paused:
                display_pause_menu()

                pause_event = pygame.event.wait()
                if pause_event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif pause_event.type == pygame.KEYDOWN:
                    if pause_event.key == pygame.K_1:
                        paused = False
                    elif pause_event.key == pygame.K_2:
                        paused = False
                        game_over = True
                    elif pause_event.key == pygame.K_3:
                        paused = False
                        game_over = True
                        break

            if game_over:
                # Stop game music when game over
                pygame.mixer.music.stop()

                result = game_over_screen(score)

                if result == "quit":
                    pygame.mixer.quit()
                    pygame.quit()
                    sys.exit()
                elif result == "main_menu":
                    pygame.mixer.music.load("Resilience.ogg")
                    pygame.mixer.music.play(-1)
                    break
                elif result == "play_again":
                    pygame.mixer.music.load("music.ogg")
                    pygame.mixer.music.play(-1)
                    start_time = pygame.time.get_ticks()
                    elapsed_time = 0
                    star_add_increment = 1000
                    star_count = 0
                    stars = []
                    player = pygame.Rect(200, HEIGHT - PLAYER_IMAGE.get_height(), PLAYER_IMAGE.get_width(), PLAYER_IMAGE.get_height())
                    game_over = False

    pygame.quit()

if __name__ == "__main__":
    main()
