'''
This file contains the Ball class which represents the game ball.
'''
import random
class Ball:
    def __init__(self, canvas, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.ball = self.canvas.create_oval(0, 0, 20, 20, fill="white")
        self.canvas.move(self.ball, 390, 190)
        self.x_speed = random.choice([-2, 2])
        self.y_speed = -2
    def move_ball(self):
        self.canvas.move(self.ball, self.x_speed, self.y_speed)
        ball_pos = self.canvas.coords(self.ball)
        if ball_pos[0] < 0 or ball_pos[2] > 800:
            self.x_speed *= -1
        if ball_pos[1] < 0 or ball_pos[3] > 400:
            self.y_speed *= -1
        if self.hit_paddle(ball_pos):
            self.y_speed = -2
        self.canvas.after(10, self.move_ball)
    def hit_paddle(self, ball_pos):
        paddle_pos = self.canvas.coords(self.paddle.paddle)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                return True
        return False