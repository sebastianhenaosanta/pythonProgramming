"""
Welcome to Battleship!

In this project you will build a simplified, one-player version of the classic board game Battleship! In this version of the game, there will be a single ship hidden in a random location on a 5x5 grid. The player will have 10 guesses to try to sink the ship.

To build this game we will use our knowledge of lists, conditionals and functions in Python. 


"""
from random import randint


#########################################################
def print_board(board_in):
    for i in board_in:
        print(" ".join(i))


#########################################################
board = []


for i in range(0, 5):
    board.append(["0"]*5)


def random_row(board_in):
    return randint(0, len(board_in)-1)


def random_col(board_in):
    return randint(0, len(board_in)-1)


##########################################################
for turn in range(4):
    print("Turn", turn + 1)
    ship_row = random_row(board)
    ship_col = random_col(board)
    print(ship_row)
    print(ship_col)
    # Add your code below!
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sank my battleship!")
        break
    else:
        if guess_row not in range(4) and guess_col not in range(4):
            print("Oops, that's not even in the ocean.")
            print("You missed my battleship!")
        elif board[guess_row][guess_col] == 'X':
            print("You guessed that one already.")
        else:
            board[guess_row][guess_col] = "X"
            print_board(board)
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
            print_board(board)
        if turn == 3:
            print("Game Over")

##########################################
################
