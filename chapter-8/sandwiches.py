# 8-12
""" Simple example of *args """

def order_sandwich(*toppings):
    print("I am preparing a sandwich with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")
    print("\n")


order_sandwich('tomato')
order_sandwich('cheese', 'onion')
order_sandwich('turkey', 'ranch', 'lettuce', 'oregano', 'garlic powder')
