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

user = User('Zhang', 'Peng', 'male', 22)
user.describe_user()
user.greet_user()
user.display_login_attempts()

user.increment_login_attempts()
user.display_login_attempts()

user.increment_login_attempts()
user.display_login_attempts()

user.increment_login_attempts()
user.display_login_attempts()

user.reset_login_attempts()
user.display_login_attempts()

