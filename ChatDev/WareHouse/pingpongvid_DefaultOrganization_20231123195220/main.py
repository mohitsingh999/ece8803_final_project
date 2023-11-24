'''
This is the main file of the ping pong game with an embedded video window for the background.
'''
import tkinter as tk
from PIL import Image, ImageTk
import cv2
class PingPongGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ping Pong Game")
        self.root.geometry("800x600")
        self.video_frame = tk.Frame(self.root)
        self.video_frame.pack()
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.pack()
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack()
        self.cap = cv2.VideoCapture("background_video.mp4")
        self.show_video()
        self.ball_image = ImageTk.PhotoImage(Image.open("ball.png").resize((50, 50)))
        self.net_image = ImageTk.PhotoImage(Image.open("net.png").resize((800, 10)))
        self.paddle_image = ImageTk.PhotoImage(Image.open("paddle.png").resize((100, 20)))
        self.pause_button_image = ImageTk.PhotoImage(Image.open("pause_button.png").resize((50, 50)))
        self.quit_button_image = ImageTk.PhotoImage(Image.open("quit_button.png").resize((50, 50)))
        self.restart_button_image = ImageTk.PhotoImage(Image.open("restart_button.png").resize((50, 50)))
        self.resume_button_image = ImageTk.PhotoImage(Image.open("resume_button.png").resize((50, 50)))
        self.score_board_image = ImageTk.PhotoImage(Image.open("score_board.png").resize((150, 50)))
        self.start_button_image = ImageTk.PhotoImage(Image.open("start_button.png").resize((100, 50)))
        self.root.mainloop()
    def show_video(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (800, 600))
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            self.video_label.configure(image=img)
            self.video_label.image = img
            self.canvas.after(10, self.show_video)
        else:
            self.cap.release()
if __name__ == "__main__":
    root = tk.Tk()
    game = PingPongGame(root)