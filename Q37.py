# Check if a number is a palindrome. without converting to string.
# Input: 121 Output: 121 is a Palindrome
# Input: 122 Output: 121 is not a Palindrome  

n = int(input("Enter an integer: "))
def is_palindrome(n):
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    if original == reversed_num:
        print(f"{original} is a Palindrome")
    else:
        print(f"{original} is not a Palindrome")
is_palindrome(n)