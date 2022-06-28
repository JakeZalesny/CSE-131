"""

"""
def seg_sort(numbers: list):
    i_start = 1
    i_end = len(numbers)
    pivot = (i_end + i_start) // 2

    if i_start == i_end: 
        return numbers
    
    else:
        print("2nd half: ",numbers[pivot:])
        print("1st half: ",numbers[:pivot]) 
        for a,b in enumerate(numbers):
            try: 
                if numbers[a] > numbers[a + 1]:
                    print("1.", numbers[a])
                    print("2.", numbers[a + 1])
                    numbers[a], numbers[a + 1] = numbers[a + 1], numbers[a]
                    print(numbers)
                    return seg_sort(numbers)
            
            except IndexError: 
                pass
        
        return numbers

array = [1,5,2,3,4,8,6,45,3,3,15,33,10,500,300,34,23,12,45,67]


def main():

    global array
    i_start = 0
    i_end = len(array) - 1
    sort_recursive(i_start, i_end)

    print(f"Sorted: {array}")

def sort_recursive(i_start, i_end):

    print("\nCalled ---------------")

    global array

    i_up = i_start
    i_down = i_end
    i_pivot = (i_start + i_end) // 2

    loop_i = 1
    print(f"i_start: {i_start}")
    print(f"i_end: {i_end}")
    print(f"i_pivot: {i_pivot}")
    
    while i_up < i_down:
        print(f"\nIteration: {loop_i}")
        print(f"i_up: {i_up}")
        print(f"i_down: {i_down}")
        print(f"i_pivot: {i_pivot}")
        print(array)

        # If neither are greater/less than pivot.

        if array[i_up] < array[i_pivot] and array[i_down] > array[i_pivot]:
            print("Block 1")
            i_up += 1
            i_down -= 1

        # If i_up is greater than pivot, but i_down is not less than pivot.

        elif array[i_up] >= array[i_pivot] and array[i_down] > array[i_pivot]:
            print("Block 2")
            i_down -= 1

        # If i_down is less than pivot, but i_up is not greater than pivot.

        elif array[i_up] < array[i_pivot] and array[i_down] <= array[i_pivot]:
            print("Block 3")
            i_up += 1

        # If both i_up and i_down are greater than and less than pivot respectively.

        elif array[i_up] >= array[i_pivot] and array[i_down] <= array[i_pivot]:

            print("Block 4")
            array[i_up], array[i_down] = array[i_down], array[i_up]
            print(array)
        
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
            sort_recursive(i_start, i_pivot - 1)
            sort_recursive(i_pivot + 1, i_end)

        else:
            print("Return")
            return

#seg_sort([31, 72, 10, 32, 18, 95, 25, 50])

main()