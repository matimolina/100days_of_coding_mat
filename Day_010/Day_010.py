##functions with output
from art import logo

def format_name (f_name, l_name):

    f_name_new=f_name.title()
    l_name_new=l_name.title()
    f"Result: {f_name_new} {l_name_new}"

format_name("MATIAS","molina")

#Calculator
#add
def add(n1,n2):
    return n1+n2

#Substract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2

#divide
def divide(n1,n2):
    return n1/n2

operations={
    "+":add,
    "-":subtract,
    "*": multiply,
    "/":divide
    }

def calculator():
    print(logo)

    num1=int(input("What is the first number?: "))
    for key in operations:
        print(key)
    should_continue=True

    while should_continue:
        operation_symbol=input("Pick an operation from the line above: ")
        num2=int(input("What is the next number?: "))
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2) 

        print (f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ")=="y":
            num1=answer
        else:
            should_continue = False
            calculator()

calculator()
