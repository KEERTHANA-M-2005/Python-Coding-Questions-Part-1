# Print the numbers in the pattern shown
# for input n. sample output given when
# n = 5
# 5 *****
# 4 ****
# 3 ***
# 2 **
# 1 *

n = 6
for i in range(n-1, 0, -1):
    print(i, end=" ")
    print('*' *i)