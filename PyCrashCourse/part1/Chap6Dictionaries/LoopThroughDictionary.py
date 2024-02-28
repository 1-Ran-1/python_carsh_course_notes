# Looping through All Key-Value Pairs
user_0 = {
    'user_name' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
    }

# for loop

for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# .items() returns a sequence of key-value pairs.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print("\n")

# Looping Through All Keys
# keys() method

for name in favorite_languages.keys():
    print(name.title())

# Looping through the keys is the default behavior
# so this code will have exactly the same output:
# for name in favorite_languages:

friends = ['phil', 'sarah']    
for name in favorite_languages.keys():
    # print all names
    print(f"Hi {name.title()}.")
    
    # check whether name in list 'friend' 
        # if it is, get language print another message
        # if not skip
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")


# Use .keys() to check if a key exist

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    
# Looping through a Dictionary's Keys in a Paticular Order
# sort the keys returned in the for loop:
# sorted() get all keys and sort them before starting the loop.

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through all values

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# This approach pulls all values without checking for repeats
# to see results without repetition we can use a 'set'

print(set(favorite_languages.values()))

# set and dictionary are both warpped in braces
    # set do not retain items in any specific order
    # set is non-repetitive
    # set has no key-value pairs
    