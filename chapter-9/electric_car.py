class Car:
    def __init__(self, make, model, year):
        """initializes attributes of a Car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Print formatted info about instance of Car"""

        full_name = f"{self.make} {self.model} {self.year}"
        return f"{full_name.title()}"

    def read_odometer(self):
        print(f"This car has an odometer reading of {self.odometer_reading}")

    def update_odometer(self, mileage):
        """Sets odometer reading to the passed value"""

        if mileage <= self.odometer_reading:
            print(f"Nice try!! You cannot roll-back an odometer reading.")
        else:
            self.odometer_reading = mileage

    def increment_odometer(self, new_miles):
        """Increments odometer reading by the passed value"""

        if new_miles >= 0:
            self.odometer_reading += new_miles
        else:
            print(f"You cannot subtract from an odometer!!")

    def fill_gas_tank(self):
        print("Gas tank now full!")

class Battery:
    """Simple battery model for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize battery attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Determine max battery range by battery size"""

        if self.battery_size == 75:
            range = 260

        elif self.battery_size == 100:
            range = 315

        if range == 260 or 315:
            print(f"The max range for this car is about {range} miles.")

    def upgrade_battery(self):
        """Upgrade battery_size to 100"""

        if self.battery_size < 100:
            print("Upgrading battery...")
            self.battery_size = 100
        else:
            pass


class ElectricCar(Car):
    """Represents aspects of a car, specifically electric cars"""

    def __init__(self, make, model, year):
        # 'super()' allows for call of parent class methods
        # We call the '__init__' method here
        super().__init__(make, model, year)
        self.battery = Battery()  # ElectricCar attribute 'battery' = an instance of the class 'Battery'

    def fill_gas_tank(self):
        print("Electric cars don't use gasoline!")


# Instance of Car
my_car = Car("Pontiac", "grand prix", 2002)
print(my_car.get_descriptive_name())

# Directly setting odometer_reading
my_car.read_odometer()
my_car.odometer_reading = 55
my_car.read_odometer()

# Using method to set new odometer_reading
my_car.update_odometer(77)
my_car.read_odometer()

# Incrementing odometer
my_car.increment_odometer(50)
my_car.read_odometer()

# Create instance of child class 'ElectricCar' and get its description
print("\nElectric Car:\n")
my_tesla = ElectricCar("Tesla", "model 3", 2018)
print(my_tesla.get_descriptive_name())
print("\n")

# Demonstration of overriding parent class method with identical child class method
my_car.fill_gas_tank()
my_tesla.fill_gas_tank()
print("\n")

# Describe battery (ElectricCar -> Battery -> method in Battery)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
print("\n\n")

# Upgrading ElectricCar instance's battery size from default value '75' -> '100'
electric_car_to_upgrade = ElectricCar("Tesla", "roadster", 2020)

electric_car_to_upgrade.battery.get_range()
electric_car_to_upgrade.battery.upgrade_battery()
electric_car_to_upgrade.battery.get_range()
