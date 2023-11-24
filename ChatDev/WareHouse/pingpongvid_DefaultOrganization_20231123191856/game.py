'''
The main file that initializes the game window and starts the game loop.
'''
import pygame
from paddle import Paddle
from ball import Ball
from video_player import VideoPlayer
# Initialize Pygame
pygame.init()
# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping Pong Game")
# Load images
background_image = pygame.image.load("background.png")
ball_image = pygame.image.load("ball.png")
button_exit_image = pygame.image.load("button_exit.png")
button_pause_image = pygame.image.load("button_pause.png")
button_restart_image = pygame.image.load("button_restart.png")
button_resume_image = pygame.image.load("button_resume.png")
button_start_image = pygame.image.load("button_start.png")
paddle_image = pygame.image.load("paddle.png")
score_board_image = pygame.image.load("score_board.png")
video_player_image = pygame.image.load("video_player.png")
# Create objects
paddle = Paddle(WINDOW_WIDTH, WINDOW_HEIGHT, paddle_image)
ball = Ball(WINDOW_WIDTH, WINDOW_HEIGHT, ball_image)
video_player = VideoPlayer(WINDOW_WIDTH, WINDOW_HEIGHT, video_player_image)
# Game loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update objects
    paddle.update()
    ball.update()
    video_player.update()
    # Render objects
    window.blit(background_image, (0, 0))  # Draw the background image
    video_player.render(window)
    paddle.render(window)
    ball.render(window)
    window.blit(score_board_image, (10, 10))  # Draw the score board
    window.blit(button_exit_image, (10, WINDOW_HEIGHT - 50))  # Draw the exit button
    window.blit(button_pause_image, (80, WINDOW_HEIGHT - 50))  # Draw the pause button
    window.blit(button_restart_image, (150, WINDOW_HEIGHT - 50))  # Draw the restart button
    window.blit(button_resume_image, (220, WINDOW_HEIGHT - 50))  # Draw the resume button
    window.blit(button_start_image, (290, WINDOW_HEIGHT - 50))  # Draw the start button
    pygame.display.flip()  # Update the window
    clock.tick(60)  # Limit the frame rate to 60 FPS
# Quit the game
pygame.quit()