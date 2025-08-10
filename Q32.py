# Print the sums of all even and odd digits of an integer
# Input: 12345678
# Output:
# Sum of all odd digits: 16
# Sum of all even digits: 20

n = 12345678
def sum_even_odd_digits(n):
    odd_sum = 0
    even_sum = 0
    digits = str(n)
    
    for digit in digits:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    
    print(f"Sum of all odd digits: {odd_sum}")
    print(f"Sum of all even digits: {even_sum}")
sum_even_odd_digits(n)