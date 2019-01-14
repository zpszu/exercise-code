while True:
    user_name = input("Please enter uer name: ")
    filename = 'guest.txt'
    reason = input("Why do you love programming?\n")
    with open(filename, 'w') as file_object:
        file_object.write(user_name.title() + ": " + reason + "\n")
