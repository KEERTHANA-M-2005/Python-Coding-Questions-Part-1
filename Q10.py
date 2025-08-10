# Print the numbers in the pattern
# shown for input n. sample output
# given when n = 5
# 1 * 5
# 2 * 4
# 3 * 3
# 4 * 2
# 5 * 1  

n = 5
for i in range(1, n+1):
    print(i, '*', n-i+1)