import pygame
import random
import sys
import os

# Initialize pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ROAD_WIDTH = 500
PLAYER_WIDTH = 60
PLAYER_HEIGHT = 100
ENEMY_WIDTH = 60
ENEMY_HEIGHT = 100
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
ROAD_SPEED = 5
ENEMY_SPEED = 3
PLAYER_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
GREEN = (0, 128, 0)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Road Rash 2D")
clock = pygame.time.Clock()

# Load images
current_dir = os.path.dirname(os.path.abspath(__file__))

# Create simple placeholder graphics if images don't exist
def create_surface(width, height, color):
    surface = pygame.Surface((width, height))
    surface.fill(color)
    return surface

# Player bike
try:
    player_img = pygame.image.load(os.path.join(current_dir, 'player_bike.png'))
    player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
except:
    player_img = create_surface(PLAYER_WIDTH, PLAYER_HEIGHT, RED)
    pygame.draw.polygon(player_img, BLACK, [(30, 20), (30, 80), (45, 90), (15, 90)])
    
# Enemy bike
try:
    enemy_img = pygame.image.load(os.path.join(current_dir, 'enemy_bike.png'))
    enemy_img = pygame.transform.scale(enemy_img, (ENEMY_WIDTH, ENEMY_HEIGHT))
except:
    enemy_img = create_surface(ENEMY_WIDTH, ENEMY_HEIGHT, GREEN)
    pygame.draw.polygon(enemy_img, BLACK, [(30, 20), (30, 80), (45, 90), (15, 90)])

# Obstacle
try:
    obstacle_img = pygame.image.load(os.path.join(current_dir, 'obstacle.png'))
    obstacle_img = pygame.transform.scale(obstacle_img, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))
except:
    obstacle_img = create_surface(OBSTACLE_WIDTH, OBSTACLE_HEIGHT, BLACK)

# Road stripes for animation
stripe_height = 50
stripe_width = 10
stripe_gap = 30
stripes = []
for i in range(0, SCREEN_HEIGHT + stripe_height, stripe_height + stripe_gap):
    stripes.append(pygame.Rect((SCREEN_WIDTH - ROAD_WIDTH) // 2 + ROAD_WIDTH // 2 - stripe_width // 2, i, stripe_width, stripe_height))

# Player class
class Player:
    def __init__(self):
        self.rect = player_img.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 50
        self.speed_x = 0
        self.speed_y = 0
        self.score = 0
        self.speed = PLAYER_SPEED
        
    def update(self):
        # Update position based on speed
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Keep player on the road
        road_left = (SCREEN_WIDTH - ROAD_WIDTH) // 2
        road_right = road_left + ROAD_WIDTH
        
        if self.rect.left < road_left:
            self.rect.left = road_left
        if self.rect.right > road_right:
            self.rect.right = road_right
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            
    def draw(self):
        screen.blit(player_img, self.rect)

# Enemy class
class Enemy:
    def __init__(self):
        self.rect = enemy_img.get_rect()
        road_left = (SCREEN_WIDTH - ROAD_WIDTH) // 2
        self.rect.x = random.randint(road_left, road_left + ROAD_WIDTH - ENEMY_WIDTH)
        self.rect.y = -ENEMY_HEIGHT
        self.speed = random.randint(2, 5)
        
    def update(self):
        self.rect.y += self.speed
        
    def draw(self):
        screen.blit(enemy_img, self.rect)

# Obstacle class
class Obstacle:
    def __init__(self):
        self.rect = obstacle_img.get_rect()
        road_left = (SCREEN_WIDTH - ROAD_WIDTH) // 2
        self.rect.x = random.randint(road_left, road_left + ROAD_WIDTH - OBSTACLE_WIDTH)
        self.rect.y = -OBSTACLE_HEIGHT
        self.speed = ROAD_SPEED
        
    def update(self):
        self.rect.y += self.speed
        
    def draw(self):
        screen.blit(obstacle_img, self.rect)

# Game functions
def draw_road():
    # Draw road
    road_rect = pygame.Rect((SCREEN_WIDTH - ROAD_WIDTH) // 2, 0, ROAD_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, GRAY, road_rect)
    
    # Draw stripes
    for stripe in stripes:
        pygame.draw.rect(screen, WHITE, stripe)
        
    # Draw side grass
    pygame.draw.rect(screen, GREEN, (0, 0, (SCREEN_WIDTH - ROAD_WIDTH) // 2, SCREEN_HEIGHT))
    pygame.draw.rect(screen, GREEN, ((SCREEN_WIDTH + ROAD_WIDTH) // 2, 0, (SCREEN_WIDTH - ROAD_WIDTH) // 2, SCREEN_HEIGHT))

def update_stripes():
    for stripe in stripes:
        stripe.y += ROAD_SPEED
        if stripe.top > SCREEN_HEIGHT:
            stripe.bottom = 0

def show_game_over():
    font = pygame.font.SysFont(None, 74)
    text = font.render("GAME OVER", True, RED)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    
    score_font = pygame.font.SysFont(None, 36)
    score_text = score_font.render(f"Score: {player.score}", True, WHITE)
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    
    restart_font = pygame.font.SysFont(None, 30)
    restart_text = restart_font.render("Press R to restart or Q to quit", True, WHITE)
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
    
    screen.fill(BLACK)
    screen.blit(text, text_rect)
    screen.blit(score_text, score_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
        clock.tick(FPS)

def show_hud():
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    speed_text = font.render(f"Speed: {player.speed}", True, WHITE)
    
    screen.blit(score_text, (10, 10))
    screen.blit(speed_text, (10, 50))

# Main game loop
def game_loop():
    global player, enemies, obstacles
    
    player = Player()
    enemies = []
    obstacles = []
    
    enemy_spawn_timer = 0
    obstacle_spawn_timer = 0
    
    running = True
    game_over = False
    
    while running:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.speed_x = -player.speed
                if event.key == pygame.K_RIGHT:
                    player.speed_x = player.speed
                if event.key == pygame.K_UP:
                    player.speed_y = -player.speed
                if event.key == pygame.K_DOWN:
                    player.speed_y = player.speed
            
            # Handle key releases
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.speed_x < 0:
                    player.speed_x = 0
                if event.key == pygame.K_RIGHT and player.speed_x > 0:
                    player.speed_x = 0
                if event.key == pygame.K_UP and player.speed_y < 0:
                    player.speed_y = 0
                if event.key == pygame.K_DOWN and player.speed_y > 0:
                    player.speed_y = 0
        
        if not game_over:
            # Update game elements
            player.update()
            update_stripes()
            
            # Spawn enemies
            enemy_spawn_timer += 1
            if enemy_spawn_timer >= FPS * 2:  # Spawn every 2 seconds
                enemies.append(Enemy())
                enemy_spawn_timer = 0
            
            # Spawn obstacles
            obstacle_spawn_timer += 1
            if obstacle_spawn_timer >= FPS * 3:  # Spawn every 3 seconds
                obstacles.append(Obstacle())
                obstacle_spawn_timer = 0
            
            # Update enemies
            for enemy in enemies[:]:
                enemy.update()
                if enemy.rect.top > SCREEN_HEIGHT:
                    enemies.remove(enemy)
                    player.score += 10
            
            # Update obstacles
            for obstacle in obstacles[:]:
                obstacle.update()
                if obstacle.rect.top > SCREEN_HEIGHT:
                    obstacles.remove(obstacle)
                    player.score += 5
            
            # Check for collisions
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    game_over = True
            
            for obstacle in obstacles:
                if player.rect.colliderect(obstacle.rect):
                    game_over = True
            
            # Draw everything
            screen.fill(BLACK)
            draw_road()
            player.draw()
            
            for enemy in enemies:
                enemy.draw()
            
            for obstacle in obstacles:
                obstacle.draw()
            
            show_hud()
            
            # Increase difficulty over time
            if player.score > 0 and player.score % 100 == 0:
                player.speed += 0.1
            
            pygame.display.flip()
            clock.tick(FPS)
        else:
            show_game_over()
            game_over = False
            game_loop()  # Restart the game
    
    pygame.quit()
    sys.exit()

# Start the game
if __name__ == "__main__":
    game_loop()
