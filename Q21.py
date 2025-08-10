# Print the sum of two integers n and m without using the plus (+) operator 
m = int(input("Enter first integer: "))
n = int(input("Enter second integer: "))
m_original = m
for _ in range(n):
    m += 1
print(f"The sum of {m_original} and {n} is {m}")