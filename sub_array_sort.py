"""
SUB LIST LAB


"""



from numpy import number


def get_list() -> list :
    number_list = [31, 72, 32, 10, 95, 50, 25, 18]
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
            print(f"Counter: {counter}")
            source1 = number_list[:counter]
            print(f"Source 1: {source1}")
            
            source2 = number_list[counter]
            print(f"Source 2: {source2}")
            
            if source1[0] < source2 and source1 not in destination :
                destination.append(source1[0])
                destination.append(source2)
            
            elif source2 < source1[1] and source1[1] not in destination :
                destination.append(source2)
                destination.append(source1[1])
            
            elif source1[1] < source2 and source1[1] not in destination :
                destination.append(source1[1])
                destination.append(source2)
            
            else:
                destination.append(source2)

            print(f"Destination: {destination}")


def main():
    number_list = get_list()
    sort_list(number_list)

main()