        ####### Looping Through an Entire List #########
# ---------------------------------------------------------------------------- #
# Python for loop basics
# Create a list
print('---- for loop basics ----')
magicians = ['alice', 'david', 'carolina']
# Pull a name from the list and associate it with variable 'magician'
for magician in magicians:
    print(magician)
# It's helpful to choose a meaningful name that represents a single item from
# the list as temporary variable.
# like:
# for cat in cats: \ for item in list_of_items:
# ---------------------------------------------------------------------------- #
# Doing Mork Work Within a for Loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    # Doing Something After a for Loop:
print("Thank you, everyone. That was a great magic show!")
# ---------------------------------------------------------------------------- #
# Avoiding Indentation Errors
# Always check indentation, colon and logic