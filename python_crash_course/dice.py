#!/usr/bin/env python3

from random import randint

class Die:
    def __init__(self, sides=''):
        self.sides = sides or 6

    def roll_die(self):
        print(randint(1,self.sides))

def main():
    d6 = Die()
    d6.roll_die()

    d10 = Die(10)
    d10.roll_die()

    d20 = Die(20)
    d20.roll_die()

if __name__ == "__main__":
    main()
    
