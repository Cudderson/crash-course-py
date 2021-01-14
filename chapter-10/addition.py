# 10-6
# basic try/except block example


def addition():
    try:
        first = int(input("First number: "))
        second = int(input("Second number: "))
        third = first + second
    except ValueError:
        print("You must input numbers only.")
        addition()
    else:
        print(f"{first} + {second} is {third}!")


print("Let's add 2 numbers together!")
addition()
