#!/bin/python3
import sys


def dict_get_key_from_value(dct, value):
    for key, item in dct.items():
        if item == value:
            return key
    return None


def state(name):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    tmp = dict_get_key_from_value(capital_cities, name)
    if not tmp:
        print("Unknown capital city")
        sys.exit(1)
    print(dict_get_key_from_value(states, tmp))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        state(sys.argv[1])
