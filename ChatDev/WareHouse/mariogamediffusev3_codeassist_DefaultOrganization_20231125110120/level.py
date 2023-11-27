'''
This file defines the Level class which represents the game level.
'''
import pygame
class Level:
    def __init__(self):
        # Define the level layout
        self.layout = [
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    ",
            "                    "
        ]
        # Load the level images
        self.block_image = pygame.image.load("mario.png")
    def draw(self, screen):
        # Draw the level blocks
        for y, row in enumerate(self.layout):
            for x, char in enumerate(row):
                if char == "#":
                    screen.blit(self.block_image, (x * 32, y * 32))