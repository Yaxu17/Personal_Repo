import math
while True:
    Operator = input("Enter the operator (+, -, *, /) or type 'exit' to quit: ")

    if Operator.lower() == "exit":
        print("Calculator closed.")
        break

    try:
        num1 = float(input("Enter the 1st Number: "))
        num2 = float(input("Enter the 2nd Number: "))

        if Operator == "+":
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is {result}")
        elif Operator == "-":
            result = num1 - num2
            print(f"The subtraction of {num1} and {num2} is {result}")
        elif Operator == "*":
            result = num1 * num2
            print(f"The multiplication of {num1} and {num2} is {round(result, 2)}")
        elif Operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The division of {num1} and {num2} is {round(result, 2)}")
        else:
            print(f"'{Operator}' is not a valid operator.")
    except ValueError:
        print("Error: Please enter valid numbers.")