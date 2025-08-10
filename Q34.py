# Replace each digit of a number with its word form
# Input: 123
# Output: one two three
n = int(input("Enter an integer: "))
def replace_digits_with_words(n):
    digit_to_word = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    
    words = [digit_to_word[digit] for digit in str(n)]
    return ' '.join(words)
result = replace_digits_with_words(n)
print(f"Number in words: {result}")
