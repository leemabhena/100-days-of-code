from Day_10_art import logo

def add(n1, n2):
    """Takes Two numbers and add them together"""
    return n1 + n2

def subtract(n1, n2):
    """Takes Two numbers and subtract them"""
    return n1 - n2

def multiply(n1, n2):
    """Finds product of two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Finds quotient of two numbers"""
    return n1 / n2

def calculator():
    print(logo)
    operations = {'+': add, '-': subtract, '/': divide, '*': multiply}

    num1 = int(input("Enter First Number: "))
    for operation in operations:
        print(operation)

    still_calculating = True

    while still_calculating:
        operation_symbol = input('Pick an operation: ')
        num2 = int(input("Enter next number: "))
        func = operations[operation_symbol]
        answer = func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        should_continue = input(f"Type 'y' to continue calculating with {answer}, or 'n' to exit: ")
        if should_continue == 'y':
            num1 = answer
        else:
            still_calculating = False
            calculator()
calculator()









