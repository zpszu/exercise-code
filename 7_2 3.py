#
person = input("Tell me how many person there are: ")
person = int(person)

if person > 8:
    print("There is no table free now!")
else:
    print("There is table free now!")

#
num = input("Please enter a number: ")
num = int(num)

if num % 10 == 0:
    print(str(num) + " is a multiple of 10")
else:
    print(str(num) + " is not a multiple of 10")
