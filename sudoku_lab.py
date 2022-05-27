"""
# 1. Name:
#      Jake Zalesny
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      So far, its just meant to put a value in a square in a sudoku game
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part for me was configuring the display and saving the board. 
#       I kept running into configuration errors with the display and I kept only saving
#       zeros every time I saved the board which was problematic. I finally solved it with 
#       only a couple of minor adjustments. 
# 5. How long did it take for you to complete the assignment?
#      2.5 hours.
"""

import json
from lib2to3.pytree import convert
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

def convert_column_to_value(user_square: str) -> str:
    column = user_square[0].upper()
    return column

def convert_row_to_int(user_square: str) -> int:
    row = int(user_square[1]) - 1
    return row

def convert_column_to_int(column: str, coordinate_dictionary: dict) -> int: 
    column_number = coordinate_dictionary[column]
    return column_number

def insert_value(coordinate_dictionary: dict, column: str, row: int, column_number: int, user_value: int, board: list):
    is_valid = True
    while is_valid: 
        is_valid = check_column(column, coordinate_dictionary)
        is_valid = check_row(row)
        board[row][column_number] = user_value

def possible_values(occupied_column_list: list, occupied_row_list: list):
    occupied_list = []
    possible_values = []

    for i in occupied_row_list :
        occupied_list.append(i)
    
    for i in occupied_column_list :
        occupied_list.append(i)
    
    for value in range(10) :
        if value not in occupied_list :
            possible_values.append(value)
    
    return possible_values


# Checks the column to see if the value is valid
def check_column(column: str, coordinate_dictionary: dict) -> bool:
    if column in coordinate_dictionary.keys():
        return True
    
    else :
        print("ERROR: Invalid Column! Please try again.")
        return False

# Checks the row to see if the inserted row is valid 
def check_row(row: int) -> bool:
    if row > 9 :
        return False
    
    else :
        print("ERROR: Invalid Row! Please try again.")
        return True

# Checks to see if the square is empty or not
def check_square_for_value(row: int, column_number: int, board: list) -> bool:
    if board[row][column_number] != " ":
        print("ERROR: Square already has a value! please try again.")
        return False
    
    else :
        return True

# Returns all the numbers that are in the row
def check_unique_row(row: int, column_number: int, board: list, user_value: int) :
    occupied_number_list_column = []
    for i in board[row] :
        if i != " ":
            occupied_number_list_column.append(i)
    
    return occupied_number_list_column

# Compares all numbers in the row to user's input
def is_occupied_row(occupied_number_list_row: list, user_value: int) -> bool:
    for i in occupied_number_list_row :
        if user_value == i :
            return False
        
        else :
            return True

# Returns a list of numbers in the column 
def check_unique_column(column_number: int, board: list, user_value: int) :
    occupied_number_list_column = []
    for i in range(8):
        if board[i][column_number] != " ":
            occupied_number_list_column.append(board[i][column_number])
        
        return occupied_number_list_column

# Compares to list of numbers in the column 
def is_occupied_column(occupied_number_list_column: list, user_value: int) -> bool:
    for i in occupied_number_list_column :
        if user_value == i :
            return False

        else :
            return True


def get_user_square(board, filename):
    user_square = input("Specify a coordinate to edit or \'Q\' to save and quit\n> ")
    if user_square.upper() == "Q":
        save_board(board, filename)
    
    else :
        return user_square

def get_value(user_square: str) -> int: 
    user_value = 0
    
    while user_value <= 0 or user_value >= 10 :
        user_value = int(input(f"What number goes in {user_square}? "))
        
        if user_value <= 0 or user_value >= 10 :
            print("ERROR: Invalid Value, please enter a number from 1 to 9.")
    
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
    value_is_valid = True
    while user_square != "Q" and value_is_valid == True:
        display_board(board)
        _coordinate_dictionary = coordinate_dictionary()
        user_square = get_user_square(board, filename)
        user_value = get_value(user_square)
        value_is_valid = True
        column = convert_column_to_value(user_square)
        row = convert_row_to_int(user_square)
        column_number = convert_column_to_int(column, _coordinate_dictionary)
        occupied_number_list_column = check_unique_column(column_number, board, user_value)
        occupied_number_list_row = check_unique_row(row, column_number, board, user_value)
        value_is_valid = is_occupied_column(occupied_number_list_column, user_value)
        value_is_valid = is_occupied_row(occupied_number_list_row, user_value)
        value_is_valid = check_square_for_value(row, column_number, board)
        insert_value(_coordinate_dictionary, column, row, column_number, user_value, board)
    save_board(board, filename)

main()
