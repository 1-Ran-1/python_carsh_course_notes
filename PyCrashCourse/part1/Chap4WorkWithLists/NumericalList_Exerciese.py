# 4-3
for value in range(1, 21):
    print(value)    
# 4-4
one_million = list(range(1, 1_000_001))
for value in one_million:
    print(value)
# 4-5
print(min(one_million))
print(max(one_million))
print(sum(one_million))
# 4-6
odd_numbers = [value for value in range(1, 21, 2)]
for odd_number in odd_numbers:
    print(odd_number)
# 4-7
multipules = [value * 3 for value in range(3, 31)]
for multipule in multipules:
    print(multipule)
# 4-8
cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
print(cubes)