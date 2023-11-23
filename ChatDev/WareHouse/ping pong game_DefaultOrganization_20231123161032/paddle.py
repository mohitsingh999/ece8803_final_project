'''
This file contains the Paddle class which represents the player's paddle.
'''
class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.paddle = self.canvas.create_rectangle(0, 0, 100, 10, fill="white")
        self.canvas.move(self.paddle, 350, 380)
        self.x_speed = 0
    def move_paddle(self, event):
        if event.keysym == "Left":
            self.x_speed = -2
        elif event.keysym == "Right":
            self.x_speed = 2
    def stop_paddle(self, event):
        self.x_speed = 0
    def update(self):
        self.canvas.move(self.paddle, self.x_speed, 0)
        paddle_pos = self.canvas.coords(self.paddle)
        if paddle_pos[0] < 0:
            self.x_speed = 0
        elif paddle_pos[2] > 800:
            self.x_speed = 0