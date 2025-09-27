#!/bin/python3
import sys
def capital_city(name):
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
    tmp = states.get(name)
    if not tmp:
        print("Unknown state")
        sys.exit(1)
    print(capital_cities.get(tmp))



if __name__ == "__main__":
    if len(sys.argv) == 2:
        capital_city(sys.argv[1])