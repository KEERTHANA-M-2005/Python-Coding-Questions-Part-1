# Write a program to find the length of a floating-point number. For eg.,
# 1234.567 should result in length = 4,3


num = input("Enter a floating-point number: ")

if '.' in num:
    integer_part, decimal_part = num.split('.')
    int_len = len(integer_part)
    dec_len = len(decimal_part)
    print(f"Length = {int_len},{dec_len}")
else:
    print("Not a floating-point number!")
