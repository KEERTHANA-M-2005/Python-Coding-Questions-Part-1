# Print a triangle of numbers for input
# n. sample output given when n = 5
# 01
# 02 03
# 04 05 06
# 07 08 09 10
# 11 12 13 14 15


n = 5
for i in range(1, n+1):
    for j in range(1, i+1):
        print(f"{(i*(i-1))//2 +j:02d}", end=' ')
    print()