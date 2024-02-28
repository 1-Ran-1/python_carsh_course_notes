# 6-1 Person
info = {'first_name' : 'Runhan',
        'last_name' : 'Li',
        'age' : '21',
        'city' : 'Qingzhou'}
print(info['first_name'])
print(info['last_name'])
print(info['age'])
print(info['city'])

# 6-2 Favorite Numbers
favorite_numbers = {'Cory' : 17,
                    'Runhan' : 17,
                    'Sarah' : 12,
                    'Lanu' : 6,
                    'Floyd' : 1
                    }

for name in favorite_numbers:
    print(f"{name}'s favorite number is {favorite_numbers[name]}.")

# 6-3 Glossary
programming_words = {'dictionary' : 'collection of key-value pairs',
                     'method' : ' functions that are associated with an object\
 and can manipulate its data or perform actions on it'}

for word in programming_words:
    print(f'{word} is {programming_words[word]}.')