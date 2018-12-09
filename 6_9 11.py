#
favorite_places = {
    'mike': ['yueyang', 'hengyang', 'shenzhen'],
    'jack': ['yunnan', 'fenghuang'],
    'ella': ['jiujiang'],
}

for name, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + name + "'s favorite place is: ")
    else:
        print("\n" + name + "'s favorite place are: ")
    for place in places:
        print(place)
    
 #
 cities = {
    'taiwan': {
        'country': 'china',
        'population': '5000k',
        'fact': 'interesting',
    },
    'shanghai': {
        'country': 'china',
        'population': '6000k',
        'fact': 'modern',
    },
}

for city, city_info  in cities.items():
    print("\n" + city.title() + ":")
    for key, value in city_info.items():
        print(key.title() + ": " + value)

        
