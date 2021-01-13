# 9-3, describing a person using Class
# 9-7 9-8, creating subclass 'Admin' for class 'User', and class 'Privileges'

import admin_mods as am

# instances of User class
user1 = am.User("John", "Williams", 29, "blue")
user2 = am.User("Henry", "Bittersweet", 44, "brown")
user3 = am.User("Cody", "Wells", 26, "red")

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
print(f"Login attempts for {user3.first_name} is now {user3.login_attempts}\n")

# create instance of 'Admin' child class,
main_admin = am.Admin("Viktor", "Krum", 35, "brown")
main_admin.privileges.show_privileges()

# appending string to instance attribute list 'privileges_list' in class 'Privileges' for 'main_admin'
main_admin.privileges.privileges_list.append("be the boss")
main_admin.privileges.show_privileges()

new_admin = am.Admin("Cody", "Wells", 26, "brown")
new_admin.privileges.show_privileges()
new_admin.greet_user()
