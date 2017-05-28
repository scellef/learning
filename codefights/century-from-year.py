#!/usr/bin/env python3

def centuryFromYear(year):
    if (year % 100) == 0:
        century = int(year / 100)
    else:
        century = int(year / 100) + 1
    return century

def assignSuffix(century):
    if (century[-1] == '1'):
        suffix = 'st'
    elif (century[-1] == '2'):
        suffix = 'nd'
    elif (century[-1] == '3'):
        suffix = 'rd'
    else:
        suffix = 'th'
    return suffix

year = int(input('Enter a year: '))

century = str(centuryFromYear(year))
suffix = assignSuffix(century)

print('Welcome to the', century + suffix, 'century!') 
