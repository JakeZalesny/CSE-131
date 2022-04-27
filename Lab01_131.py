# 1. Name:
#      Jake Zalesny
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      Having to resubmit due to a freak github accident
# 5. How long did it take for you to complete the assignment?
#      1.5 hrs

from ast import While
import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '
TURN_COUNTER = 0
FILENAME = "tictactoe.json"

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    with open(filename) as f: 
        data = f.read()
        board = json.loads(data)
    return board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    transcription_board = {
        "board": [
            " ", " ", " ",
            " ", " ", " ",
            " ", " ", " "
        ]
    }
    transcription_board["board"] = board
    with open(filename, "w") as w :
        json.dump(transcription_board, w)
    
    quit()

def clear_board(filename, board) :
    with open(filename, "w") as w :
        json.dump(blank_board, w)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    for i in range(0, 9):
        if i == 2 or i == 5 :
            print(f" {board[i]} ")
            print("---+---+---")
        
        elif i == 8 :
            print(f" {board[i]} \n")
        
        else :
            print(f" {board[i]} |", end="")
        

def is_x_turn(board, turn_counter):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    if turn_counter % 2 == 0 :
        turn_counter += 1
        return True
    
    else:
        turn_counter += 1 
        return False

def get_x_input(board):
    x = input("X> ")
    if x == "q" :
        save_board(FILENAME,board)
    
    else:
        return x

def get_o_input(board):
    o = input("O> ")
    if o == "q" :
        save_board(FILENAME, board)
    
    else :
        return o

def play_game(board, turn):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    display_board(board)
    if turn :
        x = int(get_x_input(board))
        board[x - 1] = X
        display_board(board)
    
    else :
        o = int(get_o_input(board))
        board[o - 1] = O
        display_board(board)
    
    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
def main():
    # This is used to determine who's turn it is
    # Everytime it strikes an odd number it switches turns
    turn_counter = 0
    board = read_board(FILENAME)
    
    # This is what plays the game and determines when
    # it's over
    while game_done(board, message= False) == False :
        turn = is_x_turn(board, turn_counter)
        play_game(board, turn)
        turn_counter += 1
    
    # This clears the board on the file
    clear_board(FILENAME, board)
    game_done(board, message= True)

main()