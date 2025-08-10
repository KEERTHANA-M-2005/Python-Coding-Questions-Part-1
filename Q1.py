#Print the numbers in the pattern shown for input n. Sample output given when n=5 
# 1 2 3 4 5
# 1 * 2 * 3 * 4 * 5

n=5
for i in range(1,6):
    print(i, end=' ')
print("\n")
    
for i in range(1, n+1):
    print(i, end=' ')
    if i != n:
        print('*', end=' ')
    
