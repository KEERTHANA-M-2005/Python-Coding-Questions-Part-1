# Print a spiral matrix of numbers for
# input n. sample output given when n =
# 5
# 01 * 02 * 03 * 04 * 05
# 16 * 17 * 18 * 19 * 06
# 15 * 24 * 25 * 20 * 07
# 14 * 23 * 22 * 21 * 08
# 13 * 12 * 11 * 10 * 09

n = 5
matrix = [[0] * n for _ in range(n)]
num = 1
left, right = 0, n - 1
top, bottom = 0, n - 1
while left <= right and top <= bottom:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    if top <= bottom:
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
for row in matrix:
    for value in row:
        print(f"{value:02d}", end=' * ')
    print() 
    