while True:
    number1 = int(input("Type the first number:\n"))
    number2 = int(input("Type the second number:\n"))
    operation = input("Type the operation (add, multiply, subtract, divide) or 'quit' to exit:\n")
    if operation == "quit":
        break
    if operation == "add":
        print("Result:", number1 + number2)
    if operation == "multiply":
        print("Result:",number1 * number2)
    if operation == "subtract":
        print("Result:",number1-number2)
    if operation == "divide":
        if number2 != 0:
            print("Result:",number1/number2)
        else:
            print("Second number is 0. Can't divide by 0.")
    else:
        print("Can't accept that operation.")
        break