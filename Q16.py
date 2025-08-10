# Print a spiral matrix of numbers for
# input n. sample output given when n =
# 5
# 01 * 02 * 03 * 04 * 05
# 06 * 07 * 08 * 09 * 10
# 11 * 12 * 13 * 14 * 15
# 16 * 17 * 18 * 19 * 20
# 21 * 22 * 23 * 24 * 25

m = 5
n = 5
num = 1
for i in range(m):
    for j in range(n):
        print(f"{num:02d}", end=' * ' if j<n-1 else ' ')
        num += 1
    print( )