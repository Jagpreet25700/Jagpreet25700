from Calculator_logo import logo

print(logo)
def add (n1,n2):
    return n1 + n2

def subtract (n1,n2):
    return n1 - n2    

def multiply (n1,n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2    

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}    

def calculator():
    num1 = float(input("What the first number: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operator = input("Select one of the operations you want to use: ")
        num2 = float(input("What is the next number: "))
        calculation_function = operations[operator]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operator} {num2} = {answer}")
        decision = input(f"Do you want to continue? press 'y' to calculate with {answer} or type 'n' for new calculation or 'no' to discontinue: ")
        if decision == "y":
            num1 = answer
        elif decision == "no":
            should_continue = False     
        else:
            should_continue = False 
            calculator()   

calculator()
