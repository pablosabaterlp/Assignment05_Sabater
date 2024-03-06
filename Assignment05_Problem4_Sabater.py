#Define method for squaring a number:
def square(x):
    return x**2

def main():
    #Ask user for first number
    num1 = int(input("Input the number: "))
    #Print the square
    print(f"\nThe square is {square(num1)}.")