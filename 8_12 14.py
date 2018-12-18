#
def make_sandwich(*toppings):
    print("The sandwich is made by following toppings: ")
    for topping in toppings:
        print("-" + topping)

make_sandwich('aa')
make_sandwich('aa', 'bb')
make_sandwich('aa', 'bb', 'cc')

#
def make_car(producer, model, **car_info):
    car_information = {}
    car_information['producer'] = producer
    car_information['model'] = model
    for key, value in car_info.items():
        car_information[key] = value
    return car_information

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
