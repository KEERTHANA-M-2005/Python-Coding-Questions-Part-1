# Print the numbers in the pattern shown
# for input n. sample output given when
# n = 5
# 5 ****
# 4 ***
# 3 **
# 2 *
# 1  


n = 5
for i in range(n, 0, -1):
    print(i, '*'*(i-1))