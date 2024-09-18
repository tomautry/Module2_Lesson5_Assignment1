# Task 1 Calculator App

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("You can't divide by zero.")
        return None
    return num1 / num2

# Task 2 User Input

def main():
    print("Hello, this is a calc (short for calculator).")
    print("Please select an operation from the list below using 1-4.")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Select the desired operation (1-4): ")
    if operation not in {"1", "2", "3", "4"}:
        print("Invalid selection.")
        return
    
# I'm not sure how to check if the input is a valid number

    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    if operation == "1":
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == "2":
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == "3":
        result = multiply(num1, num2)
        print(f"{num1} * {num2} + {result}")
    elif operation == "4":
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")



main()