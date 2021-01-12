# 9-1, 9-2, 9-4
# 9-6 introducing a child class
# Class practice


class Restaurant:
    """class blueprint for a restaurant"""

    def __init__(self, r_name, cuisine_type): # notice that 'number_served' not needed in declaration (default value)
        self.r_name = r_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes basic info about a restaurant"""
        print(f"This restaurant is called {self.r_name}")
        print(f"{self.r_name} serves {self.cuisine_type} food!")

    def open_restaurant(self):
        """Declares that a restaurant is open"""
        print(f"{self.r_name} is officially open!!")

    def set_number_served(self, number_served):
        """ Modify attribute 'number_served' """
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """Positively increment attribute 'number_served' """
        self.number_served += number_served


class IceCreamStand(Restaurant):
    """subclass represents aspects of Restaurant, specific to an ice cream stand"""
    def __init__(self, r_name, cuisine_type):
        super().__init__(r_name, cuisine_type)
        self.flavors = []

    def flavors_available(self):
        print(f"Here are the ice cream flavors we have available:")
        for flavor in self.flavors:
            print(f"\t - {flavor}")


# instance of Restaurant
restaurant = Restaurant("Jonny Salsa", "mexican")

print(f"{restaurant.r_name} has served {restaurant.number_served} people.\n")

# Directly changing attribute value
restaurant.number_served = 1_000
print(f"{restaurant.r_name} has served {restaurant.number_served} people.\n")

# Setting new attribute value via class method
restaurant.set_number_served(2_000)
print(f"They have now served {restaurant.number_served} people!\n")

# Adding to cumulative attribute value via class method
restaurant.increment_number_served(72)
print(f"After closing today, {restaurant.r_name} has now served {restaurant.number_served} people!!!\n")

# creating instance of subclass 'IceCreamStand'
my_stand = IceCreamStand("Daily Cones", "ice cream")
# defining 'self.flavors' for instance 'my_stand' and calling method
my_stand.flavors = ["chocolate", "vanilla", "strawberry swirl"]
my_stand.flavors_available()
# Calling method from parent class, opens the restaurant
my_stand.open_restaurant()
