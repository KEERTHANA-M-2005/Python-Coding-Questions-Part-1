# Write a program to search a digit n in a given number N
# Input: N = 500; n = 0
# Output:
# 0 occurs 2 times

N = int(input("Enter the number N: "))
n = int(input("Enter the digit n to search: "))
def search_digit(N, n):
    count = 0
    for digit in str(N):
        if int(digit) == n:
            count += 1
    return count
print(f"{n} occurs {search_digit(N, n)} times in {N}.")
search_digit(N, n)
