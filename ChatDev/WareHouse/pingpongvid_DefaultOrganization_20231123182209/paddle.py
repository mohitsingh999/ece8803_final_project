'''
This file contains the Paddle class which represents the game paddle.
'''
import tkinter as tk
class Paddle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.paddle_image = tk.PhotoImage(file="paddle.png")
        self.paddle = self.canvas.create_image(5, 200, image=self.paddle_image)
        self.dy = 5
    def move(self, event):
        if event.keysym == "Up":
            self.canvas.move(self.paddle, 0, -self.dy)
        elif event.keysym == "Down":
            self.canvas.move(self.paddle, 0, self.dy)