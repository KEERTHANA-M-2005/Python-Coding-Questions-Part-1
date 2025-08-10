# Write a program find the nth digit of a number N
# Input: N = 50023; n = 4
# Output:
# 4th digit is 2

N = int(input("Enter the number N: "))
n = int(input("Enter the digit n to find: "))
def find_nth_digit(N, n):
    digits = str(N)
    if n <= len(digits):
        return int(digits[n - 1])  
    else:
        return None  
result = find_nth_digit(N, n)
if result is not None:
    print(f"{n}th digit is {result}.")
else:
    print(f"{n}th digit does not exist in {N}.")
find_nth_digit(N, n)