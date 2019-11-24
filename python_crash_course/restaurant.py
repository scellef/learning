#!/usr/bin/env python3

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Name:", self.restaurant_name)
        print("Cuisine:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "is now open for business!")

def main():
    frontier = Restaurant("Frontier Restaurant", "New Mexican")
    frontier.describe_restaurant()
    frontier.open_restaurant()

    pepper_box = Restaurant("Pepper Box Cafe", "New Mexican")
    marukin = Restaurant("Marukin", "Japanese")

    pepper_box.describe_restaurant()
    marukin.describe_restaurant()

if __name__ == "__main__":
    main()

