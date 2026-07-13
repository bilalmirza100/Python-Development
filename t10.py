def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div
}
def calculator():
    num1 = float(input("What is the first number ?"))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operations_symbol = input("Pick an operation from the list above:")
        num2 = float(input("What is the second number ?"))
        calculation_symbol = operations[operations_symbol]
        first_answer = calculation_symbol(num1, num2)

        print(f"{num1} {operations_symbol} {num2} = {first_answer}")
        if input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = first_answer
        else:
            should_continue = False
            calculator()

calculator()