# 9-14
# using random module, create a winning lottery ticket, just for fun

import random

# Possible numbers in a lottery ticket
lottery_values = [i for i in range(1, 10)]

winning_ticket = ""
my_ticket = ""

# generate lottery tickets
while len(winning_ticket) < 4:
    winning_ticket += str(random.choice(lottery_values))
    my_ticket += str(random.choice(lottery_values))

print(f"Winning ticket:\n"
      f"\t- {winning_ticket}\n")
print(f"Your ticket:\n"
      f"\t- {my_ticket}")

if my_ticket == winning_ticket:
    print("You won the lottery!!")
else:
    print("Not this time..")

# Drawing tickets until the ticket matches the winning ticket
print("Let's see how many tickets you would need to draw before you won..\n")

i = 1
while my_ticket != winning_ticket:
    my_ticket = ""
    while len(my_ticket) < 4:
        my_ticket += str(random.choice(lottery_values))
    i += 1

print(f"It took {i} ticket pulls before your ticket matched the winning ticket, '{winning_ticket}'.")
print(f"My ticket = {my_ticket}")
