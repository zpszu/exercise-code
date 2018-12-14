#
def make_shirt(size, word):
    print("The size of T-shirt is " + size + ", and the word is " + word)
make_shirt('large','cool')
make_shirt(word='out', size='small')

#
def make_shirt(size='large', word='I love Python'):
    print("The size of T-shirt is " + size + ", and the word is " + word)
make_shirt()
make_shirt(size='medium')
make_shirt(word='keep moving')

#
def describe_city(city_name, country='china'):
    print(city_name.title() + " is in " + country.title())

describe_city('shanghai')
describe_city('reykjavik', 'iceland')
describe_city(country='america', city_name='san fransisco')

