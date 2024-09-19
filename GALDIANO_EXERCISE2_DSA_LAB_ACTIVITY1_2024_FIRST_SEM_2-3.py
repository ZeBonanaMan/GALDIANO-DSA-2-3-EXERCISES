# Name: Marco Gabriel P. Galdiano                                                         
# Subject: Data Structure and Algorithm                                                      
# Lab Activity: Python Review                                                       
# Date Passed: 19-09-2024                                                      

# Exercise 2: Ohm’s Law Calculator
def input_type():
    given_type = (input("\n\nWhat type of conversion will it be?\n"
                            "(1) Voltage\n"
                            "(2) Current\n"
                            "(3) Resistance\n"
                            "(0) Exit\n\n"
                            "Response: "))
    try:
        if given_type == "1":
            curr = int(input("\nCurrent: "))
            resistance = int(input("Resistance: "))
            answer = float(curr*resistance)
            print(answer.__round__(4))

        elif given_type == "2":
            voltage = int(input("\nVoltage: "))
            resistance = int(input("Resistance: "))
            answer = float(voltage/resistance)
            print(answer.__round__(4))

        elif given_type == "3":
            voltage = int(input("\nVoltage: "))
            current = int(input("Current: "))
            answer = float(voltage/current)
            print(answer.__round__(4))

        elif given_type == "0":
            exit()

        else:
            print(f"\n\n\033[91m!! Choose only between 1, 2, or 3 !!\033[0m")
            input_type()

    except ZeroDivisionError:
        print(f"\n\n\033[91m!! You cannot divide by 0 !!\033[0m\n")
        input_type()

    except ValueError:
        print("\n\n\033[91m!! Please enter numbers only\033[0m\n")
        input_type()

input_type()