# Print the numbers in the pattern
# shown for input n. sample output
# given when n = 5
# 1 * 5 * 5 * 25 * 125
# 2 * 4 * 8 * 32 * 256
# 3 * 3 * 9 * 27 * 243
# 4 * 2 * 8 * 16 * 128
# 5 * 1 * 5 * 05 * 025


n = 5
for i in range(1, n+1):
    val = i
    mult = n-i+1
    print(i, '*', mult, end =' ')
    for j in range(1, n+1):
        val *= mult
        print('*', val, end=' ')
    print()