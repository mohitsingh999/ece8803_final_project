'''
The VideoPlayer class that handles the embedded video window.
'''
import pygame
class VideoPlayer:
    def __init__(self, window_width, window_height, image):
        self.video_width = 400
        self.video_height = 300
        self.x = (window_width - self.video_width) // 2
        self.y = (window_height - self.video_height) // 2
        self.video = pygame.movie.Movie("background_video.mp4")
        self.video.set_display(pygame.Rect(self.x, self.y, self.video_width, self.video_height))
        self.video.play()
        self.image = pygame.transform.scale(image, (self.video_width, self.video_height))
    def update(self):
        self.video.get_busy()
    def render(self, window):
        window.blit(self.image, (self.x, self.y))