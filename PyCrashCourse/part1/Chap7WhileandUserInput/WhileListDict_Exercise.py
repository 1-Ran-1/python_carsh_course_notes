# 7-8 Deli

sandwich_orders = ['tuna sandwich', 
                   'pastrami sandwich',
                   'sausage sandwich',
                   'beef sandwich', 
                   'vegan sandwich',
                   'pastrami sandwich',
                   'pastrami sandwich',
                   'tuna sandwich',]
finished_sandwiches = []

print("The Deli has run out of pastrami.")

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders != []:
    sandwich = sandwich_orders[0]
    print(f"I made your {sandwich}.")

    finished_sandwiches.append(sandwich_orders.pop(0))

print(f"I made {len(finished_sandwiches)} sandwiches: ")
count = 1
for sandwich in finished_sandwiches:
    print(f"\t{count}. {sandwich} ")
    count += 1
    
# 7-9 No Pastrami
# Done

# 7-10 Dream Vacations
prompt = "If you coule visit one place in the world, "
prompt += "where would you go? \n"
polling_active = True
poll = {}



while polling_active == True:
    repeat = ''
    print("==== Dream Vacation Investigation ====")
    place = input(prompt)
    name = input("Enter your name please: \n")
    poll[name] = place
    while repeat not in ['N', 'Y', 'y', 'n']:
        repeat = input("Would you like to let another person respond? (Y/N) \n")
        if repeat in ['N', 'n']:
            polling_active = False
        elif repeat in ['Y', 'y']:
            continue
        else:
            print("Invalid input, try again.")

print(f"Total {len(poll)} people took the survey: ")
for name, place in poll.items():
    print(f"{name.title()} would like to go to {place}.")