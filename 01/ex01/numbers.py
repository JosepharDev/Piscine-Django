#!/bin/python3

def number():
    try:
        with open("numbers.txt", "r")  as file:
            print("\n".join(file.read().split(',')))
    except Exception as e:
        print(f"Error {e}")

if __name__ == "__main__":
    number()