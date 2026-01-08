import art

def add(n1, n2):
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# TODO: Add these 4 functions into a dictionary as the values. Keys = "+", "-", "*", "/"

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# TODO: Use the dictionary operations to perform the calculations.

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number: "))

    while should_accumulate:    # keep the function going until the user says stop and restart
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with the previous {answer}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_accumulate = False
            print("\n" * 20)
            calculator()    # will restart the function
        else:
            return "Calculator has stopped"
    return None


calculator()    # will run the function
