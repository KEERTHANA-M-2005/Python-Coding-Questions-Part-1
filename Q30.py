# For input of odd integer n, print a half-rhombus shaped pattern using
# '*', example shown for n = 7. Also print the mirror image of the output.

# *
# * *
# * * *
# * * * *
# * * *
# * *
# *


n = 7
for i in range(n):
    if i < n // 2 + 1:
        print('* ' * (i + 1))
    else:
        print('* ' * (n - i))  