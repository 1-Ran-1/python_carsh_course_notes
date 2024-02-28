                    ####### Organizing a List #########
# ---------------------------------------------------------------------------- #
# Sorting a List Permanently with the sort() Method
    # sort() method change the order alphabetically
print('---- sort()----')
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
# ---------------------------------------------------------------------------- #
# Sorting a List Temporarily with the sorted() Function
    # sorted() function lets you display your list in a particular order
    # but not affect the acutal order
print('---- sorted() ----')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Original list:')
print(cars)
print("\nSorted list:")
print(sorted(cars))
print('\nOriginal list again:')
print(cars)
    # Sorting a list alphabetically is more complicated when all values are not
    # in lowercase  
    # There are several ways to interpret capital letters
# ---------------------------------------------------------------------------- #
# Printing a List in Reverse Order
    # Use .reverse() to rearrange the list into reverse-chronological order
print("---- using .reverse() ----")
cars.reverse()
print(cars)
# ---------------------------------------------------------------------------- #
# Finding the Length of a List
    # Use len() function
print('---- len() ----')
print(len(cars))

