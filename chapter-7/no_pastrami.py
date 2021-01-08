# exercises 7-8, 7-9git
import time

sandwich_orders = ['cheeseburger',
                   'chicken parm',
                   'pastrami',
                   'grilled panini',
                   'pastrami',
                   'pastrami',
                   'turkey avocado on wheat']

finished_sandwiches = []
pastrami_lost = 0
customer_id = 1

print("Bad news, customers. We have run out of pastrami. All pastrami sandwich orders will be cancelled.")
time.sleep(3)

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    pastrami_lost += 1

print(f"Sorry to the {pastrami_lost} of you who did not receive your pastrami sandwiches,\n"
      f"we will be sending a free sandwich to all {pastrami_lost} of you in the mail.\n")

while sandwich_orders:
    time.sleep(2)
    current_sand = sandwich_orders.pop(0)
    print(f"Table #{customer_id}, I am preparing your {current_sand} as we speak!!")
    finished_sandwiches.append(current_sand)
    customer_id += 1
customer_id = 1
print("\n")

for sandwich in finished_sandwiches:
    time.sleep(2)
    print(f"Order up!!! Table #{customer_id}, your {sandwich} is done!")
    customer_id += 1

time.sleep(1)
print("\nEnjoy!")