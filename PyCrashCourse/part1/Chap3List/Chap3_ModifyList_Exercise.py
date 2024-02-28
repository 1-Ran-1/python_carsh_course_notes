# 3-4 Guest List
guests = ['gordon ramsay', 'elon musk', 'jensen huang', 'stewie griffin']
for i in range(len(guests)):
    print(f"Hello {guests[i].title()}, would you like to have dinner in my house today?")
# 3-5 Changing Guest List
print("Elon Musk can't make it.")
guests[1] = 'peter griffin'
for i in range(len(guests)):
    print(f"Hello {guests[i].title()}, would you like to have dinner in my house today?")
# 3-6 More Guests
print("More guests are coming!")
guests.insert(0, 'lois griffin')
guests.insert(2, 'brian griffin')
guests.append('chris griffin')
for i in range(len(guests)):
    print(f"Hello {guests[i].title()}, would you like to have dinner in my house today?")
# 3-7 Shrinking Guest List
print("Only 2 people are allowed to stay :(")
for i in range(len(guests) - 2):
    left_guest = guests.pop()
    print(f"Sorry {left_guest.title()}, I will invite you next time.")
del guests[0], guests[0]
print(guests)