            ####### Working with Part of List #########
# ---------------------------------------------------------------------------- #
# Work with a specific group of items in a list, called a slice in Python
# Slicing a List
# Specify the index of first and last elements.
print('---- Slicing a List ----')
players = ['charles', 'martina', 'micheal', 'florence','eli']
# 0:3 print index 0, 1, 2
print(players[0:3])
# Python automatically starts from 0 if u omit the first index
print(players[:4])
# vice versa
print(players[2:])
# As a negative number returns an element a certain distance from the end
# of the list. 
# Therefore, you can output any slice from the end of list.
# This prints the last 3 players
print(players[-3:])
# Include a third value in brackets indicating a slice:
# third value tells Python how many items to skip between items.
print(players[0:5:1])
# 0:5:2 will result in index 1 and 3 skipped
print(players[0:5:2])
print(players[0:4:2])
# ---------------------------------------------------------------------------- #
# Looping Through a Slice
print('---- Looping Through a Slice ----')
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())
# ---------------------------------------------------------------------------- #
# Copying a List
print('---- Copying a List ----')
# Make a slice that includes the entire original list
# by omitting both index ([:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\n My friend's favorite foods are:")
print(friend_foods)

# Simply set friend_foods = my_foods WOULD NOT produce 2 seperate lists.
# this syntax actually result in both variables point to the same list.