import pygame
from paddle import Paddle
from ball import Ball
class GameWindow:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Ping Pong Game")
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.paddle1 = Paddle(20, height // 2 - 50)
        self.paddle2 = Paddle(width - 40, height // 2 - 50)
        self.ball = Ball(width // 2, height // 2, 5)
    def run(self):
        while self.is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.paddle1.move_up()
                    elif event.key == pygame.K_DOWN:
                        self.paddle1.move_down()
            self.ball.move()
            self.ball.check_collision([self.paddle1, self.paddle2])
            self.screen.fill((0, 0, 0))
            self.paddle1.draw(self.screen)
            self.paddle2.draw(self.screen)
            self.ball.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()
if __name__ == "__main__":
    game = GameWindow(800, 600)
    game.run()