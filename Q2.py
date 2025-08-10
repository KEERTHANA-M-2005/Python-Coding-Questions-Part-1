#Print the numbers in the following pattern for input n. sample output given when n = 5

# 5 4 3 2 1
# 5 * 4 * 3 * 2 * 1

n=5
for i in range(n, 0, -1):
    print(i, end=' ')
print("\n")
    
    
for i in range(n, 1, -1):
    print(i, end=' * ')
print(1)      
