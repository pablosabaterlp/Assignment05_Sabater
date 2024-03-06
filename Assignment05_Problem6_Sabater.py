#Define a method for numbers from A to B
def nums(A, B):
        #print each number in the range from A to B
        for i in range(A, B + 1):
            print(i)

def main():
    #Ask user for first number
    A = int(input("Input the start: "))
    B = int(input("Input the end: "))
    #Print the square
    print(f"\nThe numbers from {A} to {B} are {nums(A, B)}.")