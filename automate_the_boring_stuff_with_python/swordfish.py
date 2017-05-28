#!/usr/bin/env python3

while True:
    name = input("And who are you? ")
    if name != 'Sean':
        continue
    password = input("Hello, " + name + ". What is the password? ")
    if password == 'god, sex, or money':
        break
print('Access granted.')
    

