# 10-* simple json example

import json

print("Let's add some info to the json file.")

info = input("Enter info to add to file: ")

with open("test_info.json", "w") as f:
    json.dump(info, f)



