# Write a program to add all digits that are even and multiply all odd digits of a given number n
# Input: 12350
# Output:
# Sum of digits that are even: 2
# Product of digits that are odd: 15 

n = int(input("Enter an integer: "))

def add_even_multiply_odd(n):
    even_sum = 0
    odd_product = 1
    has_odd = False

    for digit_char in str(n):
        digit = int(digit_char)
        if digit % 2 == 0:      # even
            even_sum += digit
        else:                   # odd
            odd_product *= digit
            has_odd = True

    # If no odd digits found, product should be 0
    if not has_odd:
        odd_product = 0

    print(f"Sum of digits that are even: {even_sum}")
    print(f"Product of digits that are odd: {odd_product}")

add_even_multiply_odd(n)

