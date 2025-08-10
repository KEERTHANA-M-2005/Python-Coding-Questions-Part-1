# Write a program to accept N numbers and find the largest and smallest of them
# Input: N = 10
# n1 = 100 ; n2 = 202334; n3 = 3; ….
# n10 = 6451
# Output:
# Smallest number is: 3
# Largest number is: 202334

def find_largest_and_smallest(n):
    if n <= 0:
        print("Please enter a positive integer for N.")
        return
    
    numbers = []
    for i in range(n):
        num = int(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    
    smallest = min(numbers)
    largest = max(numbers)
    
    print(f"Smallest number is: {smallest}")
    print(f"Largest number is: {largest}")
n = int(input("Enter the number of integers (N): ")) 
find_largest_and_smallest(n)