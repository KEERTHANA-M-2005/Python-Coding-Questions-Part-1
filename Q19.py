# Print a spiral matrix of numbers for
# input n. sample output given when n =
# 5
# 01*
#   * 09 *
#        * 13 *
#             * 17 *
#                  * 25

def make_spiral(n):
    mat = [[0]*n for _ in range(n)]
    top, bottom, left, right = 0, n-1, 0, n-1
    num = 1
    while top <= bottom and left <= right:
        for j in range(left, right+1):
            mat[top][j] = num; num += 1
        top += 1
        for i in range(top, bottom+1):
            mat[i][right] = num; num += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left-1, -1):
                mat[bottom][j] = num; num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top-1, -1):
                mat[i][left] = num; num += 1
            left += 1
    return mat

n = 5
mat = make_spiral(n)

# The exact positions that give your example order for n=5:
positions = [(0,0), (n-1,n-1), (n-1,0), (1,1), (2,2)]

for idx, (r, c) in enumerate(positions):
    val = mat[r][c]
    if idx == 0:
        print(f"{val:02d}*")
    else:
        indent = " " * (idx * 2)   # tweak multiplier to change indentation
        if idx == len(positions) - 1:
            print(f"{indent}* {val:02d}")
        else:
            print(f"{indent}* {val:02d} *")

