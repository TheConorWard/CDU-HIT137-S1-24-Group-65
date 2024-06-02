import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Side-Scrolling Game')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Player settings
player_speed = 5
player_jump_power = 22
player_gravity = 0.5

# Initial enemy settings
base_enemy_speed = 2

# Collectible settings
collectible_size = 20

# Load player image
player_image = pygame.image.load("/Users/ashrietalipuan/Desktop/kat.png")  # Update the path to your image
player_width = player_image.get_width()
player_height = player_image.get_height()

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = SCREEN_HEIGHT - player_height - 50
        self.change_x = 0
        self.change_y = 0
        self.jumping = False
        self.health = 100
        self.lives = 3
        self.score = 0

    def update(self):
        self.rect.x += self.change_x

        # Apply gravity
        self.change_y += player_gravity
        self.rect.y += self.change_y

        # Prevent moving out of screen bounds
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > SCREEN_WIDTH - player_width:
            self.rect.x = SCREEN_WIDTH - player_width

        # Prevent falling through the floor
        if self.rect.y > SCREEN_HEIGHT - player_height - 50:
            self.rect.y = SCREEN_HEIGHT - player_height - 50
            self.jumping = False
            self.change_y = 0

    def jump(self):
        if not self.jumping:
            self.change_y = -player_jump_power
            self.jumping = True

    def shoot(self):
        projectile = Projectile(self.rect.x + player_width, self.rect.y + player_height // 2)
        all_sprites.add(projectile)
        projectiles.add(projectile)

# Load enemy image
enemy_image = pygame.image.load("/Users/ashrietalipuan/Desktop/enemy.png")  # Update the path to your image
enemy_width = enemy_image.get_width()
enemy_height = enemy_image.get_height()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.change_x = -speed

    def update(self):
        self.rect.x += self.change_x
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([10, 5])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 7

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > SCREEN_WIDTH:
            self.kill()

# Load collectible image
collectible_image = pygame.image.load("/Users/ashrietalipuan/Desktop/money.png")  # Update the path to your image
collectible_width = collectible_image.get_width()
collectible_height = collectible_image.get_height()

# Collectible class
class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = collectible_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
collectibles = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Function to load a level
def load_level(level):
    global all_sprites, enemies, collectibles, projectiles, player
    all_sprites.empty()
    enemies.empty()
    projectiles.empty()
    collectibles.empty()

    # Increase enemy speed by 0.5 for each level
    enemy_speed = base_enemy_speed + (level - 1) * 0.5

    # Add player to all_sprites
    all_sprites.add(player)
    player.rect.x = 50
    player.rect.y = SCREEN_HEIGHT - player_height - 50

    # Create enemies
    for i in range(level + 3):
        enemy = Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), SCREEN_HEIGHT - enemy_height - 50, enemy_speed)
        all_sprites.add(enemy)
        enemies.add(enemy)

    # Create collectibles
    for i in range(10):
        collectible = Collectible(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT - collectible_height))
        all_sprites.add(collectible)
        collectibles.add(collectible)

# Load the first level
current_level = 1
load_level(current_level)

# Fonts
score_font = pygame.font.SysFont('Comic Sans MS', 30)
health_font = pygame.font.SysFont('Arial', 24, bold=True)
level_font = pygame.font.SysFont('Times New Roman', 26, italic=True)

# Game loop
run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.change_x = -player_speed
            elif event.key == pygame.K_RIGHT:
                player.change_x = player_speed
            elif event.key == pygame.K_SPACE:  # Use spacebar for jumping
                player.jump()
            elif event.key == pygame.K_z:
                player.shoot()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.change_x = 0

    # Update
    all_sprites.update()

    # Collision detection between player and enemies
    if pygame.sprite.spritecollide(player, enemies, True):
        player.health -= 10
        if player.health <= 0:
            player.lives -= 1
            player.health = 100
            if player.lives == 0:
                run = False

    # Collision detection between player and collectibles
    if pygame.sprite.spritecollide(player, collectibles, True):
        player.score += 10

    # Collision detection between projectiles and enemies
    for projectile in projectiles:
        hit_enemies = pygame.sprite.spritecollide(projectile, enemies, True)
        if hit_enemies:
            projectile.kill()
            player.score += 5

    # Check if all collectibles are collected
    if len(collectibles) == 0:
        current_level += 1
        load_level(current_level)

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)

    # Render score, health, and level text
    score_text = score_font.render(f'Score: {player.score}', True, GREEN)
    health_text = health_font.render(f'Health: {player.health}', True, RED)
    level_text = level_font.render(f'Level: {current_level}', True, BLUE)

    # Display score, health, and level on screen
    screen.blit(score_text, (10, 10))
    screen.blit(health_text, (10, 50))
    screen.blit(level_text, (10, 90))

    # Refresh screen
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
