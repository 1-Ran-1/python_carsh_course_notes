# 6-7 People
people = {
    'runhan': {
        'first_name' : 'runhan',
        'last_name' : 'li',
        'age' : '21',
        'city' : 'qingzhou'
        },
    'tong': {
        'first_name' : 'tong',
        'last_name' : 'zhang',
        'age' : '21',
        'city' : 'heze'
        },
    'chuankai': {
        'first_name' : 'chuankai',
        'last_name' : 'lu',
        'age' : '22',
        'city' : 'qingzhou'
        }
    }

for name, info in people.items():
    full_name = f"{info['first_name']} {info['last_name']}"
    print(f"\n{full_name.title()}:"
          f"\n\tAge: {info['age'].title()}"
          f"\n\tCity: {info['city'].title()}"
          )

# 6-8 Pets

stewie = {
    'name': 'stewie',
    'kind': 'infant',
    'owner': 'peter griffin',
    'age': '5',
    }

brian = {
    'name': 'brian',
    'kind': 'dog',
    'owner': 'stwart griffin',
    'age' : '10',
    
    }

meg = {
    'name': 'meg',
    'kind': 'unknown',
    'owner': 'peter griffin',
    'age': '16',
    }

pets = [stewie, brian, meg]

for pet in pets:
    print(f"\nName: {pet['name'].title()}:"
          f"\nOnwer: {pet['owner'].title()}"
          f"\nAge: {pet['age']}\n"  
          )

# 6-9 Favorite Places

favorite_places = {
    'lanu' : ['manchester', 'liverpool', 'heze'],
    'cory' : ['bath', 'shanghai', 'hangzhou'],
    'runhan' : ['wuhan', 'qingzhou'],
    'matthew' : ['dongying']
    }

for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is {places[0].title()}")
    else:
        print(f"\n{name.title()}'s favorite places are:")
        for place in places:
            print(f"\n\t{place.title()}")

# 6-10 Favotite Numbers
favorite_numbers = {'Cory' : [17, 7],
                    'Runhan' : [17, 3],
                    'Sarah' : [4, 8, 9],
                    'Lanu' : [2, 12, 6],
                    'Floyd' : [1],
                    }

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}'s favorite number is {numbers[0]}")
    else:
        print(f"\n{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f'\t{number}')

# 6-11 Cities
cities = {
    'qingzhou': {
        'country': 'china',
        'population': '900,000',
        'famous': 'ancient budda sculpture',
        },
    'manchester':{
        'country': 'united kingom',
        'population': '1,000,000',
        'famous': 'industry and football'
        },
    'paris': {
        'country': 'france',
        'population': '2,160,000',
        'famous': 'art',
        },
    }

for name, info in cities.items():
    print(f"\n{name.title()} is a city of {info['country'].title()} "
          f"with a population of {info['population']},"
          f"\nand it's famous for {info['famous']}."
          )
    
# 6-12 Extensions

# Done.