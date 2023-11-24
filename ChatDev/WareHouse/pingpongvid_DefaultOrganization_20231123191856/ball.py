'''
The Ball class that represents the ball.
'''
import pygame
class Ball:
    def __init__(self, window_width, window_height, image):
        self.radius = 10
        self.x = window_width // 2
        self.y = window_height // 2
        self.speed_x = 3
        self.speed_y = 3
        self.image = pygame.transform.scale(image, (self.radius * 2, self.radius * 2))
    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y
        if self.x <= 0 or self.x >= window_width:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= window_height:
            self.speed_y *= -1
    def render(self, window):
        window.blit(self.image, (self.x - self.radius, self.y - self.radius))