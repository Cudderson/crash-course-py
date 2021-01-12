# 9-1, 9-2
# Class practice


class Restaurant:
    """class blueprint for a restaurant"""

    def __init__(self, r_name, cuisine_type):
        self.r_name = r_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"This restaurant is called {self.r_name}")
        print(f"{self.r_name} serves {self.cuisine_type} food!")

    def open_restaurant(self):
        print(f"{self.r_name} is officially open!!")


restaurant = Restaurant("Jonny Salsa", "mexican")
restaurant2 = Restaurant("Wheelhouse", "comfort")
restaurant3 = Restaurant("ICC", "summer")

restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
