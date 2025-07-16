import logging
from datetime import datetime

# Setup logging
logging.basicConfig(filename='calculator.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Try again.")

def get_operator():
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Enter an operator (+, -, *, /): ")
        if op in valid_operators:
            return op
        else:
            print("Invalid operator. Try again.")

def calculate(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        if y == 0:
            print("Error: Division by zero.")
            return None
        return x / y

def main():
    print("Welcome to the Python Calculator!")
    x = get_number("Enter the first number: ")
    op = get_operator()
    y = get_number("Enter the second number: ")

    result = calculate(x, y, op)
    if result is not None:
        print(f"Result: {x} {op} {y} = {result}")
        logging.info(f"{x} {op} {y} = {result}")
    else:
        logging.error(f"{x} {op} {y} = Error")

if __name__ == "__main__":
    main()
