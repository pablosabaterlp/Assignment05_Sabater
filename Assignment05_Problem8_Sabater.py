#Define a method to find the area of a rectangle
def areaRec(width, height):
        return width * height

def main():
    #Ask user for width and height numbers
    width = int(input("Input the base: "))
    height = int(input("Input the height: "))
    #Print the area
    print(f"\nThe area for rectangle with width {width} and height {height} is {areaRec(width, height)}.")

main()