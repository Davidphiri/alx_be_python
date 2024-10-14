#prompt for user input 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

#Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

#Evaluates match case operation
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2 
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
           result = num1 / num2
           print(f"The result is {result}")
        else:
            print("Error, division by zero is not allowed.")
    case _:
        print("Error: Invalid operation. Please choose one of (+, -, *, /).")
    