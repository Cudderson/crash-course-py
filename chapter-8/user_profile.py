# 8-13
""" Simple example of **kwargs """

def build_profile(first, last, **user_info):
    user_info['First Name'] = first
    user_info['Last Name'] = last
    return user_info


profile = build_profile('Cody', 'Wells', Age='26', Location='WI', Job='Programmer')

print("Here is your profile:\n")

for key, value in profile.items():
    print(f"{key} - {value}")
