# Print a hollow square pattern of '*' for a given size n.
# Input: n = 4
# Output:
# * * * *
# *     *
# *     *
# * * * *

n = 4
def print_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
print_hollow_square(n)
