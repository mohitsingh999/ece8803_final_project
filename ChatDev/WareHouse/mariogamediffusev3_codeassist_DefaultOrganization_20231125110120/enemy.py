'''
This file defines the Enemy class which represents the enemy character.
'''
import pygame
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Set the enemy position
        self.x = 400
        self.y = 400
        # Set the enemy velocity
        self.vx = 1
        self.vy = 0
        # Set the enemy size
        self.width = 32
        self.height = 32
        # Set the enemy image
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 255, 0))
    def update(self):
        # Update the enemy position based on velocity
        self.x += self.vx
        self.y += self.vy
    def draw(self, screen):
        # Draw the enemy
        screen.blit(self.image, (self.x, self.y))