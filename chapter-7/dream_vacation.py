# 7-10
# short prompt for user's dream vacation

vacations = {}

print("\n***\nIn this program, you are a poll worker.\n"
      "You are conducting a poll on vacations, trying to find popular destinations/locations.\n***\n\n")

users_to_poll = int(input("How many people will you be polling today? "))

print("\nLet the polling begin!\n")

while users_to_poll > 0:
    name = input("\nHello there, what is your name? ")
    print(f"\nHi, {name.title()}.")

    location = input("\nWe are gathering data on desired vacation destinations! "
                     "If you could go anywhere in the world, right now..."
                     "Where would you go? ")

    print("\n-----Next Person-----\n")

    vacations[name] = location
    users_to_poll -= 1

print("\n\nThe polling results are complete! Here's what we found:\n")

for name, location in vacations.items():
    print(f"\nAs of now, {name.title()}'s dream vacation destination is {location.title()}!")

print("-----End-----")