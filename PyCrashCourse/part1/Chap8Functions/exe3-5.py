# 8-3 T-Shirt

def make_shirt(size, text='I love Python.'):
    print(f"making a T-shirt, size: {size}, with a message \"{text}\".")
    
make_shirt('large', 'hello world.')
make_shirt(size='medium', text='try it yourself.')

# 8-4 Large Shirts
make_shirt('large')
make_shirt('medium')
make_shirt('any', 'different message')

# 8-5 Cities
def describe_city(city_name, country='china'):
    print(f"{city_name.title()} is in {country.title()}.")
describe_city('qingzhou')
describe_city('heze')
describe_city('manchester', 'united kingdom')