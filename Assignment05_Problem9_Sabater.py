#9 Define a method to put a number to a power
def exponent(num, power):
    return num**power

def main():
    #Ask user for num and power numbers
    num = int(input("Input the number: "))
    power = int(input("Input the power: "))
    #Print the power
    print(f"\n{num} to the power of {power} is {exponent(num, power)}.")

main()