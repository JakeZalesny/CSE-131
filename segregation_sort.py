"""
# 1. Name:
#      Jake Zalesny
# 2. Assignment Name:
#      Lab 13 : Segregation Sort Program
# 3. Assignment Description:
#      This program is meant to sort an unsorted array of numbers using a recursion
#       algorithm by splitting the list in two several times over and picking up the
#       pieces.
# 4. What was the hardest part? Be as specific as possible.
#      It took me a second o n how to figure out how to implement calling the array variable 
#       as a parameter rather than a globally scoped variable, but I realized that it wouldn't 
#       affect the variable as long as it remained the same variable. 
# 5. How long did it take for you to complete the assignment?
#      2.5 hrs. 
"""
import json



def get_filename() -> str:
    filename = str(input("What is the filename? "))
    return filename

def readfile(filename: str):
    with open(filename) as f: 
        file_data = f.read()
        unformated_array = json.loads(file_data)
        array = unformated_array["array"]
    return array

def sort_recursive(i_start, i_end, array):

    # print("\nCalled ---------------")

    i_up = i_start
    i_down = i_end
    i_pivot = (i_start + i_end) // 2

    loop_i = 1
    # print(f"i_start: {i_start}")
    # print(f"i_end: {i_end}")
    # print(f"i_pivot: {i_pivot}")
    
    while i_up < i_down:
        # print(f"\nIteration: {loop_i}")
        # print(f"i_up: {i_up}")
        # print(f"i_down: {i_down}")
        # print(f"i_pivot: {i_pivot}")
        # print(array)

        # If neither are greater/less than pivot.

        if array[i_up] < array[i_pivot] and array[i_down] > array[i_pivot]:
            # print("Block 1")
            i_up += 1
            i_down -= 1

        # If i_up is greater than pivot, but i_down is not less than pivot.

        elif array[i_up] >= array[i_pivot] and array[i_down] > array[i_pivot]:
            # print("Block 2")
            i_down -= 1

        # If i_down is less than pivot, but i_up is not greater than pivot.

        elif array[i_up] < array[i_pivot] and array[i_down] <= array[i_pivot]:
            # print("Block 3")
            i_up += 1

        # If both i_up and i_down are greater than and less than pivot respectively.

        elif array[i_up] >= array[i_pivot] and array[i_down] <= array[i_pivot]:

            # print("Block 4")
            array[i_up], array[i_down] = array[i_down], array[i_up]
            # print(array)
        
            if i_up == i_pivot:
                i_pivot = i_down
                i_up += 1

            elif i_down == i_pivot:
                i_pivot = i_up
                i_down -= 1

            else:
                i_up += 1
                i_down -= 1
        loop_i += 1
        
        if i_start < i_end:
            sort_recursive(i_start, i_pivot - 1, array)
            sort_recursive(i_pivot + 1, i_end, array)

        else:
            # print("Return")
            return

def main():

    filename = get_filename()
    array = readfile(filename)

    i_start = 0
    i_end = len(array) - 1
    sort_recursive(i_start, i_end, array)

    print(f"Sorted: {array}")


main()