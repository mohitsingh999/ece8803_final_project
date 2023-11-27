'''
This is the main file that initializes the game and runs the game loop.
'''
import pygame
from level import Level
from player import Player
from player import Enemy
import cv2
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Mario Game")
        self.clock = pygame.time.Clock()
        # Load the video
        self.video = cv2.VideoCapture("background.mp4")
        self.success, self.video_image = self.video.read()
        self.running = True
        self.level = Level()
        self.player = Player()
        self.enemy1 = Enemy()
        self.enemy2 = Enemy()
        self.enemy3 = Enemy()
        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.enemy1)
        self.enemies.add(self.enemy2)
        self.enemies.add(self.enemy3)
    def run(self):
        i = 0
        while self.running:
            i += 1
            # Check for collisions
            collisions = pygame.sprite.spritecollide(self.player, self.enemies, False)
            if collisions:
                print("Player hit an enemy!")
                self.running=False
            self.clock.tick(60)

            if i % 6 == 0:
                self.success, self.video_image = self.video.read()
            if self.success:
                self.video_surf = pygame.image.frombuffer(self.video_image.tobytes(), self.video_image.shape[1::-1], "BGR")
            else:
                self.running = False
            self.handle_events()
            self.update()
            self.render()
        pygame.quit()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        self.player.update()
        self.level.update()
        self.enemy1.update()        
        self.enemy2.update()
        self.enemy3.update()

    def render(self):
        #self.screen.fill((0, 255, 0))
        self.screen.blit(self.video_surf, (0, 0))
        self.level.render(self.screen)
        self.player.render(self.screen)
        self.enemy1.render(self.screen)
        self.enemy2.render(self.screen)
        self.enemy3.render(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()