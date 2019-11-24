#!/usr/bin/env python3

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Name:", self.restaurant_name)
        print("Cuisine:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "is now open for business!")

    def set_number_served(self, number_of_customers):
        self.number_served = number_of_customers

    def increment_number_served(self, number_of_customers):
        self.number_served += number_of_customers

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["chocolate", "vanilla", "strawberry", "pistachio"]

    def show_flavors(self):
        print(self.flavors)

def main():
    coldstone = IceCreamStand("Coldstone Creamery", "Desert")
    coldstone.describe_restaurant()
    coldstone.show_flavors()

if __name__ == "__main__":
    main()

