# 4-10
import statistics
one_million = list(range(1, 1_000_001))
print("The first 3 items in the list are:")
for item in one_million[0:3]:
    print(item)
print("\nTwo items form the middle of the list are:")
for item in one_million[499_999:500_001]:
    print(item)
print("\nThe last three items in the list are:")
for item in one_million[-3:]:
    print(item)

# 4-11
pizzas = ['margherita', 'pepperroni', 'romana tonda', 'hawaiian']
friend_pizzas = pizzas[:]
pizzas.append('new york style')
friend_pizzas.append('buffalo chicken')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza.title())
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza.title())
    
# 4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)