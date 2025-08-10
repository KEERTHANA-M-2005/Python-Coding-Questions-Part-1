# Print a spiral matrix of numbers for
# input n. sample output given when n =
# 5
# 01 * 02 * 03 * 04 * 05
# 10 * 09 * 08 * 07 * 06
# 11 * 12 * 13 * 14 * 15
# 20 * 19 * 18 * 17 * 16
# 21 * 22 * 23 * 24 * 25 

n = 5  # matrix size
num = 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(f"{num:02d}")
        num += 1
    
    # Reverse the row for even-indexed rows (second, fourth...)
    if i % 2 == 1:
        row.reverse()
    
    print(" * ".join(row))
