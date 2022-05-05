"""
Calendar Program

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

def month_to_day():
    month_to_day = {
        "January":31, 
        "February":(28,29),
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

def get_month_number() -> int:
    month_number = int(input("Enter a month number: "))
    return month_number

def get_year() -> int:
    year = int(input("Enter a year number: "))
    return year

def is_leap_year(year, month_to_day):
    pass

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
            month_total += month_to_day[month][2]
        
        else : 
            month_total += month_to_day[month]
    
    total = month_total + day_total

    offset = total % 7

    print(offset)

    return offset

def month_number_to_name(month_number):
    if month_number == 1: 
        month_name = "January"
    
    elif month_number == 2:
        month_name = "February"
    
    elif month_number == 3:
        month_name = "March"
    
    elif month_number == 4:
        month_name = "April"
    
    elif month_number == 5:
        month_name == "May"
    
    elif month_number == 6:
        month_name = "June"
    
    elif month_number == 7:
        month_name = "July"
    
    elif month_number == 8: 
        month_name = "August"
    
    elif month_number == 9:
        month_name = "September"
    
    elif month_number == 10: 
        month_name = "October"
    
    elif month_number == 11:
        month_name = "November"
    
    elif month_name == 12:
        month_name = "December"
    
    else: 
        month_name = "ERROR invalid month entry"
    
    return month_name

def display_calendar(year, month_to_days, offset):
    pass

def main():
    month_to_days = month_to_day()
    month_number = get_month_number()
    year = get_year()
    offset = compute_offset(year, month_to_days, month_number)
    display_calendar(year, month_to_days, offset)

main()

