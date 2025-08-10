# Print the numbers in the pattern shown
# for input n. sample output given when
# n = 5
# 1 *
# 2 **
# 3 ***
# 4 ****
# 5 *****

n=6
for i in range(1, n): 
    print(i, end=' ')
    print('*' * i)
    