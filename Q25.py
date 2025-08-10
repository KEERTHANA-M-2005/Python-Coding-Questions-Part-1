#  Given an integer, find the longest sequence of increasing digits with incremental of 1. Sample inputs and
# outputs given
#  Input: 9146826182 Output: None
#  Input: 9145682618 Output: 456

n = input("Enter an integer: ")
def longest_increasing_sequence(n):
    max_length = 0
    current_length = 1
    start_index = 0
    max_start_index = 0

    for i in range(1, len(n)):
        if int(n[i]) == int(n[i - 1]) + 1:
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

    return n[max_start_index:max_start_index + max_length] if max_length > 1 else None
result = longest_increasing_sequence(n)
if result:
    print(f"The longest increasing sequence in {n} is: {result}")
else:
    print(f"There is no increasing sequence in {n} with incremental of 1.")