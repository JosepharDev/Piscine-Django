#!/bin/python3

import sys

def dict_get_key_from_value(dct, value):
    for key, item in dct.items():
        if item.upper() == value.upper():
            return key
    return None

def dict_get_value_from_key(dct, key):
    for item, value in dct.items():
        if item.upper() == key.upper():
            return value
    return None

def clean_dict(dct):
    tmp = []
    for item in dct:
        item = item.strip()
        if item == "":
            continue
        tmp.append(item)
    return tmp


def all_in(names):
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
    items = clean_dict(names)
    for item in items:
        key = dict_get_key_from_value(capital_cities, item)
        value = dict_get_value_from_key(states, item)
        if value:
            print(capital_cities.get(value),"is the state of", dict_get_key_from_value(states, value))
        elif key:
            print(capital_cities.get(key), "is the capital of", dict_get_key_from_value(states, key))
        else:
            print(item, "is neither a capital city nor a state")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        all_in(sys.argv[1].split(','))