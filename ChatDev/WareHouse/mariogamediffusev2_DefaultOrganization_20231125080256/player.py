'''
This file defines the Player class which represents the player character.
'''
import pygame
import random 

# Constants
WIDTH, HEIGHT = 600, 400
ENEMY_SIZE = 30
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Load player image
player_image = pygame.image.load("mario.png")  # Replace with the path to your player image
player_image = pygame.transform.scale(player_image, (50, 50))  # Adjust the size as needed

# Load enemy image
enemy_image = pygame.image.load("enemy.png")  # Replace with the path to your player image
enemy_image = pygame.transform.scale(enemy_image, (50, 50))  # Adjust the size as needed

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_image
        self.rect = self.image.get_rect()
        self.velocity = pygame.Vector2(0, 0)
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        elif keys[pygame.K_DOWN]:
            self.velocity.y = 5
        elif keys[pygame.K_UP]:
            self.velocity.y = -5
        else:
            self.velocity.x = 0
            self.velocity.y = 0
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y
    def render(self, screen):
        screen.blit(self.image, self.rect)

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.speed = 4

    def update(self):
        # Move the enemy randomly
        self.rect.x += random.choice([-self.speed, 0, self.speed])
        self.rect.y += random.choice([-self.speed, 0, self.speed])

        # Check boundaries
        self.rect.x = max(0, min(self.rect.x, WIDTH - ENEMY_SIZE))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - ENEMY_SIZE))

    def render(self, screen):
        screen.blit(self.image, self.rect)
