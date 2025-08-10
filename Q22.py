# Print the product of two integers n and m without using the multiplication
# (*) operator 

# Multiply two integers without using *

m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))

product = 0

negative = False
if m < 0 and n >= 0:
    m = -m
    negative = True
elif n < 0 and m >= 0:
    n = -n
    negative = True
elif m < 0 and n < 0:
    m = -m
    n = -n

# Add m to product n times
for _ in range(n):
    product += m

# Adjust sign if needed
if negative:
    product = -product

print(f"The product of {m} and {n} is {product}")
