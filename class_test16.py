"""

"""

import numpy


def find_highest(array, num_elements):
    assert len(array) > 0
    size = len(array)
    print(num_elements)
    index = 1 
    num_elements += 1
    highest = array[0]
    
    if num_elements != size :
        index += 1
        if array[index] > array[0] :
            array[index], array[0] = array[0], array[index]
            print(f"Array[i]: {array[index]} \nArray[0]: {array[0]}")
            highest = array[0]
            print(highest)
        return find_highest(array, num_elements)
    
    if num_elements == size :
        return highest

def sum_powers_two(sum,index, num_powers):
    
    def sum_recursive(number, power):
        if number <= 1:
            return 1 if number == 1 else 0

        else :
            power*= 2 

def main():
    #array = [30, 79, 22, 97, 18, 45, 199]
    #highest = find_highest(array, 0)
    #print(highest)
    sum = sum_powers_two(1, 5)
    print(sum)

main()