#Greet function

#Define the method that takes a first and a last name in the form of a string
def greeter(first, last):
    #Print the greeting message with the full name imbeded into the message
    print(f"\nGreetings {first.capitalize()} {last.capitalize()}, have a great day!")

#Define the method to call the greeter and ask the user for their name 
def main():
    #Create variables for the users first and last name and input it into the greeter method
    firstName = input("What is your first name? ")
    lastName = input("What is your last name? ")
    greeter(firstName, lastName)
#Start the program
main()
