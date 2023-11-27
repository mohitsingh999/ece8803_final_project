'''
This is the main file that initializes the game and handles the game loop.
'''
import pygame
from level import Level
from player import Player
# Initialize Pygame
pygame.init()
# Set up the game window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mario Game")
# Create the level
level = Level()
# Create the player
player = Player(level)
# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the player
    player.update()
    # Draw the level and player
    screen.fill((0, 0, 0))
    level.draw(screen)
    player.draw(screen)
    # Update the display
    pygame.display.flip()
    # Limit the frame rate
    clock.tick(60)
# Quit the game
pygame.quit()