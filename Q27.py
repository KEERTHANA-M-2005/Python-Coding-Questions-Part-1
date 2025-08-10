# Print digits in a given integer as shown in the sample. The length of the number does not exceed 10 digits.
# Input: 124475577
# Output:
# first digit : 1
# second digit : 2
# third digit : 4
# fourth digit : 4
# and so on

n = int(input("Enter an integer: "))
def print_digits(n):
    digits = str(n)
    for i, digit in enumerate(digits):
        print(f"{i + 1} digit: {digit}")
print_digits(n)


# enumerate(): is used in python to iterate over a sequence (like a list or string) to keep track of both index and value.