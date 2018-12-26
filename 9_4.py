#
class Restaurant():

    def __init__(self, name, type):
        self.restaurant_name = name
        self.restaurant_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.restaurant_name)
        print("It's a " + self.restaurant_type + " restaurant")

    def open_restaurant(self):
        print("It's opening")

    def number_served_reading(self):
        print("There are " + str(self.number_served) +
              " people who have been eating here!")

    def set_number_served(self, num):
        if num >= 0:
            self.number_served = num
        else:
            print("Negative Error!")

    def increment_number_served(self, nums):
        self.number_served += nums

my_restaurant = Restaurant('ZPPPPP', 'Chinese_food')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served_reading()

my_restaurant.set_number_served(100)
my_restaurant.number_served_reading()

my_restaurant.increment_number_served(200)
my_restaurant.number_served_reading()

