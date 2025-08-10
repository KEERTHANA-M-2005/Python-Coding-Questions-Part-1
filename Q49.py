# Write a program that accepts 2 co-ordinates (x, y) and (x’, y’) of a
# rectangle of size n(length) x m(width) and finds the distance between them  

import math
def distance_between_points(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Input coordinates
x1, y1 = map(float, input("Enter the first coordinate (x1, y1): ").split())
x2, y2 = map(float, input("Enter the second coordinate (x2, y2): ").split())
# Calculate distance
distance = distance_between_points(x1, y1, x2, y2)
print(f"The distance between the points ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
