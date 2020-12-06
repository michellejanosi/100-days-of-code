from art import logo
print(logo)

def calculator():
    # add
    def add(num1, num2):
        return num1 + num2

    # subtract
    def subtract(num1, num2):
        return num1 - num2

    # multiply
    def multiply(num1, num2):
        return num1 * num2

    # divide 
    def divide(num1, num2):
        return num1 / num2

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        calculate_function = operations[operation_symbol]
        answer = calculate_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calculate_again = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or 'q' to quit: ")

        if calculate_again == 'y':
            num1 = answer
        elif calculate_again == 'n':
            should_continue = False
            calculator()
        else:
            break

calculator()
