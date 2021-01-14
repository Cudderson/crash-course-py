# 10-* simple json example

import json


def retrieve_data():
    print("Let's retrieve your json data...")

    with open(my_file, "r") as f:
        info = json.load(f)
    return info

my_file = "test_info.json"

info = retrieve_data()
print(info)
