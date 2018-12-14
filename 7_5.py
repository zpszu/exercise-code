#
prompt = "\nHow old are you? "

age = ""
while age != 'quit':
    age = input(prompt)
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("You are free for this movie.")
        elif age <= 12:
            print("your price of ticket is $10.")
        elif age > 12:
            print("your price of ticket is $15.")
            
#
prompt = "\nHow old are you? "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("You are free for this movie.")
        elif age <= 12:
            print("your price of ticket is $10.")
        elif age > 12:
            print("your price of ticket is $15.")

#
prompt = "\nHow old are you? "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("You are free for this movie.")
        elif age <= 12:
            print("your price of ticket is $10.")
        elif age > 12:
            print("your price of ticket is $15.")
