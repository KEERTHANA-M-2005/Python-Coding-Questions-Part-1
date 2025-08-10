#  Print the numbers in pattern shown for
# input n. sample output given when n = 5
# 1 1 1 1 1
# 2 3 4 5 6
# 3 6 10 15 21
# 4 10 20 35 56
# 5 15 35 70 126


n = int(input("Enter a number: "))
def print_pattern(n):
    for i in range(1, n + 1):
        num = 0
        for j in range(1, n + 1):
            if i == 1:
                num = 1
            else:
                if j == 1:
                    num = i
                else:
                    num += (i - 1) * (j - 1)
            print(num, end=' ')
        print()

print_pattern(n)
