# Name: Marco Gabriel P. Galdiano                                                         
# Subject: Data Structure and Algorithm                                                      
# Lab Activity: Python Review                                                       
# Date Passed: 19-09-2024                                                      

# Exercise 1: Temperature Converter
def perform_input():
        global given_temperature
        given_temperature = input("\n\nPlease input a temperature:\n")
        if given_temperature.isnumeric() == False:
            print(f"\n\n\033[91m!! Please enter numbers only\033[0m")
            perform_input()
        else:
            input_type()

def input_type():
    given_type = (input("\n\nWhat type of conversion will it be?\n"
                            "(1) For Celsius to Fahrenheit\n"
                            "(2) For Fahrenheit to Celsius\n"
                            "(0) Exit\n\n"
                            "Response: "))
    
    if given_type == "1":
        answer = (float(given_temperature) * 1.8) + 32
        print(answer.__round__(4),"°C",)

    elif given_type == "2":
        answer = (float(given_temperature) - 32) * (5/9)
        print(answer.__round__(4),"°F")
    
    elif given_type == "0":
        exit()

    else:
        print(f"\n\n\033[91m!! Choose only between 1 or 2 !!\033[0m")
        input_type()

perform_input()