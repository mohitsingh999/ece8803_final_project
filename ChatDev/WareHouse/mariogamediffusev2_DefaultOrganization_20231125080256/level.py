'''
This file defines the Level class which represents the game level.
'''
import pygame
class Level:
    def __init__(self):
        self.platforms = []
    def update(self):
        pass
    def render(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (255, 255, 255), platform)
    def add_platform(self, platform):
        self.platforms.append(platform)