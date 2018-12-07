#
age = 5

if age < 2:
    print("He is baby.")
elif age < 4:
    print("He is learning walking.")
elif age < 13:
    print("He is a child.")
elif age < 20:
    print("He is a teenager.")
elif age < 65:
    print("He is an adult.")
elif age >= 65:
    print("He is an elder man")

#
favorite_fruits = ['apple', 'pear', 'watermelon']
fruits = ['apple', 'pear', 'watermelon','banana']

if 'apple' in favorite_fruits:
    print("You really like apple")
if 'pear' in favorite_fruits:
    print("You really like pear")
if 'watermelon' in favorite_fruits:
    print("You really like watermelon")
if 'banana' in favorite_fruits:
    print("You really like banana")

for fruit in fruits:
    if fruit in favorite_fruits:
        print("You really like " + fruit)





