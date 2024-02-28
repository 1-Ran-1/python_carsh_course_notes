# 7-1 Rental Car
message = "What kind of rental car you like? "
car = input(message)
print(f"Let me see if I can find you a {car.title()}.")

# 7-2 Restaurant Seating
message = "How many people are in your dinner group? "
number = int(input(message))
if number > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")

# 7-3 Multiples of Ten
message = "Give me a random number: "
number = int(input(message))
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")
