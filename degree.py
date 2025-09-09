def main():
    print("Hello welcome to the degree converter.")
    while True:
        try:
            current_mesurement, current_mesurement2 = conversion_picker()
        except:
            print("Error running or using conversion picker please read code")
            return
        """try:
            degree, mesurement = conversion_degree()
            print(degree, mesurement)
        except:
            print("Error running degree and mesurement picker")"""

        try:
            current_degree = degree_picker(current_mesurement)
        except:
            print("Error running or using degree picker please read code")
            return

        try:
            converted_degree = degree_converter(current_mesurement, current_mesurement2, current_degree)
        except:
            print("Error running degree converter please check code")
            return
        print(converted_degree)
        user_input = input("Do you want to convert another number? (y or n)").lower()
        if user_input == "n":
            return
        elif user_input == "y":
            print("running program again")
            pass
            
    return
"""
def conversion_degree():
    print("please enter your current degree with the degree mesurement after seperated by a space (example: 32 f, -10 cel, 400 kelvin)")
    while True:
        userinput = input("options include (C, F, and K)").lower()
        seperator = " "
        degree, mesurement = userinput.split(seperator, 1)
        degree = int(degree)
        for x in mesurement:
            if x == "c":
                mesurement = "c"
                if degree >= -273:
                    print(f"degree and mesurement is valid {degree}, {mesurement}")
                    break
                else:
                    print("degree entered is blow absolute zero please try again")
                    pass
                    
            elif x == "f":
                mesurement = "f"
                if degree >= -459:
                    print(f"degree and mesurement is valid {degree}, {mesurement}")
                    break
                else:
                    print("degree entered is blow absolute zero please try again")
                    pass

            elif x == "k":
                mesurement = "k"
                if degree >= 0:
                    print(f"degree and mesurement is valid {degree}, {mesurement}")
                    break
                else:
                    print("degree entered is blow absolute zero please try again")
                    pass

            else:
                pass
        if mesurement != "c" or "f" or "k":
            print("sorry the mesurement you have entered is not valid try again")
            pass
    print(f"current degree is {degree} and mesurement is {mesurement}")
"""
    

def conversion_picker():
    print("what is your inital degree (type the letter of the measurment you currently have (C, F, or K))")
    while True:
        current_mesurement = input("C or F or K: ").lower()
            
        if current_mesurement == "c":
            print("Conversion factor set to c.")
            break
        elif current_mesurement == "f":
            print("Conversion factor set to f.")
            break
        elif current_mesurement == "k":
            print("Conversion factor set to k.")
            break
        else:
            print("The input you have entered is not equal to C, F, or K please try again.")
            pass
    while True:
        print(f"pick your desired convertion from {current_mesurement} ")
        current_mesurement2 = input("C or F or K: ").lower()
        
        if current_mesurement == current_mesurement2:
            print("cannot convert the same degree")
            pass
        elif current_mesurement2 == "c":
            print("Conversion factor set to c.")
            break
        elif current_mesurement2 == "f":
            print("Conversion factor set to f.")
            break
        elif current_mesurement2 == "k":
            print("Conversion factor set to k.")
            break
        elif current_mesurement == current_mesurement2:
            print("cannot convert the same degree")
            pass
        else:
            print("The input you have entered is not equal to C, F, or K please try again.")
            pass
    return current_mesurement, current_mesurement2

def degree_picker(current_mesurement):
    print(f"Please enter valid degree amount for your chosen degree measurement. current measurment: {current_mesurement}")
    while True:
        current_degree = float(input("Current degree (has to be a valid degree): "))
        if current_mesurement == "c":
            if current_degree >= -273:
                print(f"current degree is valid: {current_degree}")
                break
            else:
                print("degree inputed is blow zero please pick a valid degree.")
                pass
            """if current_degree in range(-273, 999999999999999999999999999999999999999999999):
                print(f"current degree is valid: {current_degree}")
                break
            else:
                print("degree amount entered is not a valid degree for the current mesurement")
                pass"""
        elif current_mesurement == "f":
            if current_degree >= -459:
                print(f"current degree is valid: {current_degree}")
                break
            else:
                print("degree inputed is blow zero please pick a valid degree.")
                pass
            """if current_degree in range(-459, 999999999999999999999999999999999999999999999):
                print(f"current degree is valid: {current_degree}")
                break
            else:
                print("degree amount entered is not a valid degree for the current mesurement")
                pass"""
        else:
            print("Error with current_mesurement check code")
            return
    return current_degree

def degree_converter(current_mesurement, current_mesurement2, current_degree):
    if current_mesurement == "c" and current_mesurement2 == "f":
        converted_degree = ((current_degree * 1.8) + 32)
        converted_degree_message = (f"Your converted degree is {converted_degree} F")

    elif current_mesurement == "f" and current_mesurement2 == "c":
        converted_degree = ((current_degree - 32) * 0.5555)
        converted_degree_message = (f"Your converted degree is {converted_degree} C")

    elif current_mesurement == "f" and current_mesurement2 == "k":
        converted_degree = ((current_degree - 32) * 0.5555 + 273.15)
        converted_degree_message = (f"Your converted degree is {converted_degree} K")

    elif current_mesurement == "c" and current_mesurement2 == "k":
        converted_degree = (current_degree + 273.15)
        converted_degree_message = (f"Your converted degree is {converted_degree} K")

    elif current_mesurement == "k" and current_mesurement2 == "f":
        converted_degree = (((current_degree - 273.15) * 1.8) + 32)
        converted_degree_message = (f"Your converted degree is {converted_degree} F")

    elif current_mesurement == "k" and current_mesurement2 == "c":
        converted_degree = (current_degree - 273.15) 
        converted_degree_message = (f"Your converted degree is {converted_degree} C")    

    else:
        print("Error with current mesurement look at code")
    return converted_degree_message

        
        

    
if __name__ == "__main__":
    result = main()