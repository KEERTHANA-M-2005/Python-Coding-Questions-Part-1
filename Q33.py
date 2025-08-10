# Print the sum digits of an integer m for a given condition
# Input: m = 1132548 condition = odd
# Output: 10
# Input: m = 1132548 condition = even
# Output: 14

m = 1132548
condition = 'odd' 
def sum_digits(m, condition):
    total = 0
    digits = str(m)
    
    for digit in digits:
        if condition == 'odd' and int(digit) % 2 != 0:
            total += int(digit)
        elif condition == 'even' and int(digit) % 2 == 0:
            total += int(digit)
    
    return total
result = sum_digits(m, condition)
print(f"Sum of {condition} digits: {result}")
