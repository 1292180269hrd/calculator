num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '*':
    print(num1 * num2)
elif operation == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operation")
