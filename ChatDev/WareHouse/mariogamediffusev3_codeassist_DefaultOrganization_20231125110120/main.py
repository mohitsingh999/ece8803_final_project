'''
This is the main file that initializes the game and handles the game loop.
'''
import pygame
from level import Level
from player import Player
from enemy import Enemy
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Mario Game")
        self.clock = pygame.time.Clock()
        # Create the level
        self.level = Level()
        # Create the player
        self.player = Player(self.level)
        # Create the enemies
        self.enemy1 = Enemy()
        self.enemy2 = Enemy()
        self.enemy3 = Enemy()
        self.enemies = pygame.sprite.Group()
        self.enemies.add(self.enemy1)
        self.enemies.add(self.enemy2)
        self.enemies.add(self.enemy3)
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def update(self):
        self.player.update()
        self.enemy1.update()
        self.enemy2.update()
        self.enemy3.update()
    def render(self):
        self.screen.fill((0, 0, 0))
        self.level.draw(self.screen)
        self.player.draw(self.screen)
        self.enemy1.draw(self.screen)
        self.enemy2.draw(self.screen)
        self.enemy3.draw(self.screen)
        pygame.display.flip()
if __name__ == "__main__":
    game = Game()
    game.run()