# Given an integer, find the longest sequence of increasing digits. Sample
# inputs and outputs given: 
# Input: 9146826182 Output: 1468
# Input: 924689128 Output: 24689 

n = input("Enter an integer: ") 
def longest_increasing_sequence(n):
    max_length = 0
    current_length = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, len(n)):
        if n[i] > n[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
                max_start_index = start_index
            current_length = 1
            start_index = i

    if current_length > max_length:
        max_length = current_length
        max_start_index = start_index

    return n[max_start_index:max_start_index + max_length]
result = longest_increasing_sequence(n)
print(f"The longest increasing sequence in {n} is: {result}")
