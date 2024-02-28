# Introducing while loops
# Whlie loop runs as long as, or WHILE, a certain condition is true.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the User Choose When to Quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
        print(message)

# Using a Flag
# For a progream should run only as long as < many conditions are ture>
# define one variable that 
# determines whether or not the program is active.
# The variable is called a FLAG

# condtions meet --> flag = True
# conditions not meet --> flage = Flase
# flag can help to neatly organize other tests.

# Example of flag

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# set default flag to True
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to Exit a Loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}")

# Using continue in a Loop
# you can use continue statement to return to the beginning of the loop

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    
    print(current_number)

# Avoiding Infinite Loops

x = 1
while x <= 5:
    print(x)
    x += 1

# if you omit the line x += 1
# The Loop will be infinite

# Make sure at least ONE part of the program can make the loop's condition False
# or cause it to reach a break statement

