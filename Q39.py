# Print a full square pattern of '*' for a given size n
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *

n = 4
def print_full_square(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
        
print_full_square(n)