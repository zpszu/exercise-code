#
import json
def get_stored_num():
    filename = 'favourite_number.json'
    try:
        with open(filename) as f_obj:
            num = json.load(f_obj)
    except FileNotFoundError:
        print("ERROR!")
    else:
        return num

def favourite_num():
    num = get_stored_num()
    if num:
        print("I know your favourite number is " + str(num))
    else:
        num = input("What is your favourite number?")
        filename = "favourite_number.json"
        with open(filename, 'w') as f_obj:
            json.dump(num, f_obj)
            print("We'll remember your favourite number " + str(num) + "!")
favourite_num()

#
import json
def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        user_same = input("What is your name? ")
        while True:
            if user_same == username:
                print("Welcome back, " + user_same + "!")
                break
            elif user_same != username:
                print("Please enter the right username!\n")
                user_same = get_new_username()
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()






