#Sum 

#Define method that adds two numbers and returns the sum
def sum(num1, num2):
    return num1 + num2

#Define method to ask for user input and output sum
def main():
    #Ask user for first and second numbers
    num1 = int(input("Input the first number: "))
    num2 = int(input("Input the second number: "))
    #Print the two numbers and the sum imbeded into a string
    print(f"\nThe sum of {num1} and {num2} is {sum(num1, num2)}")

#Run the function when the program runs
main()