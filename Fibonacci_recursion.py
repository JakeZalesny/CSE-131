def recursion_fibonacci(n: int):
    if n <= 1: 
        return n 
    else: 
        return recursion_fibonacci(n - 1) + recursion_fibonacci(n - 2)


def main(): 
    n_terms = 10
    if n_terms <= 0 :
        print("Enter a positive integer: ")
    else: 
        for i in range(n_terms):
            print(recursion_fibonacci(i))

main()