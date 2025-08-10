#  Write a program to print any alphabet
# using *
# Input: A
# Output:
#      *
#     * *
#    *   *
#   *******
#  *       *

def print_A():
    rows = 5
    for i in range(rows):
        for j in range(rows * 2 - 1):
            if j == rows - i - 1 or j == rows + i - 1:  # sides
                print("*", end="")
            elif i == rows // 2 and j > rows - i - 1 and j < rows + i - 1:  # middle bar
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_A()

