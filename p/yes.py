import pygame
import time
import random

pygame.font.init()

# Set up the window
WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Load background image
BACKGROUND = pygame.transform.scale(pygame.image.load("bg.png"), (WIDTH, HEIGHT))

# Create two instances of the background for seamless looping
background_y1, background_y2 = 0, -HEIGHT

# Load player image
PLAYER_WIDTH, PLAYER_HEIGHT = 40, 60
PLAYER_IMAGE = pygame.transform.scale(pygame.image.load("ship.png"), (PLAYER_WIDTH, PLAYER_HEIGHT))

# Load star image
STAR_WIDTH, STAR_HEIGHT = 25, 50
STAR_IMAGE = pygame.transform.scale(pygame.image.load("star.png"), (STAR_WIDTH, STAR_HEIGHT))

# Define player velocity
PLAYER_VELOCITY = 4  # adjust left and right speed
Y_VELOCITY = 4  # adjust up and down speed

STAR_VELOCITY = 3
BACKGROUND_SCROLL_VELOCITY = 1  # Background scrolling speed

# Set up font and color
FONT = pygame.font.SysFont("comicsans", 30)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Function to draw elements on the screen
def draw(player, elapsed_time, stars):
    # Draw the background instances for seamless looping
    WIN.blit(BACKGROUND, (0, background_y1))
    WIN.blit(BACKGROUND, (0, background_y2))

    # Display elapsed time
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, WHITE)
    WIN.blit(time_text, (10, 10))

    # Draw the player
    WIN.blit(PLAYER_IMAGE, (player.x, player.y))

    # Draw stars
    for star_x, star_y in stars:
        WIN.blit(STAR_IMAGE, (star_x, star_y))

    pygame.display.update()

# Function to create a new star at a random position
def create_star():
    star_x = random.randint(0, WIDTH - STAR_WIDTH)
    star_y = -STAR_HEIGHT
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
    selected_option = None  # To track which option is currently selected



    while run_menu:
        WIN.fill((0, 0, 0))  # Fill the screen with a black background for the menu

       # Adjust the font size for the title
        title_font = pygame.font.SysFont("comicsans", 70)
        title_text = title_font.render("Space Dodge", 1, RED)
        WIN.blit(title_text, (WIDTH/2 - title_text.get_width()/2, 150))

        # Render menu options
        menu_text = FONT.render("Main Menu", 1, WHITE)
        start_text = FONT.render("1. Start Game", 1, RED if selected_option == 1 else WHITE)
        controls_text = FONT.render("2. Controls", 1, RED if selected_option == 2 else WHITE)
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
                    run_menu = False
                elif event.key == pygame.K_2:
                    display_controls()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    return False

            # Handle mouse hover events
            if event.type == pygame.MOUSEMOTION:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_option = get_selected_option(mouse_x, mouse_y)

            # Handle mouse click events
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                selected_option = get_selected_option(mouse_x, mouse_y)
                if selected_option == 1:
                    run_menu = False
                elif selected_option == 2:
                    display_controls()
                elif selected_option == 3:
                    pygame.quit()
                    return False


    return True  # Continue running the game


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

# Function to display controls
def display_controls():
    run_controls = True

    while run_controls:
        WIN.fill((0, 0, 0))

        controls_text = FONT.render("Controls", 1, WHITE)
        back_text = FONT.render("Press 'B' to go back", 1, WHITE)

        WIN.blit(controls_text, (WIDTH/2 - controls_text.get_width()/2, 200))
        WIN.blit(back_text, (WIDTH/2 - back_text.get_width()/2, 300))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run_controls = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    run_controls = False

# Main game loop
def main():
    run = True
    game_over = False

    # Display the main menu
    if not main_menu():
        return

    # Initialize player position and dimensions
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    # Initialize Pygame clock and start time
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    elapsed_time = 0

    # Set up star creation parameters
    star_add_increment = 1000
    star_count = 0

    # List to store star positions
    stars = []

    while run:
        # Track elapsed time and star creation count
        star_count += clock.tick(150)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000

        # Create new stars based on time interval
        if star_count > star_add_increment:
            for _ in range(3):
                stars.append(create_star())

            # Adjust star creation parameters
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

       # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Check if the player has decided to quit
        if not run:
            break  # Exit the loop immediately

        # Handle player movement
        handle_player_movement(player)

        # Update star positions and check for collisions
        new_stars = []
        for star_x, star_y in stars:
            star_y += STAR_VELOCITY

            # Check for collision with player
            if pygame.Rect(star_x, star_y, STAR_WIDTH, STAR_HEIGHT).colliderect(player):
                run = False

            # Check if star is still on the screen
            if star_y + STAR_HEIGHT > 0 and star_y < HEIGHT:
                new_stars.append((star_x, star_y))

        stars = new_stars

        # Update background positions for seamless looping with separate speed
        global background_y1, background_y2
        background_y1 += BACKGROUND_SCROLL_VELOCITY
        background_y2 += BACKGROUND_SCROLL_VELOCITY

        if background_y1 >= HEIGHT:
            background_y1 = -HEIGHT

        if background_y2 >= HEIGHT:
            background_y2 = -HEIGHT

        # Draw elements on the screen
        draw(player, elapsed_time, stars)

        # Display game over message and delay before quitting
        if not run:
            game_over_text = FONT.render("Game Over!", 1, "red")
            WIN.blit(game_over_text, (WIDTH/2 - game_over_text.get_width()/2, HEIGHT/2 - game_over_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
