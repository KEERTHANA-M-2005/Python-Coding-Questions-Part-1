# Write a program to add all even digits and multiply all odd digits of
# a given number n
# Input: 1235
# Output:
# Sum of odd digits: 4
# Sum of even digits: 7

n = int(input("Enter an integer: "))
def add_even_multiply_odd(n):
    even_sum = 0
    odd_product = 1
    has_odd = False  # To check if there are any odd digits

    digits = str(n)

    for digit in digits:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_product *= int(digit)
            has_odd = True

    if not has_odd:  # If there are no odd digits, set product to 0
        odd_product = 0

    print(f"Sum of even digits: {even_sum}")
    print(f"Product of odd digits: {odd_product}")
add_even_multiply_odd(n)
