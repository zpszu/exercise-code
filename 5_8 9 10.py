#
user_name = ['admin', 'mike', 'lina', 'jack', 'kevin']
for user in user_name:
    if user == "admin":
        print("Hello Admin, would you like to see status report?")
    else:
        print("Hello " + user + ", thank you for logging in again.")
       
#
user_name = []
if user_name:
    for user in user_name:
        if user == "admin":
            print("Hello Admin, would you like to see status report?")
        else:
            print("Hello " + user + ", thank you for logging in again.")
else:
    print("We need to find some users!")
    
#
current_users = ['mike', 'lina', 'jack', 'kevin', 'eric']
new_users = ['Mike', 'hebe', 'Jack', 'admin', 'taylor']

for user in new_users:
    if user.lower() in current_users:
        print("You need to input other name!")
    else:
        print("This name is available!")
