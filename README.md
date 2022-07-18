# Tic Tac Toe Game - Pygame
## [Watch it on youtube](https://www.youtube.com/watch?v=FP4UAbs1Eik)

### Note: I was forced to make this long README.md 🙂

## **Description:**
### Technologies used:

- Python
- Pygame

### Concepts in the project:

- Game Development
- Data Structure (list, tuple)
- OOP
- Algorithms Design

## About this project
Tic Tac Toe is my final project for CS50P with Harvard University Online. This game was made using Python and Pygame libraries.

## **main.py**

The main.py file contains all the code that will be executed when the program is run. It import Pygame library classes Block and Board from the file board.py, which represent block in the board and the board itself, respectively.

The main.py file first inits the pygame library and declares colour variables that will be used to illustrate the game in the program. The main function in this file is where all others functions are called, and the game is controlled in this main function. 

The main function first initialise some variables like the score of two player and the winner, then it runs a while True loop that will end when the user click exit. In the loop, the function gets the input like mouse clicks and key pressed, then executes the function accordingly.

The function draw is responsible for drawing the initial window and board into the screen as an interface of the game. The function draw first sets the background of the window to be black, then draw the board onto the window and then displays the current score between two players.

The draw_win function is called when there is a winner, and its responsibility is to display the winner of the round. The draw_score function is responsible for drawing the score for X and O players and Tie.

## **board.py**

The board.py import the Pygame library and then initialises it to draw the board and the cells in the window. Colours variables like Black and White are also declared in this file. This file contains two classes, Board and Block, to represent the board and cell of the tic tac toe game.

The Board class init function takes 5 arguments to initialise essential data and information for the class to function like the window, classes, width and height. 

The Board class also contains function like draw for drawing the board into the window, the tick function to make a input the player move, the checkWin and checkTie function to decide when the round will be end and finally the reset function which will reset everything.

The Block class represent a cell in the board of tic tac toe which takes 7 arguments to initialise. It will be drawn into the window if the cell have the value of X or O. This class has functions such as draw, assign and reset.

### Creator - **Minh Vy Ha**
![preview img](/preview.png)
