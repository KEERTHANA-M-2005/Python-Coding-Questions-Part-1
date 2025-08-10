#  Print the difference of two integers n and m without using the minus (-)
# operator
m = int(input("Enter first integer :"))
n = int(input("Enter second integer :"))

count = 0
if n < m:
    while n != m:
        n += 1
        count += 1
    print(f"The difference of {m} and {n-count} is {count}")
elif n > m:
    while m != n:
        m += 1
        count += 1
    print(f"The difference of {m} and {n-count} is {count}")
else:
    print(f"The difference of {m} and {n} is 0") 