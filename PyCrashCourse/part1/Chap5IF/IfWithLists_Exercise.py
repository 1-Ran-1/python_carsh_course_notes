# 5-8 Hello Admin
# 5-9 No Users

usernames = ['admin', 'default', 'sickevil1', 'wasabi.w', 'ironknory']
# usernames = []
username = ''
if usernames:

    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
        
    elif username in usernames:
        print(f"Hello {username}, thank you for logging in again.")
        
    else:
        print('Invalid username, please register first.')
        
else:
    print('We need to find more users!')
    
# 5-10 Checking usernames:

current_users = ['sickevi1', 'ironknory', 'lanu', 'havoc', 'pixy', 'lnjn']
new_users = ['sickevi1', 'Ironknory', 'LANU', 'hq', 'christysty']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry, the username '{new_user}' already been used,"
              "please enter a new username.")
    else:
        print("This username is available.")

# 5-11 Ordinal Numbers
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(f"{number}th")