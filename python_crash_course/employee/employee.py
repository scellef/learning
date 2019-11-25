#!/usr/bin/env python3
import locale

class Employee():
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
        locale.setlocale(locale.LC_ALL, '')

    def give_raise(self):
        self.salary += 5000

    def describe_employee(self):
        name = self.first.title() + " " + self.last.title()
        print("Employee:", name)
        print("Salary:", locale.currency(self.salary, grouping=True))

def main():
    new_hire = Employee("john", "belushi", 32000)
    new_hire.describe_employee()
    new_hire.give_raise()
    new_hire.describe_employee()

if __name__ == "__main__":
    main()
