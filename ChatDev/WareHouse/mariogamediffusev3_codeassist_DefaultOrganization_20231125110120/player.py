'''
This file defines the Player class which represents the player character.
'''
import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        # Set the player position
        self.x = 0
        self.y = 0
        # Set the player velocity
        self.vx = 0
        self.vy = 0
        # Set the player acceleration
        self.ax = 0
        self.ay = 0
        # Set the player size
        self.width = 32
        self.height = 32
        # Set the player image
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 0, 0))
        # Set the level reference
        self.level = level
    def update(self):
        # Apply gravity
        self.ay = 0.5
        # Update the player position based on velocity and acceleration
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy
        # Check for collisions with level blocks
        for y, row in enumerate(self.level.layout):
            for x, char in enumerate(row):
                if char == "#":
                    block_rect = pygame.Rect(x * 32, y * 32, 32, 32)
                    player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
                    if block_rect.colliderect(player_rect):
                        # Resolve the collision
                        if self.vx > 0:
                            self.x = block_rect.left - self.width
                        elif self.vx < 0:
                            self.x = block_rect.right
                        if self.vy > 0:
                            self.y = block_rect.top - self.height
                            self.vy = 0
                        elif self.vy < 0:
                            self.y = block_rect.bottom
    def draw(self, screen):
        # Draw the player
        screen.blit(self.image, (self.x, self.y))