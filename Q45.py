# Write a program to display multiplication table for a given
# number n upto the multiplier m
# Input: n = 10 m = 20
# Output:
# 10 x 1 = 10
# 10 x 2 = 20
# ..
# 10 x 20 = 200 

n = int(input("Enter the number for which you want the multiplication table: "))
m = int(input("Enter the multiplier limit: "))
def multiplication_table(n, m):
    for i in range(1, m + 1):
        print(f"{n} x {i} = {n * i}")
multiplication_table(n, m)