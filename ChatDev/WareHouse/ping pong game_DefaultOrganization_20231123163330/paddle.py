'''
This file contains the Paddle class which represents the paddle in the ping pong game.
'''
import tkinter as tk
class Paddle:
    def __init__(self, canvas, paddle_image):
        self.canvas = canvas
        self.paddle = self.canvas.create_image(400, 580, image=paddle_image)
        self.dx = 10
    def move_paddle(self, event):
        if event.keysym == "Left":
            self.canvas.move(self.paddle, -self.dx, 0)
        elif event.keysym == "Right":
            self.canvas.move(self.paddle, self.dx, 0)
    def move(self):
        paddle_pos = self.canvas.coords(self.paddle)
        if paddle_pos[0] <= 0:
            self.canvas.move(self.paddle, self.dx, 0)
        elif paddle_pos[2] >= 800:
            self.canvas.move(self.paddle, -self.dx, 0)