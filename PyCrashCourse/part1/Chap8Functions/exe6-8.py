# 8-6 City Names

def city_country(city_name, country='china'):
    return f"\"{city_name.title()}, {country.title()}\""

print(city_country('qingzhou'))
print(city_country('heze'))
print(city_country('manchester', 'united kingdom'))

# 8-7 Albums

def make_album(artist_name, album_title, song_num=None):
    if song_num:
        album = {'name' : artist_name,
                 'album' : album_title,
                 'number of songs' : song_num,
                 }
    else:
        album = {'name' : artist_name,
                'album' : album_title,
                }
    return album

print(make_album('buckethead', "it's alive", song_num=8))
print(make_album('matt rach', 'classik'))
print(make_album('king crimson', 'islands'))

# 8-8 User Albums

index = 1
TotalDict = {}
while True:
    print("enter 'q' anytime to quit.")
    name = input("artist name: ")
    if name == 'q':
        break
    title = input("album title: ")
    if title == 'q':
        break
    album_dict = make_album(name, title)
    TotalDict[index] = album_dict
    index += 1
    
print(TotalDict)