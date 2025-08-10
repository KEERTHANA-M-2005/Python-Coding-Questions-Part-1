# Print a diamond pattern of numbers
# for a given odd number n
# Input: 5
# Output:
#    1
#  1 2 1
# 1 2 3 2 1
#   1 2 1
#     1

n = 5
def print_diamond_pattern(n):
    if n % 2 == 0:
        print("Please enter an odd number.")
        return
    
    mid = n // 2
    for i in range(n):
        if i <= mid:
            num = i + 1
        else:
            num = n - i
        
        spaces = ' ' * (mid - i) if i <= mid else ' ' * (i - mid)
        numbers = ' '.join(str(j) for j in range(1, num + 1))
        reverse_numbers = ' '.join(str(j) for j in range(num - 1, 0, -1))
        
        print(spaces + numbers + (' ' + reverse_numbers if num > 1 else ''))
print_diamond_pattern(n)