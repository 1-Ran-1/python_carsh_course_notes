#  9 - 1 class Restaurant
class Restaurant: 
    '''
    A simple model of a restaurant
    '''
    
    def __init__(self, restaurant_name, cuisine_type):
        '''
        Initialize name and type attributes
        '''
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"This is a {self.type} restaurant called {self.name}.")
        
    def open_restaurant(self):
        print("The restaurant is open now.")

wasabi = Restaurant('wasabi', 'japanese food')
print(wasabi.name)
print(wasabi.type)
wasabi.describe_restaurant()
wasabi.open_restaurant()

print("\n================9 - 2===================\n")

# 9 - 2 Three Restaurants
kfc = Restaurant('KFC', 'fast food')
five_guys = Restaurant('Five Guys', 'fast food')

kfc.describe_restaurant()
five_guys.describe_restaurant()

print("\n================9 - 3====================\n")

# 9 - 3 Users
class User:
    """
    A simple user class demo
    """
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
    
    def describe_user(self):
        print(f"{self.first_name.title()} {self.last_name.title()}, {self.gender.title()}, {self.age} years old.")
    
    def greet_user(self):
        full_name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {full_name.title()}!")

catcore = User('Chuhan', 'wang', 21, 'male')
catcore.describe_user()
catcore.greet_user()

lanuzt = User('Tong', 'zhang', 20, 'male')
lanuzt.describe_user()
lanuzt.greet_user()

wwyyyds = User('wenyu', 'Wang', 21, 'male')
wwyyyds.describe_user()
wwyyyds.greet_user()

user_list = [catcore, lanuzt, wwyyyds]

for user in user_list:
    user.greet_user()