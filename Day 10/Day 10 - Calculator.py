from art import logo
#Functions

def add(f_num,s_num):
    return f_num + s_num

def subtract(f_num,s_num):
    return f_num - s_num

def multiply(f_num,s_num):
    return f_num*s_num

def divide(f_num,s_num):
    return f_num/s_num

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculations():
    print(logo)
    should_continue = True
    f_num = float(input("What's the next number?: "))
    while should_continue:

        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        s_num = float(input("What's the next number?: "))
        function = operations[operation_symbol]
        result = function(f_num,s_num)

        print(f"{f_num} {operation_symbol} {s_num} = {result}")

        if input(f"Type 'y' to continue calculating with {result}: and 'n' start from scratch").lower() == "y":
            f_num = result
        else:
            should_continue = False
            calculations()

calculations()



