#
river_country = {
    'nile': 'egypt',
    'huanghe river': 'china',
    'duonao river': 'america'
    }
for river, country in river_country.items():
    print("The " + river.title() + " runs through " + country.title())
print("\n")

for river in river_country.keys():
    print(river)
print("\n")

for country in river_country.values():
    print(country)
    
    #
    favorite_languages = {
    'sarah': 'python',
    'mike': 'c',
    'eric': 'java',
    'chen': 'python',
    }
names = ['sarah', 'lina', 'stephen', 'eric']
for name in names:
    if name in favorite_languages.keys():
        print(name.title() + ", Thank you for poll!")
    elif name not in favorite_languages.keys():
        print(name.title() + ", please take our poll!")
