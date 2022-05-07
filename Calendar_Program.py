"""
Calendar Program
1. Name
    Jake Zalesny

2. Assignment Name: 
    Lab 03: Calendar

3. Assignment Description: 
    A monthly calendar based on the users input

4. What was the hardest part? Be as specific as possible. 
    It was difficult for me to figure out how to exactly 
    configure the display so that all the numbers would 
    pop up correctly

5. How long did it take for you to complete the assignment? 
    It took me about 2-2:30 hours in total to complete

"""


BEGINNING_SPACING = "   "

"""
MONTH LIST

Args: None
Rtrn: Returns a list of each month of the year
"""
def month_list():
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return month_list

"""
MONTH TO DAY

Args: None
Rtrns: Returns a dictionary of each month of the year and an associated number value for the days
"""
def month_to_day():
    month_to_day = {
        "January":31, 
        "February":28,
        "March":31, 
        "April":30, 
        "May":31, 
        "June":30, 
        "July":31, 
        "August":31, 
        "September":30, 
        "October":31, 
        "November":30, 
        "December":31
    }

    return month_to_day

"""
GET MONTH NUMBER

Args: None
Rtrns: Returns User input for the desired month number
"""
def get_month_number() -> int:
    month_number = int(input("Enter a month number: "))
    return int(month_number)

"""
GET YEAR

Args: None
Rtrns: Returns User input for the desired year
"""
def get_year() -> int:
    year = int(input("Enter a year number: "))
    return int(year)

"""
IS LEAP YEAR

Args: Year: User inputed year. 
Rtrns: Returns True or False based on the calculation of the leap year
"""
def is_leap_year(year: int, month_to_day: dict):
    if year % 4 == 0: 
        return True
    
    elif year % 4 == 0 and year % 100 == 0 :
        return True
    
    elif year % 400 == 0 :
        return True
    
    else :
        return False


"""
COMPUTE OFFSET

Args: year: User inputed year, month_to_day: dictionary containing months and associated
day values, month_number: User inputed month, month_list: List of months in the year 

Rtrns: Offset (The day the month starts on)
"""
def compute_offset(year: int, month_to_day: dict, month_number: int, month_list: list):
    offset = 0
    day_total = 0
    month_total = 0
    for year in range(1753, year - 1):
        if is_leap_year(year, month_to_day) :
            day_total += 366
        
        else :
            day_total += 365
    
    for month in month_to_day :
        if month == month_list[month_number - 1]:
            break
        
        elif is_leap_year(year, month_to_day) and month == "February" :
            month_total += month_to_day[month] + 1
        
        else : 
            month_total += int(month_to_day[month])
    
    total = month_total + day_total

    offset = total % 7

    return offset - 1

"""
DISPLAY CALENDAR

Args: year: User inputed year, month_to_day: dictionary containing months and associated
day values, month_number: User inputed month, month_list: List of months in the year 

Rtrns: None, only displays
"""
def display_calendar(year: int, month_to_days: dict, offset: int, month_number: int, month_list: list):
    counter = 0
    print(f"{BEGINNING_SPACING}Su  Mo  Tu  We  Th  Fr  Sa")
    print(f"{BEGINNING_SPACING}", end="")
    new_line_counter = 0
    
    match offset: 
        case 0 :
            print(" ", end="")
        
        case 1 :
            print("     ", end="")
            new_line_counter = 1
        
        case 2: 
            print("         ", end="")
            new_line_counter = 2
        
        case 3:
            print("             ", end="")
            new_line_counter = 3
        
        case 4: 
            print("                 ", end="")
            new_line_counter = 4
        
        case 5:
            print("                     ", end="")
            new_line_counter = 5
        
        case 6:
            print("                         ", end="")
            new_line_counter = 6
        
        case 7:
            print("                             ", end="")
            new_line_counter = 7
    
    month = month_list[month_number - 1]
    day_count = month_to_days[month]
    
    if is_leap_year(year, month_to_days) and month == "February":
        day_count = month_to_days[month] + 1
    
    for i in range(1, day_count + 1) :
        if i <= 8 :
            print(f"{i}   ", end="")
        
        if i >= 9 :
            print(f"{i}  ", end="")
        
        new_line_counter += 1
        #1
        # print(new_line_counter, end=" ")
        if new_line_counter == 7 and i >= 10 :
            print()
            print("   ", end="")
            new_line_counter = 0
        
        elif new_line_counter == 7 :
            print()
            print("    ", end="")
            new_line_counter = 0
        
    return       

"""
MAIN

Args: None
Rtrns None
Calls each function and runs the program
"""
def main():
    month_to_days = month_to_day()
    month = month_list()
    
    month_number = get_month_number()
    while month_number > 12 or month_number < 1:
        print("ERROR: Invalid month number")
        month_number = get_month_number()
    
    year = get_year()
    while year < 1753:
        print("ERROR: Please enter a year after 1752")
        year = get_year()
    
    offset = compute_offset(year, month_to_days, month_number, month)
    display_calendar(year, month_to_days, offset, month_number, month)

main()

