def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

my_dic = {
    "+" : addition,
    "-" : subtraction,
    "*" : multiplication,
    "/" : division
}

# print(my_dic["*"](4,8))
def calculator():
    should_accumulate = True
    first_no = float(input("What is the first number?: "))
    while should_accumulate:

        for symbol in my_dic:
            print(symbol)

        ope_symbol = input("Pick an operation: ")
        second_no = float(input("What is the second number?: "))

        value = my_dic[ope_symbol](first_no, second_no)
        print(f"{first_no} {ope_symbol} {second_no} = {value}")

        want_continue = input(f"Type 'yes' to continue calculating with"
                              f" {value}, or type 'no' to start a new calculation: ").lower()

        if want_continue == "yes":
            first_no = value

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()

