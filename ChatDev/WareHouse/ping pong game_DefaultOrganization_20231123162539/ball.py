import pygame
class Ball:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.radius = 10
        self.speed = speed
        self.direction_x = 1
        self.direction_y = 1
    def move(self):
        self.x += self.speed * self.direction_x
        self.y += self.speed * self.direction_y
        if self.y <= 0 or self.y >= 590:
            self.direction_y *= -1
    def check_collision(self, paddles):
        for paddle in paddles:
            if (
                self.x + self.radius >= paddle.x
                and self.x - self.radius <= paddle.x + paddle.width
                and self.y + self.radius >= paddle.y
                and self.y - self.radius <= paddle.y + paddle.height
            ):
                self.direction_x *= -1
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)