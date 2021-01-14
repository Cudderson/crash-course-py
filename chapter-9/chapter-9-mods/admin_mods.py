# 9-11, mods for users_cc


class User:
    """basic blueprint for a person"""

    def __init__(self, first_name, last_name, age, eye_color):
        """Initialize attributes for a person"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.eye_color = eye_color
        self.login_attempts = 0

    def describe_user(self):
        print(f"This person's name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"{self.first_name.title()} is {self.age} years old.")
        print(f"{self.first_name} has {self.eye_color} eyes!")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        print(f"{self.first_name} {self.last_name} attempted to login.")
        self.login_attempts += 1

    def reset_login_attempts(self):
        print(f"Resetting login attempts for {self.first_name}...\n")
        self.login_attempts = 0


class Admin(User):
    """child class of 'User', specifically for admins"""

    def __init__(self, first_name, last_name, age, eye_color):
        super().__init__(first_name, last_name, age, eye_color)
        # attribute as an instance of class Privileges
        self.privileges = Privileges()


class Privileges:
    """Describes privileges of a user"""
    def __init__(self):
        self.privileges_list = ["can ban users", "can view logistics", "can push new code"]

    def show_privileges(self):
        print(f"\nThese are the special privileges of Admin:")
        for privilege in self.privileges_list:
            print(f"\t- {privilege}")
