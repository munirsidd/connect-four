# Connect Four Game

## Introduction

Connect Four is a classic two-player strategy game where the goal is to be the first to form a horizontal, vertical, or diagonal line of four checkers of your color. This Python implementation of Connect Four provides a versatile game board, various player classes, and a script to play the game.

## Game Components

### `board.py`

The `board.py` file contains the core component of the game, the `Board` class. This class represents the Connect Four game board and provides the following functionalities:

- Initializing the game board with a specified height and width.
- Adding checkers ('X' or 'O') to the board in specified columns.
- Resetting the board to start a new game.
- Checking if a column can accept a new checker.
- Checking if the board is completely filled.
- Removing checkers from the board.
- Determining if a player has won horizontally, vertically, or diagonally.
- Combining these functions to determine the game's outcome.

### `player.py`

The `player.py` file defines the `Player` class, representing a player in the Connect Four game. The class includes the following features:

- Initialization with a checker ('X' or 'O') and move count.
- The ability to retrieve the opponent's checker.
- Interactive input for human players to choose columns for their moves.

### `random_player.py`

The `random_player.py` file introduces the `RandomPlayer` class, a subclass of `Player`. This player is an unintelligent computer opponent that selects its moves randomly.

### `AI_player.py`

The `AI_player.py` file includes the `AIPlayer` class, a subclass of `Player`. The AIPlayer is an intelligent computer opponent that uses a scoring algorithm and lookahead depth to make strategic moves.

## Playing the Game

To play the Connect Four game, follow these steps:

1. Ensure you have all the necessary files (`board.py`, `player.py`, `random_player.py`, `AI_player.py`, and `connect_four.py`) in the same directory.

2. Start the game by running the `connect_four.py` script.

3. Choose Players:
   - To play against another human player, create two instances of the `Player` class, specifying 'X' and 'O' as checkers. Example:
     ```python
     player1 = Player('X')
     player2 = Player('O')
     ```
   - To play against a random computer player, create a `Player` instance for the human player and a `RandomPlayer` instance for the computer player. Example:
     ```python
     human_player = Player('X')
     computer_player = RandomPlayer('O')
     ```
   - To play against an AI computer player, create a `Player` instance for the human player and an `AIPlayer` instance for the computer player. You can specify the AI player's checker, tiebreak preference ('LEFT,' 'RIGHT,' or 'RANDOM'), and lookahead depth. Example:
     ```python
     human_player = Player('X')
     computer_player = AIPlayer('O', 'RANDOM', 3)
     ```

4. Run the game:
   ```python
   connect_four(player1, player2)
   ```

6. Follow the on-screen instructions to choose columns for your moves, and watch the game progress until there's a winner or a tie.

## Game Rules

- Players take turns dropping their checkers into a column of the game board.
- The objective is to be the first to form a horizontal, vertical, or diagonal line of four of their checkers.
- The game ends in a win for the first player to achieve this condition, a tie if the board is full with no winner, or when you decide to interrupt the game.

## Enjoy the Game!

Connect Four is a classic game of skill and strategy. Enjoy playing against human or computer opponents, and challenge your strategic thinking. Have fun and aim to Connect Four!
