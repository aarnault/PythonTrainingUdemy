
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[1]+"|" + board[2] + "|" + board [3])
    print(board[4] + "|" + board[5] + "|" + board[6])
    print(board[7] + "|" + board[8] + "|" + board[9])

def player_input():
    player_marker = " "
    while player_marker != "X" or player_marker !="O":
        player_marker = input("Please choose if you want to be X or O?")
        if player_marker== "X":
            return ("X", "O")
        elif player_marker== "O":
            return ("O", "X")

def place_marker (board, marker, position):
    board[position] = marker

def win_check(board, mark):
    for i in range (1,10):
        return(board[i] == board[i+1] ==board[i+2] == mark or board[i] == board[i+3] ==board[i+6] == mark or
            board[1] == board[5] == board[9] == mark or board[3] == board[5] ==board[7] == mark)

import random

def choose_first():
    player=random.randint(1,2)
    if player = 1:
        return "Player 1"
    else:
        return "Player 2"


def space_check(board, position):
    return(board[position] == " ")

def full_board_check(board):
    for i in range (1, 10):
        if space_check(board, i):
            return False

def player_choice(board):
    next_position = 0
    while next_position != range(1.10) or not space_check(board, next_position):
        next_position= int(input("Please choose the position of your next move (1-9)?"))
    return next_position

def replay():
    play_again = input("Would you like to replay (Y or N)?")
    return (play_again = "Y")

print("Welcome to Tic Tac Toe!")

#Set the game
    the_board = [" "] *10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn+"will go first")

    play_game= input("Ready to play (Y or N)")
    if play_game = "Y":
        game_on = True,
    else:
        game_on = False

    while game-on:

# Player 1
    if turn=="Player 1":
        display_board(the_board)
        position = player_choice(the_board)
        place_marker(the_board, player1_marker, position)

        if win_check(the_board, player1_marker):
            display_board(the_board)
            print("Player 1 won!")
        else:
            if full_board_check(the_board):
                display_board(the_board)
                print("It is a Tie!")
                game_on = False
            else:
                turn == "Player 2"

    else:
        display_board(the_board)
        position = player_choice(the_board)
        place_marker(the_board, player2_marker, position)

        if win_check(the_board, player2_marker):
        display_board(the_board)
        print("Player 2 won!")
        else:
            if full_board_check(the_board):
                display_board(the_board)
                print("It is a Tie!")
                game_on = False
            else:
                turn == "Player 1"

#Replay?
if not replay()
    break
