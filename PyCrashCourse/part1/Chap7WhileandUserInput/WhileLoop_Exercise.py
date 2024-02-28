# 7-4 Pizza Toppings

active = True
prompt = "\nWhat kind of toppings you want? "
prompt += "\nEnter 'quit' to exit. "

while active:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f"\nI'll add {toppings} on your pizza.")

# 7-5 Moive Tickets
active = True
prompt = "\nEnter your age here: "
fail_count = 2
while active:
    age = input(prompt)
    age_num = int(age)
    
    if 0 <= age_num < 3:
        print("Your ticket if free.")
    elif 3 <= age_num < 12:
        print("Your ticket price is $10")
    elif 12 <= age_num <= 150:
        print("Your ticket price is $15.")
    else:
        fail_count -= 1
        print("Please enter valid age and try again."
              "Fail to enter valid age for 2 times will exit the program."
              f"\n{fail_count} chance left.")
        
        if fail_count == 0:
            print("\n Program ended")

# 7-6 Three Exits
# DONE

# 7-7 Infinity
# Press Ctrl + C to end the program
while True:
    print("How I wish you were there.")



