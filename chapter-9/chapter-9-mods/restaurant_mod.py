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
