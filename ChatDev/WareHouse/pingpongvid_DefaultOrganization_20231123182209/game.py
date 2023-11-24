'''
This file contains the Game class which manages the game logic.
'''
import tkinter as tk
from ball import Ball
from paddle import Paddle
class Game:
    def __init__(self, window):
        self.window = window
        self.canvas = tk.Canvas(self.window, width=800, height=400, bg="black")
        self.canvas.pack()
        self.ball = Ball(self.canvas)
        self.paddle = Paddle(self.canvas)
        self.canvas.bind("<KeyPress>", self.paddle.move)
        self.canvas.focus_set()
    def start(self):
        self.ball.move()
    def stop(self):
        self.ball.stop()