#!/bin/python3

import sys

def dict_get_key_from_value(dct, value):
    for key, item in dct.items():
        if item.upper() == value.upper():
            return key
    return None

def all_in(names):
    print(names)
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    

if __name__ == "__main__":
    if len(sys.argv) == 2:
        all_in(sys.argv[1].split(','))