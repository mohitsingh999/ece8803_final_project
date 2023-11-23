# Ping Pong Game User Manual

Welcome to the Ping Pong Game! This user manual will guide you through the installation process, introduce the main functions of the game, and provide instructions on how to play.

## Installation

To install and run the Ping Pong Game, please follow these steps:

1. Ensure that you have Python installed on your computer. If not, you can download it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the game files from the provided source.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the game files.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter, numpy, and pandas.

5. Once the dependencies are installed, you are ready to play the game!

## Game Controls

The Ping Pong Game can be controlled using the keyboard. The controls are as follows:

- Use the **Left Arrow** key to move the paddle to the left.
- Use the **Right Arrow** key to move the paddle to the right.

## Playing the Game

To start the game, run the following command in the terminal or command prompt:

```
python main.py
```

This will launch the game window.

The objective of the game is to prevent the ball from hitting the bottom of the screen by moving the paddle. The ball will bounce off the paddle and the walls, and your goal is to keep it in play for as long as possible.

The game will continue until the ball hits the bottom of the screen. Your score will be displayed at the top of the game window.

To exit the game, simply close the game window.

## Customization

If you wish to customize the game, you can modify the code in the provided files. Here are some possible modifications you can make:

- Adjust the size of the game window by modifying the `width` and `height` parameters in the `Game` class in the `game.py` file.
- Change the color of the paddle and ball by modifying the `fill` parameter in the `Paddle` and `Ball` classes in the `paddle.py` and `ball.py` files, respectively.
- Modify the speed of the ball by changing the values of `self.x_speed` and `self.y_speed` in the `Ball` class in the `ball.py` file.

## Conclusion

Congratulations! You have successfully installed and learned how to play the Ping Pong Game. Enjoy playing and have fun!

If you have any questions or encounter any issues, please don't hesitate to reach out to our support team. Happy gaming!