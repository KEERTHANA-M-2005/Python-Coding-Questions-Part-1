# For input n, print number of ways to form sum using 1s and 2s. Order
# matters.
# Input: 4
# Output: 5
# 1 1 1 1
# 1 1 2
# 1 2 1
# 2 1 1
# 2 2

n = 4

# Count ways (recursion)
def count_ways(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_ways(n - 1) + count_ways(n - 2)

# Generate sequences (backtracking)
def generate_sequences(target, current):
    if sum(current) == target:
        print(" ".join(map(str, current)))
        return
    if sum(current) > target:
        return
    generate_sequences(target, current + [1])
    generate_sequences(target, current + [2])

ways = count_ways(n)
print(f"Number of ways to form sum {n} using 1s and 2s: {ways}")
generate_sequences(n, [])
 
    