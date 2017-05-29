#!/usr/bin/env python3

def adjacentElementsProduct(inputArray):
    largest = inputArray[0] * inputArray[1]
    if len(inputArray) == 2:
        return largest
    else:
        for i in range(2, len(inputArray)):
            next = inputArray[i-1] * inputArray[i]
            pair=(inputArray[i-1],inputArray[i])
            largest = max(largest, next)

        return largest

inputArray=[]
print("Enter an array of numbers (one per line): ")
while True:
        try:
            inputArray.append(int(input()))
        except EOFError:
            break
        

print(adjacentElementsProduct(inputArray))

        

