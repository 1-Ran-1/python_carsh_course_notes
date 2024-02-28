# 5-1 Conditional Tests
motorcycle = 'yamaha'
print("Is motorcycle == 'honda'? I predict False.")
print(motorcycle == 'honda')

print("\nIs motorcycle == 'yamaha'? I predict True")
print(motorcycle == 'yamaha')

horsepower = 500
print(horsepower >= 500 and motorcycle == 'yamaha')
print(horsepower >= 200 and horsepower == 'honda')
print(horsepower < 500 or motorcycle == 'yamaha')
print(horsepower < 500 or motorcycle == 'honda')
# 5-2 More Conditonal Tests
buckethead = ['N', 'Y', 'C', 'The left Panel', 'Ev']
print('n'.title() in buckethead or 'ruby tuesday' in buckethead)
print('islands'.title() not in buckethead and 'endgame'.title() not in\
    buckethead)