print("It will be a calculator!")
while True:

    number = float(input("Specify number: "))
    operation = input("Choose operation + - / * % ")
    number2 = float(input("Specify second number: "))

    if operation == "+":
        print("Result is:")
        print(number + number2)

    elif operation == "-":
        print("Result is:")
        print(number - number2)

    elif operation == "*":
        print("Result is:")
        print(number * number2)

    elif operation == "/":
        print("Result is:")
        print(number / number2)

    elif operation == "%":
        print("Result is:")
        print(number % number2)

    if input("Type exit for shutdown or clear for new calculations  (exit/clear): ") == "exit":
        break