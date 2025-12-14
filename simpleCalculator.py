Num1 = float(input("Enter first number: "))
Num2 = float(input("Enter second number: "))
operation = input("Enter operator (+,-,*,/): ")

try:
    if operation == '+':
        print("Result is:", Num1 + Num2)

    elif operation == '-':
        print("Result is:", Num1 - Num2)

    elif operation == '*':
        print("Result is:", Num1 * Num2)

    elif operation == '/':
        print("Result is:", Num1 / Num2)

    else:
        print("Invalid Operation")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Invalid input")
