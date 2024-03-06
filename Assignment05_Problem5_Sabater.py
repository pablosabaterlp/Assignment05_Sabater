#Define a method for the factorial of a number
def factorial(n):
    #Define the result variable, which can never be less than 1
    result = 1
    #If the number is 0 or 1 because they don't have factorial the result is 1
    if n == 0 or n == 1:
        return result
    else:
        #Recurse for all values up to n, including, and multiply the result by each number, making it the new result each time
        for i in range(n):
            result *= i+1
        return result

def main():
    #Ask user for first number
    num1 = int(input("Input n: "))
    #Print the square
    print(f"\nThe factorial of {num1} is {factorial(num1)}.")

main()