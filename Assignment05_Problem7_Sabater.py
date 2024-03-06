#7 Define a method that computes the hypotenuse of a triangle
def hypotenuse(base, height):
    return (base**2 + height**2)**0.5

def main():
    #Ask user for base and height numbers
    base = int(input("Input the base: "))
    height = int(input("Input the height: "))
    #Print the hypotenuse
    print(f"\nThe hypotenuse for triangle with base {base} and height {height} is {hypotenuse(base, height)}.")

main()