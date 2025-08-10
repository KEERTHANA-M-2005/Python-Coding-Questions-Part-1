# Print the numbers in the pattern
# shown for input n. sample output
# given when n = 5
# 1 (0 stars)
# 2 ** (2 stars)
# 3 ****** (6 stars)
# 4 ************ (12 stars)
# 5 ******************** (20 stars)

n = 5
for i in range(1, n+1):
    print(i, "*" *(i*(i-1)), f" {i*(i-1)} stars")
    