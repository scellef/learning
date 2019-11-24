#!/usr/bin/env python3

def main():
    menu = ['tuna', 'ham', 'roast beef', 'turkey', 'caprese', 'pastrami']
    sandwich_orders = []
    finished_sandwiches = []

    print("Here is today's menu:", *menu, sep="\n* ")
    order_sandwich(sandwich_orders)
    make_sandwich(sandwich_orders, finished_sandwiches)
    deliver_sandwich(finished_sandwiches)

def order_sandwich(orders):
    try:
        while True:
            order = input("What kind of sandwiches would you like? (^D to exit) ")
            if str(order):
                orders.append(order)
    except:
        print()
        return orders

def make_sandwich(orders, completed):
    for order in range(len(orders)):
        if orders[-1] == "pastrami":
            print("Sorry!  We're out of pastrami.")
            orders.pop()
        else:
            completed.append(orders.pop())
    return completed

def deliver_sandwich(order):
    print("Your order is ready! Here it is:")
    for sandwich in order:
        print(sandwich.capitalize(), "sandwich")

if __name__ == "__main__" :
    main()
