'''
This file contains the Ball class which represents the game ball.
'''
import tkinter as tk
class Ball:
    def __init__(self, canvas):
        self.canvas = canvas
        self.ball_image = tk.PhotoImage(file="ball.png")
        self.ball = self.canvas.create_image(400, 200, image=self.ball_image)
        self.dx = 2
        self.dy = 2
        self.is_moving = False
    def move(self):
        self.is_moving = True
        self.canvas.move(self.ball, self.dx, self.dy)
        x1, y1 = self.canvas.coords(self.ball)
        if x1 <= 0 or y1 >= 800:
            self.dx *= -1
        if y1 <= 0 or x1 >= 400:
            self.dy *= -1
        if self.is_moving:
            self.canvas.after(10, self.move)
    def stop(self):
        self.is_moving = False