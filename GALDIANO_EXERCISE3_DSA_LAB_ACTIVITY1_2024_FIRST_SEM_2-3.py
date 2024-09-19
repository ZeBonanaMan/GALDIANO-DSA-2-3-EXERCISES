# Name: Marco Gabriel P. Galdiano                                                         
# Subject: Data Structure and Algorithm                                                      
# Lab Activity: Python Review                                                       
# Date Passed: 19-09-2024                                                      

# Exercise 3:  Diamond Shape (advance topic):
def diamond_time():
    try:
        given = int(input("Enter an odd number: "))
        if given % 2 == 0:
            print(f"\033[91m!! Please enter an odd number !!\033[0m\n")
            diamond_time()
        else:
            mid = given // 2
            for i in range(given):
                spaces = abs(mid - i)
                stars = given - 2 * spaces
                print(" " * spaces + "*" * stars)

    except ValueError:
        print(f"\033[91m!! Please enter a valid odd number !!\033[0m\n")
        diamond_time()

diamond_time()