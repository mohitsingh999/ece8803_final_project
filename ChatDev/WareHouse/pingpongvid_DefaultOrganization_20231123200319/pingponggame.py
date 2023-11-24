import tkinter as tk
import cv2
from PIL import Image, ImageTk
class PingPongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Pong Game")
        self.root.geometry("800x600")
        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.video = cv2.VideoCapture("background_video.mp4")
        # Load images
        self.ball_image = ImageTk.PhotoImage(Image.open("ball.png").resize((50, 50)))
        self.game_over_image = ImageTk.PhotoImage(Image.open("game_over.png").resize((400, 200)))
        self.obstacle_image = ImageTk.PhotoImage(Image.open("obstacle.png").resize((50, 50)))
        self.paddle_image = ImageTk.PhotoImage(Image.open("paddle.png").resize((100, 20)))
        self.pause_button_image = ImageTk.PhotoImage(Image.open("pause_button.png").resize((50, 50)))
        self.power_up_image = ImageTk.PhotoImage(Image.open("power_up.png").resize((50, 50)))
        self.reset_button_image = ImageTk.PhotoImage(Image.open("reset_button.png").resize((50, 50)))
        self.score_board_image = ImageTk.PhotoImage(Image.open("score_board.png").resize((200, 100)))
        self.start_button_image = ImageTk.PhotoImage(Image.open("start_button.png").resize((100, 50)))
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Pong Game")
        self.root.geometry("800x600")
        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.video = cv2.VideoCapture("background_video.mp4")
        # Load images
        self.ball_image = ImageTk.PhotoImage(Image.open("ball.png").resize((50, 50)))
        self.game_over_image = ImageTk.PhotoImage(Image.open("game_over.png").resize((400, 200)))
        self.obstacle_image = ImageTk.PhotoImage(Image.open("obstacle.png").resize((50, 50)))
        self.paddle_image = ImageTk.PhotoImage(Image.open("paddle.png").resize((100, 20)))
        self.pause_button_image = ImageTk.PhotoImage(Image.open("pause_button.png").resize((50, 50)))
        self.power_up_image = ImageTk.PhotoImage(Image.open("power_up.png").resize((50, 50)))
        self.reset_button_image = ImageTk.PhotoImage(Image.open("reset_button.png").resize((50, 50)))
        self.score_board_image = ImageTk.PhotoImage(Image.open("score_board.png").resize((200, 100)))
        self.start_button_image = ImageTk.PhotoImage(Image.open("start_button.png").resize((100, 50)))