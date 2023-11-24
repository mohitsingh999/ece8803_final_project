'''
The Paddle class that represents the player's paddle.
'''
import pygame
class Paddle:
    def __init__(self, window_width, window_height, image):
        self.width = 100
        self.height = 20
        self.x = (window_width - self.width) // 2
        self.y = window_height - self.height - 10
        self.speed = 5
        self.image = pygame.transform.scale(image, (self.width, self.height))
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < window_width - self.width:
            self.x += self.speed
    def render(self, window):
        window.blit(self.image, (self.x, self.y))