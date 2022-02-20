import math
'''
Take the input from the user 
Find the distance between two points x,y
using the formula to find the distance math.sqrt((x ** 2) + (y ** 2))
'''

def distance():
    x = int(input("Enter the value of X : "))  # taking the input from the user
    y = int(input("Enter the value of y : "))  # taking the input from the user

    distance = math.sqrt((x ** 2) + (y ** 2))
    print("The distance between", (x, y), "is:", distance)
distance()