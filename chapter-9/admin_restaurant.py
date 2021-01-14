# 9-12 + personal idea
# Combine module classes from previous lessons
# Admin goes to a restaurant

from restaurant_mod import Restaurant
from admin_mods import Admin

# Instantiating new Admin instance, and Restaurant instance
hungry_admin = Admin("Cody", "Wells", 26, "brown")
hungry_admin.greet_user()
hungry_admin.privileges.show_privileges()

new_restaurant = Restaurant("Jonny Salsa", "mexican")

# Imports work
print(f"\nAdmin {hungry_admin.first_name} {hungry_admin.last_name} is hungry..\n"
      f"He is going to try the new restaurant on the corner, {new_restaurant.r_name}.")
new_restaurant.describe_restaurant()

# Classes Restaurant and Admin meet
print(f"\n{new_restaurant.r_name} loved {hungry_admin.first_name} so much, that they "
      f"would like to give him free food for life!!")

# add 'free food at Jonny Salsa' as a privilege to instance of Admin
hungry_admin.privileges.privileges_list.append("free food at Johnny Salsa")

hungry_admin.privileges.show_privileges()
