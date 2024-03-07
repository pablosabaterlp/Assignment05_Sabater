class BasicMathOperations:
    mult = "*"
    div = "/"
    add = "+"
    sub = "-"

    #1: Define the method that takes a first and a last name in the form of a string
    def greeter(first, last):   
        #Print the greeting message with the full name imbeded into the message
        print(f"\nGreetings {first.capitalize()} {last.capitalize()}, have a great day!")
    
    #2: Define method that adds two numbers and returns the sum
    def sum(num1, num2):
        return num1 + num2
    
    #3: Define a method that performs an operation on two numbers
    def operator(num1, num2, op):
        if op == BasicMathOperations.add:
            return num1 + num2
        elif op == BasicMathOperations.sub:
            return num1 - num2
        elif op == BasicMathOperations.mult:
            return num1 * num2
        elif op == BasicMathOperations.div:
            return num1 / num2
        else:
            return "not supported, the operator was incorrect."
    
    #4: Define a method to square a number
    def Square(x):
        return x**2
    
    #5 Define a method for the factorial of a number
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
    
    #6 Define a method for numbers from A to B
    def nums(A, B):
        #print each number in the range from A to B
        for i in range(A, B + 1):
            print(i)
    
    #7 Define a method that computes the hypotenuse of a triangle, using Square function from above
    def hypotenuse(base, height):
        baseSqr= BasicMathOperations.Square(base)
        heightSqr = BasicMathOperations.Square(height)
        return (baseSqr+ heightSqr)**0.5
    
    #8 Define a method to find the area of a rectangle
    def areaRec(width, height):
        return width * height
    
    #9 Define a method to put a number to a power
    def exponent(num, power):
        return num**power
    
    #10 Define a method to get the type of an argument
    def getType(arg):
        return type(arg)

def main():
    operation = BasicMathOperations()
    while True:
        action = int(input("""What would you like to do (choose a number): 
                                1. Greeting
                                2. Sum of two numbers
                                3. Operation of your choice on two numbers
                                4. Square a number
                                5. Factorial of a number
                                6. Range of numbers from A to B
                                7. Find the hypotenuse of a triangle
                                8. Find area of a rectangle
                                9. Get the exponent of a number
                                10. Find the type of an argument
                                11. Exit. """))
        
    

