def calculator():
    print("WELCOME TO THE CALCULATOR")
    num1 = float(input("ENTER THE FIRST NO: "))
    num2 = float(input("ENTER THE SECOND NO: "))
    print("***CHOOSE AN OPERATION***")
    print("1-ADD")
    print("2-SUB")
    print("3-MULTIPLY")
    print("4-DIVIDE")

    number= input("ENTER THE NUMBER FOR PERFORMING OPERATION(1/2/3/4): ")
    if number == '1':
        result = num1 + num2
        print(f"RESULT= {num1} + {num2} is: {result}")
    elif number == '2':
        result = num1 - num2
        print(f"RESULT= {num1} - {num2} is: {result}")
    elif number == '3':
        result = num1 * num2
        print(f"RESULT= {num1} * {num2} is: {result}")
    elif number == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"RESULT= {num1} / {num2} is: {result}")
        else:
            print("ERROR! DIVISION BY ZERO IS NOT ALLOWED.")
    else:
        print("INVALID OPERATION! PLEASE ENTER A VALID OPERATION")
calculator()
