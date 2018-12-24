#
class Restaurant():

    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name.title())
        print("The type of the restaurant is " + self.restaurant_type.title())

    def open_restaurant(self):
        print("The restaurant is opening!")

my_restaurant = Restaurant('kkk', 'bb')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
