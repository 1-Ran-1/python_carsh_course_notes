# How the input() Fucntion Works

# input()
#  -> pause program
#  -> wait for user input
#  -> receive and assign input to a variable

# A exmaple echo program
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Writing clear prompts
# Always include a clear prompt when you use input()
# Make it CLEAR to your user WHERE to enter their text.  

# You can assign your prompt to a variable and pass that variable to input()

prompt = "If you share your name, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name.title()}!")

# Using int() to Accept Numberical Input
age = input("How old are you? ")
# the input value get here is stored as string
# use int() function to convert the input str to int value
# this allows the comparison to run.
print(int(age) >= 18)

# Example to use int()
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("You'll be able to ride when you're a little older.")

# The Modulo Operator %
# divides one number by another number and returns the remainder
print(4 % 3)

# use % to determine if a number is even or odd:
number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
