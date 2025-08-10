#  For input of odd integer n, print a half-rhombus shaped pattern using
# '*', example shown for n = 5
# * * * * *
#  * * * *
#   * * *
#    * *   
#     *   


n = 5
for i in range(n):
    print(' ' * i + '* ' * (n - i))
    