# Print an inverted triangle of numbers
# for input n. sample output given when
# n = 6
# 01 02 03 04 05 06
# 07 08 09 10 11
# 12 13 14 15
# 16 17 18
# 19 20 
# 21

n= 6
for i in range(1, n+1):
    for j in range(1, n-i+2):
        print(f"{(i*(i-1))//2 + j:02d}", end=' ')
    print()