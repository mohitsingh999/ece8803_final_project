import pygame
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 100
        self.speed = 5
    def move_up(self):
        self.y -= self.speed
    def move_down(self):
        self.y += self.speed
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height))