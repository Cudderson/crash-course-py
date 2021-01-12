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

    def describe_user(self):
        print(f"This person's name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"{self.first_name.title()} is {self.age} years old.")
        print(f"{self.first_name} has {self.eye_color} eyes!")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
        print("\n")


user1 = User("John", "Williams", 29, "blue")
user2 = User("Henry", "Bittersweet", 44, "brown")
user3 = User("Cody", "Wells", 26, "red")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
