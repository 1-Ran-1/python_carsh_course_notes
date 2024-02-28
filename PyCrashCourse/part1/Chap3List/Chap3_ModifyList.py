        ####### Modifying, Adding, and Removing Elements #########
# ---------------------------------------------------------------------------- #
    #  Most lists you create will be dynamic
# Modifying Elements in a List
print("---- Modify Elements ----")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)
# ---------------------------------------------------------------------------- #
# Adding Elements to a List
# Python provides several ways to add new data
    # Appending to the End of a List
print("---- Adding Elements ----")
print('using append()')
motorcycles.append('honda')
print(motorcycles)
        # Start with empty list and add items with append
motorcycles = []
motorcycles.append('yamaha')
motorcycles.append('honda')
motorcycles.append('suzuki')
print(motorcycles)
    # Inserting Elements into a List
    # insert(index, content)
print('using insert()')
motorcycles.insert(0, 'ducati')
print(motorcycles)
# ---------------------------------------------------------------------------- #
# Removing Elements from a List
print("---- Remoing elements ----")
    # use del statement if u know the index
print('using del')
del motorcycles[0]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
    # YOU CAN NO LONGER ACCESS THE VALUE THAT WAS REMOVED
    # Removing an Item Using pop() method
    # the pop() method removes the last item in a list
    # but it lets you work with that item after removing
print("using pop()")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
poped_motercycle = motorcycles.pop()
print(motorcycles)
print(poped_motercycle)
    # how might pop() useful?
print(f"the last motorcycle i owned was a {poped_motercycle.title()}.")
    # Popping items from any positon in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(first_owned)
    # use del or pop?
        # delete item and not use that item --> del
        # use that item --> pop
    # Removing an Item by Value
    # Use remove() method if dont know index but value
print("Using remove()")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
    # Advance use
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
    # THE remove() METHOD DELETES ONLY THE FIRST OCCURENCE OF THE VALUE YOU SEPECIFY.
    # USE A LOOP TO MAKE SURE ALL OVVURRENCES OF THE VALUE ARE REMOVED