# 8-3, 8-4
# positional and keyword args, default values
# Use the best function design suited for your function

def make_shirt(message="I <3 Python!", size='large'):
    print(f"Here is your '{message}' shirt, it's a size-{size}!")


# The first call below, 'make_shirt()' does not need an argument to pass, because calling function's
# parameters are all default values.
# If function had normal parameters (no default value), and we tried 'make_shirt()'...
# we would raise an argument error.

# In the second call, 'make_shirt(size='medium')', we provide an explicit argument for 'size',
# therefore, Python will ignore the functions default value.
make_shirt()
make_shirt(size="medium")

# Both of these function calls work exactly the same. (below)
# Because we are using keyword arguments, we can ignore the argument positions.
# We specified each argument's matching parameter already in our call, now Python doesn't need to.

make_shirt(message="UFOs are real!", size="XL")
make_shirt(size="XL", message="UFOs are real!")