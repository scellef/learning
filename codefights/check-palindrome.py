#!/usr/bin/env python3

def checkPalindrome(inputString):
    for i in range(1, int(len(inputString)/2)+1):
        print(inputString[i-1], ':', inputString[-i])
        if inputString[i-1] != inputString[-i]:
            return False
    return True
        
inputString = input("Enter a string:")
checkPalindrome(inputString)
