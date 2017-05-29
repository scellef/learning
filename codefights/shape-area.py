#!/usr/bin/env python3
#
# Recursion limits kick in and prevent this from working :(
# def shapeArea(n):
#     if n == 1:
#         return 1
#     else:
#         return 4 * (n-1) + shapeArea(n-1)

def shapeArea(n):
    area = 1
    for i in range(1,n):
        area += i * 4

    return area

result = shapeArea(int(input("Enter the number of iterations: ")))
print("The polygon has area:", result)
