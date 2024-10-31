#Implementing various functions 
# Addition function 
def Add(a,b):
    return  a + b

# Subtraction function 
def Subtract(a,b):
    return a - b

# Multiplication function 
def Multiply(a,b):
    return a * b

# Division function 
def Division(a,b):
    return a / b

# Input and Output handling
def Validate_input(a,b,operator):
    # Validate operator
    if operator not in ["+","-","*","/"]:
        print("Invalid Operator!")
        return None 
    # Handle division by zero
    if operator == "/" and b == 0:
        print("Error: Division by zero is not allowed")
        return None 
    
    try:
        # Convert the input into float 
        a = float(a)
        b = float(b)
        return a, b, operator
    except ValueError:
        print("Invalid value,please enter a numeric value")
        return None 
    
# Get user input 
def GetInput():
    a = float(input("Enter the numeric value: "))
    b = float(input("Enter the numeric value: "))
    return a, b

# Perform Operators 
def PerformOperators(a,b,operator):
    if operator == "+":
        return Add(a,b)
    elif operator == "-":
        return Subtract(a,b)
    elif operator == "*":
        return Multiply(a,b)
    elif operator == "/":
        return Division(a,b)
    else:
        return "Invalid operator"

# Introduction  
print("THIS IS A CALCULATOR")
use = """
1.Enter first value and then second
2.Maximun number of value to enter is 2 only 
3.The following operators are +,-,/,*
"""
print(use)
    
# Main calculator logic
def RunCal():
    while True:
        a, b = GetInput()
        operator = input("Enter the operator (+,-,/,*): ")

        # Validate inputs and operator
        validated = Validate_input(a,b,operator)

        if validated:
            a, b, operator = validated
            result = PerformOperators(a ,b , operator)
            if result is not None:
                print(f"The result is {result} ")
            else:
                print("Try again!")
        else:
            print("Invalid input,please try again")

        # Ask the user if they want to perform another calculation
        another = input("Do you want perform another calculation? (yes/no) ")
        if another != "yes":
            break

if __name__ == "__main__":
    RunCal()






