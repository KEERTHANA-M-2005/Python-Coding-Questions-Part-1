# For input of integer n, print a
# rhombus shaped pattern using '*',
# example shown for n = 4
#     *
#    * *
#   * * *
#  * * * *
#   * * *
#    * *
#     *

n = 4 

# Top half
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

# Bottom half
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "* " * i)

