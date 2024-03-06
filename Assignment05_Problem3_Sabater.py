#Define a method that performs an operation on two numbers
def operator(num1, num2, op):
    #Check the inputted operator to match with the four basic operators, and whichever it matches with will be performed
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2
    #If the input doesn't work, print 
    else:
        return "not supported, the operator was incorrect."

def main():
    #Ask user for first and second numbers
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    op = input("Input the operation to be performed (+, -, *, /): ")
    #Print the two numbers and the sum imbeded into a string
    print(f"\nThe answer is {operator(num1, num2, op)}.")

main()