import pygame
import sys
import random
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

pygame.init()
pygame.mixer.init()

score = 0
# Constants
WIDTH, HEIGHT = 1000, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Load the icon
icon = pygame.image.load("icon/icon.ico")  # Replace with the actual path to your icon file

# Set the icon for the game window
pygame.display.set_icon(icon)

pygame.display.set_caption("Chapter 8:The Hunt For The Egg")

# Flag to determine the current screen
current_screen = "menu"  # Possible values: "menu", "loading", "game"

game_over = False

def show_main_menu():
    menu_font = pygame.font.Font(font_path, 48)
    play_text = menu_font.render("Press P to Play", True, WHITE)
    exit_text = menu_font.render("Press Q to Quit", True, WHITE)

    play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    exit_rect = exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

    waiting_for_input = True

    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    waiting_for_input = False
                    screen.blit(bg_image, (0, 0))
                    return "loading"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        screen.blit(play_text, play_rect)
        screen.blit(exit_text, exit_rect)
        pygame.display.flip()
        pygame.time.delay(10)
        

def show_loading_screen():
    loading_font = pygame.font.Font(font_path, 48)
    loading_text = loading_font.render("Loading...", True, WHITE)
    loading_rect = loading_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(loading_text, loading_rect)
    pygame.display.flip()

    pygame.time.delay(3000)  # Display the loading screen for 3 seconds
    reset_game()
def get_player_initials():
    initials = ""
    entering = True
    font_input = pygame.font.Font(font_path, 30)

    while entering:
        screen.fill(BLACK)
        text_surface = font_input.render(f"Enter your 3 initials: {initials}", True, WHITE)
        rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text_surface, rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    initials = initials[:-1]
                elif event.key == pygame.K_RETURN and len(initials) == 3:
                    entering = False
                elif len(initials) < 3 and event.unicode.isalpha():
                    initials += event.unicode.upper()

    return initials
blaster_sound = pygame.mixer.Sound("sounds/blaster.mp3")
prize_sound = pygame.mixer.Sound("sounds/prize.mp3")
destruction_sound = pygame.mixer.Sound("sounds/destruction.mp3")

pygame.mixer.music.load("sounds/arcade.mp3")
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play(-1)

# Load images
bg_image = pygame.image.load("images/background.jpg")
player_image = pygame.image.load("images/player.png")
enemy_image = pygame.image.load("images/enemy.png")
prize_image = pygame.image.load("images/prize.png")
blaster_image = pygame.image.load("images/blaster.png")
friend_image = pygame.image.load("images/friend.png")
asteroid_image = pygame.image.load("images/asteroid.png")
enemy_blaster_image = pygame.image.load("images/enemy_blaster.png")

# Resize images
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT * 2))
player_image = pygame.transform.scale(player_image, (125, 125))
enemy_image = pygame.transform.scale(enemy_image, (100, 100))
prize_image = pygame.transform.scale(prize_image, (50, 50))
friend_image = pygame.transform.scale(friend_image, (100, 100))
asteroid_image = pygame.transform.scale(asteroid_image, (100, 100))
blaster_image = pygame.transform.scale(blaster_image, (19, 78))
enemy_blaster_image = pygame.transform.scale(enemy_blaster_image, (19, 78))

# Player properties
player_width, player_height = player_image.get_width(), player_image.get_height()
player_x = WIDTH // 2 - player_width // 2
player_y = 400
player_speed = 6

# Smaller collision box for the player
player_collision_width, player_collision_height = 60, 80
player_collision_rect = pygame.Rect(
    player_x + (player_width - player_collision_width) // 2,
    player_y + (player_height - player_collision_height) // 2,
    player_collision_width,
    player_collision_height,
)
# Constants for asteroids
asteroid_probability = 0.005
asteroid_speed = 3

high_score = 0

# Variables for firing cooldown
last_fire_time = pygame.time.get_ticks()
fire_cooldown = 500

# Speeds for game objects
prize_speed = 2
enemy_speed = 1
friend_speed = 5

# Variables
MAX_LIVES = 1
lives = MAX_LIVES  # Add this line to initialize lives


# Blaster properties
blaster_speed = 9
blaster_list = []
enemy_blaster_list = []

# Lists for game objects
enemies = []
prizes = []
friends = []
asteroids = []

# Constants
MAX_LIVES = 1

# Variables
lives = MAX_LIVES

# Font setup for displaying score
font_path = "font/RetroFont.ttf"
font = pygame.font.Font(font_path, 36)

# Scaling factor for adjusting probabilities
scaling_factor = 1
enemy_probability = 0.001 * scaling_factor
prize_probability = 0.02 * scaling_factor
friend_probability = 0.01 * scaling_factor
enemy_blaster_probability = 0.001 * scaling_factor

# Classes for game objects
class FlyingObject:
    def __init__(self, x, y, speed, image):
        self.rect = pygame.Rect(x, y, image.get_width(), image.get_height())
        self.speed = speed
        self.image = image

    def update(self):
        self.rect.y += self.speed

class Asteroid(FlyingObject):
    def __init__(self, x, y, speed, start_y=0):
        super().__init__(x, start_y, speed, asteroid_image)

class Prize(FlyingObject):
    def __init__(self, x, y, speed, start_y=-0):
        super().__init__(x, start_y, speed, prize_image)

class Enemy(FlyingObject):
    def __init__(self, x, y, speed, start_y=0):
        super().__init__(x, start_y, speed, enemy_image)
        self.last_shot_time = pygame.time.get_ticks()

    def update(self):
        super().update()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > 3000:
            self.last_shot_time = current_time
            self.shoot_blaster()

    def shoot_blaster(self):
        enemy_blaster_x = self.rect.x + self.rect.width // 2 - blaster_image.get_width() // 2
        enemy_blaster_y = self.rect.y + self.rect.height
        enemy_blaster_list.append(EnemyBlaster(enemy_blaster_x, enemy_blaster_y, blaster_speed))
        blaster_sound.play()

class EnemyBlaster(FlyingObject):
    def __init__(self, x, y, speed):
        super().__init__(x, y, speed, enemy_blaster_image)
        self.last_shot_time = pygame.time.get_ticks()

    def update(self):
        super().update()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > 3000:
            self.last_shot_time = current_time
            self.shoot_blaster()

    def shoot_blaster(self):
        enemy_blaster_x = self.rect.x + self.rect.width // 2 - blaster_image.get_width() // 2
        enemy_blaster_y = self.rect.y + self.rect.height
        enemy_blaster_list.append(Blaster(enemy_blaster_x, enemy_blaster_y, blaster_speed, is_player=False))
        blaster_sound.play()

class Blaster(FlyingObject):
    def __init__(self, x, y, speed, is_player=True):
        super().__init__(x, y, speed, blaster_image)
        self.is_player = is_player

    def update(self):
        if self.is_player:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class GameOverScreen:
    def __init__(self):
        self.font = pygame.font.Font(font_path, 72)

    def render(self, final_score):
        game_over_text = self.font.render("Game Over", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))

        score_text = self.font.render(f"Score: {final_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))

        return game_over_text, score_text, game_over_rect, score_rect



def display_lives():
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (WIDTH - 300, 10))

def get_player_initials():
    """Prompt player to enter 3 initials."""
    initials = ""
    entering = True
    font_input = pygame.font.Font(font_path, 36)

    while entering:
        screen.fill(BLACK)
        text_surface = font_input.render(f"Enter your 3 initials: {initials}", True, WHITE)
        rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(text_surface, rect)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    initials = initials[:-1]
                elif event.key == pygame.K_RETURN and len(initials) == 3:
                    entering = False
                elif len(initials) < 3 and event.unicode.isalpha():
                    initials += event.unicode.upper()

    return initials

def save_score(initials, score):
    """Save the initials and score to high score file."""
    high_score_file = "files/high_scores.txt"
    try:
        # Read existing scores
        high_scores = []
        with open(high_score_file, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    hi, sc = parts
                    high_scores.append((hi, int(sc)))
    except FileNotFoundError:
        high_scores = []

    # Add current score
    high_scores.append((initials, score))

    # Sort and keep top 5
    high_scores.sort(key=lambda x: x[1], reverse=True)
    top_5 = high_scores[:5]

    # Save back to file
    with open(high_score_file, "w") as file:
        for hi, sc in top_5:
            file.write(f"{hi} {sc}\n")    

def prompt_play_again():
    prompt_font = pygame.font.Font(font_path, 20)
    prompt_text = prompt_font.render("Thank you for playing! Play again? (Y/N)", True, WHITE)
    prompt_rect = prompt_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    
    screen.fill(BLACK)
    screen.blit(prompt_text, prompt_rect)
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    screen.fill(BLACK)          
                    pygame.display.flip()       
                    return True
                elif event.key == pygame.K_n:
                    return False
def display_final_score(final_score):
    """Display Game Over and top 5 scores, then wait for key press."""
    player_initials = get_player_initials()
    save_score(player_initials, final_score)

    screen.fill(BLACK)
    final_font = pygame.font.Font(font_path, 48)
    title_surface = final_font.render("Game Over!", True, WHITE)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, 80))
    screen.blit(title_surface, title_rect)

    high_font = pygame.font.Font(font_path, 36)
    try:
        with open("files/high_scores.txt", "r") as file:
            high_scores = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        high_scores = ["AAA 0"] * 5

    for i, line in enumerate(high_scores[:5]):
        text_surface = high_font.render(f"{i+1}. {line}", True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 180 + i*50))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

    # Wait for player to press any key to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def load_high_score():
    global high_score
    try:
        with open("files/high_scores.txt", "r") as file:
            scores = []
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    _, sc = parts
                    scores.append(int(sc))

            high_score = max(scores) if scores else 0

    except FileNotFoundError:
        high_score = 0
    except Exception as e:
        print(f"Error loading high score: {e}")
        high_score = 0
def save_high_score():
    global high_score
    try:
        with open("files/high_scores.txt", "a") as file:
            file.write(str(high_score) + '\n')
    except Exception as e:
        print(f"Error saving high score: {e}")

# Modify display_high_scores function
def display_high_scores():
    """Displays the top 5 high scores with initials."""
    high_font = pygame.font.Font(font_path, 36)
    high_score_file = "files/high_scores.txt"

    # Load initials + scores
    try:
        with open(high_score_file, "r") as file:
            high_scores = []
            for line in file:
                parts = line.strip().split()
                if len(parts) == 2:
                    initials, score = parts
                    high_scores.append((initials, int(score)))
    except FileNotFoundError:
        high_scores = [("AAA", 0)] * 5

    # Sort descending
    high_scores.sort(key=lambda x: x[1], reverse=True)
    top_5 = high_scores[:5]

    # Clear screen
    screen.fill(BLACK)

    # Render each high score line
    for i, (initials, score) in enumerate(top_5):
        text_surface = high_font.render(f"{i + 1}. {initials} {score}", True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, 150 + i * 60))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
    pygame.time.delay(3000)  # Show for 3 seconds

def create_blaster(x, y):
    global last_fire_time
    current_time = pygame.time.get_ticks()
    if current_time - last_fire_time > fire_cooldown:
        blaster_rect = pygame.Rect(x - blaster_image.get_width() // 2, y, blaster_image.get_width(), blaster_image.get_height())
        blaster_list.append(Blaster(blaster_rect.x, blaster_rect.y, blaster_speed))
        last_fire_time = current_time
        blaster_sound.play()

def reset_game():
    global player_x, player_y, blaster_list, enemy_blaster_list, enemies, prizes, friends, asteroids, score, game_over, current_screen
    player_x = WIDTH // 2 - player_width // 2
    player_y = 400
    blaster_list = []
    enemy_blaster_list = []
    enemies = []
    prizes = []
    friends = []
    asteroids = []
    score = 0
    lives = MAX_LIVES
    # Reset the score only if it's not a new game after a game over

def pause_game(duration):
    pygame.time.delay(duration)

def update_player_collision_rect():
    global player_collision_rect
    player_collision_rect.x = player_x + (player_width - player_collision_width) // 2
    player_collision_rect.y = player_y + (player_height - player_collision_height) // 2

def display_and_reset_score():
    global score, high_score
    temp_score = score  # Store the current score in a temporary variable
    score_text = font.render(f"Score: {temp_score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    display_high_scores()  # Display the high score
    pygame.display.flip()
    score = 0  # Reset the score to 0

def update_high_score():
    global score, high_score
    if score > high_score:
        high_score = score
        save_high_score()

# Game loop
clock = pygame.time.Clock()

# ...

def main():
    global player_x, player_y, player_speed, blaster_list, enemy_blaster_list, enemies, prizes, friends, asteroids, score
    global clock
    global game_over
    global lives
    load_high_score()
    lives = MAX_LIVES 
    show_main_menu()
    show_loading_screen()
    running = True
    game_over = False
    game_over_screen = GameOverScreen()

    clock = pygame.time.Clock()
    try:
        while running:
            keys = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_x:
                        create_blaster(player_x + player_width // 2, player_y)

            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= player_speed
            if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
                player_x += player_speed
            if keys[pygame.K_UP] and player_y > 0:
                player_y -= player_speed
            if keys[pygame.K_DOWN] and player_y < HEIGHT - player_height:
                player_y += player_speed

            # Update player position and collision rectangle
            update_player_collision_rect()

            for blaster in blaster_list:
                blaster.update()

            for enemy_blaster in enemy_blaster_list:
                enemy_blaster.update()

            blaster_list = [blaster for blaster in blaster_list if 0 < blaster.rect.y < HEIGHT]
            enemy_blaster_list = [blaster for blaster in enemy_blaster_list if 0 < blaster.rect.y < HEIGHT + blaster.rect.height]

            for friend in friends:
                friend.update()

            for blaster in blaster_list.copy():
                blaster.update()
                if 0 < blaster.rect.y < HEIGHT:
                    for enemy in enemies.copy():
                        if blaster.rect.colliderect(enemy.rect) and 0 < enemy.rect.y < HEIGHT:
                            blaster_list.remove(blaster)
                            enemies.remove(enemy)
                            score += 75
                            destruction_sound.play()
                            if 0 < enemy.rect.y < HEIGHT:
                                blaster_sound.play()
                            if random.random() <= enemy_blaster_probability:
                                enemy.shoot_blaster()

            enemies = [enemy for enemy in enemies if enemy.rect.y < HEIGHT]

            for asteroid in asteroids.copy():
                for blaster in blaster_list.copy():
                    if blaster.rect.colliderect(asteroid.rect):
                        blaster_list.remove(blaster)
                        asteroids.remove(asteroid)
                        score += 20
                        destruction_sound.play()

            for prize in prizes:
                prize.update()
                if prize.rect.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                    prizes.remove(prize)
                    score += 10
                    prize_sound.play()

            for enemy_blaster in enemy_blaster_list:
                if enemy_blaster.rect.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
                    game_over = True
                    destruction_sound.play()
                    lives -= 1  # Decrement lives on collision

            for enemy in enemies:
                enemy.update()
                if player_collision_rect.colliderect(enemy.rect):
                    game_over = True
                    destruction_sound.play()
                    lives -= 1  # Decrement lives on collision

            for asteroid in asteroids.copy():
                asteroid.update()
                if player_collision_rect.colliderect(asteroid.rect):
                    game_over = True
                    destruction_sound.play()
                    lives -= 1  # Decrement lives on collision

            screen.blit(bg_image, (0, 0))

            for blaster in blaster_list:
                screen.blit(blaster.image, (blaster.rect.x, blaster.rect.y))

            for enemy_blaster in enemy_blaster_list:
                screen.blit(enemy_blaster.image, (enemy_blaster.rect.x, enemy_blaster.rect.y))

            for friend in friends:
                screen.blit(friend.image, (friend.rect.x, friend.rect.y))

            for enemy in enemies:
                screen.blit(enemy_image, (enemy.rect.x, enemy.rect.y))

            for asteroid in asteroids:
                screen.blit(asteroid_image, (asteroid.rect.x, asteroid.rect.y))

            for prize in prizes:
                screen.blit(prize_image, (prize.rect.x, prize.rect.y))

            screen.blit(player_image, (player_x, player_y))

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))
            display_lives()
            pygame.display.flip()

            clock.tick(FPS)

            if random.random() <= enemy_probability:
                x = random.randint(0, WIDTH - enemy_image.get_width())
                enemies.append(Enemy(x, -200, enemy_speed, start_y=-200))

            if random.random() <= asteroid_probability:
                x = random.randint(0, WIDTH - asteroid_image.get_width())
                asteroids.append(Asteroid(x, 0, asteroid_speed, start_y=-1000))

            if random.random() <= prize_probability:
                x = random.randint(0, WIDTH - prize_image.get_width())
                prizes.append(Prize(x, 0, prize_speed, start_y=-2000))

            if random.random() <= friend_probability:
                x = random.randint(0, WIDTH - friend_image.get_width())
                friends.append(FlyingObject(x, -1000, friend_speed, friend_image))
            if lives <= 0:
                running = False
            pause_game(10)

    except Exception as e:
        print(f"An exception occurred: {e}")
        import traceback
        traceback.print_exc()
    finally:
        if lives <= 0:
            display_final_score(score)
            play_again = prompt_play_again()

            if play_again:
                reset_game()
                return   # ✅ restart cleanly
            else:
                pygame.quit()
                sys.exit()      
# Run the game
if __name__ == "__main__":
    while True:
        main()
