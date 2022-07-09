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