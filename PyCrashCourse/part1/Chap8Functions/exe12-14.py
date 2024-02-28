# 8-12 Sandwiches

def make_sandwich(*sandwiches):
    print(f"Total {len(sandwiches)} sandwiches have been made: ")
    for sandwich in sandwiches:
        print(f" - {sandwich} sandwich")

make_sandwich('vegan')   
make_sandwich('mushroom', 'vegan')
make_sandwich('cheese', 'mushroom', 'chicken', 'vegan', 'vegan')

# 8-13 User profile

def build_profile(first, last, **user_info):
    """
    Buidl a dictionary containing everything we know about a user.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

userprofile = build_profile('chuhan', 'wang',
                            location='Sydney',
                            education='University of Sydney',
                            major='computer science')

print(userprofile)

# 8-14 Cars
# golf_gti = {'cubic capacity' : '1984cc',
#             'max output' : '245ps',
#             'max torque' : '370Nm',
#             'cyclinders' : 4,
#             '0-100 acc' : '6.3s',
#             'manufacturer' : 'volkswagen'
#             }

def car_info(manufacturer, model_name, **car_info):
    """_summary_

    Args:
        manufacturer (str): manufacturer info
        model_name (str): model name of car

    Returns:
        dict[str]: dictionary contains all info about the car
    """
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

golf_gti = car_info('volkswagen', 'golf gti', torque='370Nm', output='245ps', cyc=4)
print(golf_gti)
