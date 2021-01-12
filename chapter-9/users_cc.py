# 9-3
# describing a person using Class

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
        print("\n")

    def increment_login_attempts(self):
        print(f"{self.first_name} {self.last_name} attempted to login.")
        self.login_attempts += 1

    def reset_login_attempts(self):
        print(f"Resetting login attempts for {self.first_name}...\n")
        self.login_attempts = 0


# instances of User class
user1 = User("John", "Williams", 29, "blue")
user2 = User("Henry", "Bittersweet", 44, "brown")
user3 = User("Cody", "Wells", 26, "red")

# describe and greet each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

# simulates 'user3' attempting to login and records it
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()

# proof of function, comparing login attempts for 'user3' and 'user2'
print("\n")
print(f"Login attempts for {user3.first_name} {user3.last_name} is {user3.login_attempts}")
print(f"Login attempts for {user2.first_name} {user2.last_name} is {user2.login_attempts}\n")

# Reset login attempts to 0
user3.reset_login_attempts()
print(f"Login attempts for {user3.first_name} is now {user3.login_attempts}")