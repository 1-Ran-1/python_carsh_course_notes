# 6-4 Glossary 
programming_words = {'dictionary' : 'collection of key-value pairs',
                     'comments' : 'comments ##',
                     'integer' : 'interger 123',
                     'floats' : 'any number with a decimal point. 1.2',
                     'constants' : 'use all capital letters variable',
                     'string' : 'string',
                     'whitespaces' : 'any # nonprinting characters',
                     'list' : 'a collection of items in a particular order',
                     }

for word, meaning in programming_words.items():
    print(f'[{word}] \nmeaning: {meaning}.')

# 6-5 Rivers
rivers = {'nile' : 'egypt',
          'yangtze' : 'china',
          'mississippi' : 'america'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("The following rivers have been mentioned:")
for river in rivers.keys():
    print(river.title())

print("The following countries have been mentioned:")
for country in rivers.values():
    print(country.title())
    
# 6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

names = ['lanu', 'runhan', 'matthew', 'edward', 'phil']

for name in names:
    if name in favorite_languages.keys():
        print(f"Thank you for responding, {name.title()}.")
    else:
        print(f"Please take the poll, {name.title()}.")
