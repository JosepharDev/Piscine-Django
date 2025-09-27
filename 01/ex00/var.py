#!/bin/python3

def my_var():
   tmp  = 42
   print(f"{tmp} has a type {type(tmp)}")
   tmp = "42"
   print(f"{tmp} has type {type(tmp)}")
   tmp = "quarante-deux"
   print(f"{tmp} has type {type(tmp)}")
   tmp = 42.0
   print(f"{tmp} has type {type(tmp)}")
   tmp = True
   print(f"{tmp} has type {type(tmp)}")
   tmp = [42]
   print(f"{tmp} has type {type(tmp)}")
   tmp = {42:42}
   print(f"{tmp} has type {type(tmp)}")
   tmp = (42,)
   print(f"{tmp} has type {type(tmp)}")
   tmp = set()
   print(f"{tmp} has type {type(tmp)}")


if __name__ == "__main__":
    my_var()