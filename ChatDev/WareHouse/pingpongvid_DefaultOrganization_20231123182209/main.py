'''
This is the main file of the ping pong game with a video window.
'''
import tkinter as tk
from game import Game
# Create the main window
window = tk.Tk()
window.title("Ping Pong Game")
# Create the game instance
game = Game(window)
# Start the game loop
game.start()
# Run the main event loop
window.mainloop()