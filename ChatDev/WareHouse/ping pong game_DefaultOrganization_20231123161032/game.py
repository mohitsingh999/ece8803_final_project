'''
This file contains the Game class which manages the game logic.
'''
import tkinter as tk
from paddle import Paddle
from ball import Ball
class Game:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="black")
        self.canvas.pack()
        self.paddle = Paddle(self.canvas)
        self.ball = Ball(self.canvas, self.paddle)
    def start(self):
        self.canvas.bind("<KeyPress>", self.paddle.move_paddle)
        self.canvas.bind("<KeyRelease>", self.paddle.stop_paddle)
        self.ball.move_ball()
#paddle.py