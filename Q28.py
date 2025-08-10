# Print frequency of digits in a given integer. The length of the number
# does not exceed 10 digits.
# Input: 124475577
# Output:
# 1 : 1 (first digit)
# 2 : 1 (second digit)
# 4 : 2 (third, fourth digits)
# 5 : 2 (sixth, seventh digits)
# 7 : 3 (fifth, eighth, ninth digits)

n = int(input("Enter an integer: "))
def print_digit_frequency(n):
    digits = str(n)
    frequency = {}
    
    for digit in digits:
        if digit in frequency:
            frequency[digit] += 1
        else:
            frequency[digit] = 1
    
    for digit, count in frequency.items():
        print(f"{digit} : {count} ({' '.join([f'{i + 1} digit' for i, d in enumerate(digits) if d == digit])})")
        
print_digit_frequency(n)
