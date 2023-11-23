'''
This file contains the Game class which represents the ping pong game.
'''
import tkinter as tk
from PIL import Image, ImageTk
from paddle import Paddle
class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Pong Game")
        self.root.geometry("800x600")
        self.canvas = tk.Canvas(self.root, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.load_images()
        self.ball = Ball(self.canvas, self.ball_image)
        self.paddle = Paddle(self.canvas, self.paddle_image)
        self.canvas.bind("<KeyPress>", self.paddle.move_paddle)
        self.canvas.focus_set()
    def load_images(self):
        self.ball_image = ImageTk.PhotoImage(Image.open("ball.png").resize((50, 50)))
        self.paddle_image = ImageTk.PhotoImage(Image.open("paddle.png").resize((100, 10)))
    def start(self):
        self.ball.move()
        self.paddle.move()
class Ball:
    def __init__(self, canvas, ball_image):
        self.canvas = canvas
        self.ball = self.canvas.create_image(395, 295, image=ball_image)
        self.dx = 1
        self.dy = -1
    def move(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        self.check_collision()
        self.canvas.after(10, self.move)
    def check_collision(self):
        ball_pos = self.canvas.coords(self.ball)
        #paddle_pos = self.canvas.coords(self.canvas.paddle)
        if ball_pos[1] <= 0 or ball_pos[1] >= 600:
            self.dy *= -1
        if ball_pos[0] <= 0 or ball_pos[0] >= 800:
            self.dx *= -1
        # if ball_pos[1] >= paddle_pos[1] and ball_pos[0] >= paddle_pos[0] and ball_pos[2] <= paddle_pos[2]:
        #     self.dy *= -1
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
        elif paddle_pos[0] >= 800:
            self.canvas.move(self.paddle, -self.dx, 0)