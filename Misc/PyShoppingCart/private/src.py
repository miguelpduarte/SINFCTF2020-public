#!/usr/bin/python3
import os
import sys
from secret import flag

items = []


def menu():
    print("Welcome to the Shopping Cart manager!")
    print("1. Add items to the shopping cart")
    print("2. View your shopping cart")
    print("3. Check if this app is scamming you!")

    sys.stdout.write("Your choice: ")
    sys.stdout.flush()
    return sys.stdin.readline()


class Item(object):
    def __init__(self, item_type, item_quantity):
        self.quantity = item_quantity
        self.type = item_type

    def print_item(self):
        print(('{0.quantity} x ... ' + self.type).format(self))


def leak_source_code():
    print("This app swears that it's safe and thus leaks its source code for free!\n\n")

    with open(__file__, 'r') as f:
        print(f.read())


def add_item():
    sys.stdout.write("What item do you like to add to the shopping cart? ")
    sys.stdout.flush()
    item_type = sys.stdin.readline().strip()

    sys.stdout.write("How many of those? ")
    sys.stdout.flush()
    item_quantity = sys.stdin.readline().strip()  # Too lazy to sanitize this

    items.append(Item(item_type, item_quantity))

    print("Thank you, your items will be added")


def show_items():
    for item in items:
        item.print_item()


print("""
  __
    \________
 ~   \######/       
  ~   |####/
 ~    |____.
______o____o__________ 
                      \_______
""")

while True:
    choice = menu().strip()

    if(choice == '1'):
        add_item()
    elif(choice == '2'):
        show_items()
    elif(choice == '3'):
        leak_source_code()
    else:
        print("Invalid choice")
