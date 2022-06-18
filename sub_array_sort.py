"""
SUB LIST LAB
# 1. Name:
#      Jake Zalesny
# 2. Assignment Name:
#      Lab 09 : Sub-List Sort Program
# 3. Assignment Description:
#      This is meant to sort a list by dividing it up several times
# 4. What was the hardest part? Be as specific as possible.
#      I could not figure out how to implement the algorithm into this for my life.
# 5. How long did it take for you to complete the assignment?
#      4 hours

"""









def get_list(number_list) -> list :
    return number_list


def sort_list(number_list):
    bigger_number = 0
    source1 = [0]
    source2 = []
    destination = []
    counter = 0
     
    
    for i in range(len(number_list)):
        if number_list[i] < number_list[i - 1]:
            counter = i 
            #print(f"Counter: {counter}")
            source1 = number_list[:counter]
            #print(f"Source 1: {source1}")
            source2 = number_list[counter:]
            #print(f"Source 2: {source2}")
            
            if source1[0] < source2[0] and source1[0] not in destination :
                destination.append(source1[0])
                #source1 = source1.pop(0)
                #destination.append(source2[0])
            
            elif source2[0] < source1[1] and source1[1] not in destination :
                #source2 = source2.pop(0)
                destination.append(source2[0])
                #destination.append(source1[1])
            
            elif source1[1] < source2[0] and source1[1] not in destination :
                #source1 = source1.pop(1)
                destination.append(source1[1])
                #destination.append(source2[0])
            
            elif source1[0] < source2[0] and source1[0] < destination[0]:
                placeholder = destination[0]
                destination[0] = source1[0]
                source1[0] = placeholder

            elif source2[0] < source1[0] and source2[0] < destination[0]:
                placeholder = destination[0]
                destination[0] = source2[0]
                source2[0] = placeholder

            else:
                #source2 = source2.pop(0)
                destination.append(source2[0])

    print(f"Destination: {destination}")


def main():
    list_1 = [31, 72, 32, 10, 95, 50, 25, 18] 
    number_list = get_list(list_1)
    sort_list(number_list)

main()