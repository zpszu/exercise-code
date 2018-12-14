#
sandwich_orders = ['aa', 'pastrami', 'bb',  'pastrami', 'cc', 'pastrami', 'dd']
finished_sandwiches = []

print("The pastrami sandwiches have sold out!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
print("\n")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + ' sandwich.')
    finished_sandwiches.append(sandwich)

print("Your sandwiches have finished as followed:\n")
for sandwiches in finished_sandwiches:
    print(sandwiches, end=' ')

 #
 prompt = "If you could visit one place in the world, where would you go? "
user = {}
active = True

while active:
    user_name = input("\nWhat is your name?")
    place = input(prompt)
    user[user_name] = place
    another = input("Any one else need to poll? (yes/ no)")
    if another == 'no':
        active = False

print("\n--- Poll Results ---")
for name, places in user.items():
    print(name.title() + " wants to visit " + places.title())
