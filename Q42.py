# Write a program to reverse a number n Input: 1234 Output: 4321
n = int(input("Enter an integer: "))
rev = int(str(n)[::-1])
print(f"{n} will be {rev} after reversing.")
