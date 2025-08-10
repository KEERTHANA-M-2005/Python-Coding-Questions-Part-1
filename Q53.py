# Write a program to print the area of a geometric shape such as a triangle,
# square, or circle etc. The program should prompt the user to specify the type
# of shape and then request the necessary dimensions to find its area


import math

print("Choose a shape to calculate area:")
print("1. Triangle")
print("2. Square")
print("3. Rectangle")
print("4. Circle")

choice = input("Enter shape name or number: ").strip().lower()

if choice in ("1", "triangle"):
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print(f"Area of Triangle = {area:.2f}")

elif choice in ("2", "square"):
    side = float(input("Enter side length: "))
    area = side ** 2
    print(f"Area of Square = {area:.2f}")

elif choice in ("3", "rectangle"):
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = length * width
    print(f"Area of Rectangle = {area:.2f}")

elif choice in ("4", "circle"):
    radius = float(input("Enter radius: "))
    area = math.pi * radius ** 2
    print(f"Area of Circle = {area:.2f}")

else:
    print("Invalid shape selected!")
