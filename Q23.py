# Print the division of two integers with numerator n and denominator m without
# using the division (/) operator and numerator is a multiple of denominator

n = int(input("Enter numerator: "))
m = int(input("Enter denominator: "))

if m == 0:
    print("Division by zero is not allowed.")
else:
    quotient = 0
    temp = n

    while temp >= m:
        temp -= m
        quotient += 1

    print(f"{n} divided by {m} = {quotient}")
