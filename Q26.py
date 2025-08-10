# Find a given digit n in a given integer m
# Input: n = 4, m = 124475577
# Output: 4

n = int(input("Enter the digit to find: "))
m = int(input("Enter the digit: "))
def find_digit(n, m):
    m_str = str(m)
    if str(n) in m_str:
        return n
    else:
        return "Digit not found"
result = find_digit(n, m)
print(result)