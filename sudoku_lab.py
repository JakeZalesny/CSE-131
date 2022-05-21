"""

"""
from fileinput import filename
import json
HARD_FILE = "131.05.Hard.json"
MEDIUM_FILE = "131.05.Medium.json"
EASY_FILE = "131.05.Easy.json"

def read_file():
    which_board = int(input("""Which board would you like?\n 
    1. Hard\n
    2. Medium\n
    3. Easy \n> """))

    if which_board == 1 :
        with open(HARD_FILE) as h :
            hard_data = h.read()
            board = json.loads(hard_data)
            return board["board"], HARD_FILE
    
    elif which_board == 2 :
        with open(MEDIUM_FILE) as m :
            medium_data = m.read()
            board = json.loads(medium_data)
            return board["board"], MEDIUM_FILE
    
    elif which_board == 3 :
        with open(EASY_FILE) as e :
            easy_data = e.read()
            board = json.loads(easy_data)
            return board["board"], EASY_FILE


def coordinate_dictionary():
    coordinate_dictionary = {
        "A":0,
        "B":1,
        "C":2,
        "D":3,
        "E":4,
        "F":5,
        "G":6,
        "H":7,
        "I":8

    }
    return coordinate_dictionary

def insert_value(coordinate_dictionary: dict, user_square: str, user_value: int, board: list):
    column = user_square[0].upper()
    column_number = coordinate_dictionary[column]
    row = int(user_square[1]) - 1
    board[row][column_number] = user_value




def get_user_square(board, filename):
    user_square = input("Specify a coordinate to edit or \'Q\' to save and quit\n> ")
    if user_square.upper() == "Q":
        save_board(board, filename)
    
    else :
        return user_square

def get_value(user_square: str) -> int: 
    user_value = int(input(f"What number goes in {user_square}? "))
    return user_value

def display_board(board: list):
    print("   A B C D E F G H I ")    
    counter = 0
    row_counter = 1
    for square in board:
        counter += 1
        
        if counter == 4 or counter == 7 :
            print("  -----+-----+-----")
            print(f"{row_counter}  ", end="")
            row_counter += 1

        else :
            print(f"{row_counter}  ", end="")
            row_counter += 1 
        for i in range(3):
            if square[i] == 0:
                square[i] = " "
            
            if i == 2:
                print(f"{square[i]}|", end="")
            
            else :
                print(square[i], end=" ")
        
        for j in range(3, 6):
            if square[j] == 0:
                square[j] = " "

            if j == 5:
                print(f"{square[j]}|", end="")
            else:
                print(square[j], end=" ")
        
        for k in range(6, 9):
            if square[k] == 0:
                square[k] = " "

            if k == 8: 
                print(f"{square[k]}")
            
            else :            
                print(square[k], end=" ") 

def save_board(board: list, filename: str):
    
    for row in range(9) :
        for square in range(9) :
            if board[row][square] == " ":
                board[row][square] = 0
            
            else :
                pass
    
    transcription_board = {
        "board": [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
  ] 
    }
    transcription_board["board"] = board
    
    
    
    with open(filename, "w") as w :
        json.dump(transcription_board, w)
    
    quit()

def main():
    board, filename = read_file()
    user_square = None
    while user_square != "Q":
        display_board(board)
        _coordinate_dictionary = coordinate_dictionary()
        user_square = get_user_square(board, filename)
        user_value = get_value(user_square)
        insert_value(_coordinate_dictionary, user_square, user_value, board)
    save_board(board, filename)

main()
