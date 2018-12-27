#
class User():

    def __init__(self, first_name, last_name, gender, age):
        self.full_name = last_name + ' ' + first_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(self.full_name + ', ' + self.gender + ' ' + str(self.age))

    def greet_user(self):
        print("Hi " + self.full_name)

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts

    def display_login_attempts(self):
        print(self.full_name + " has attempt " + str(self.login_attempts) +
              " times.")

class Privileges():

    def __init__(self):
        self.privileges = ' '

    def set_privileges(self, items):
        self.privileges = items

    def show_privileges(self):
        print(self.privileges)

class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()



user_Admin = Admin('Zhang', 'Peng', 'male', 22)
user_Admin.describe_user()
user_Admin.greet_user()
user_Admin.display_login_attempts()
user_Admin.privileges.set_privileges(['can add post', 'can delete post'])
user_Admin.privileges.show_privileges()


