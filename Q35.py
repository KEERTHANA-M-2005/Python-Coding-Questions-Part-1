# Print a 4-digit number in words form. 
# Input: 2345
# Output: two thousand three hundred forty five 

n = int(input("Enter a 4-digit integer: "))

def number_to_words(n):
    if n < 1000 or n > 9999:
        return "Input must be a 4-digit number."
    
    ones = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    
    teens = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen"
    }
    
    tens = {
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    }
    
    words = []
    
    # Thousands place
    words.append(ones[n // 1000])
    words.append("thousand")
    
    # Hundreds place
    if (n // 100) % 10 != 0:
        words.append(ones[(n // 100) % 10])
        words.append("hundred")
    
    # Tens and ones
    last_two = n % 100
    if last_two != 0:
        if last_two < 10:
            words.append(ones[last_two])
        elif last_two < 20:
            words.append(teens[last_two])
        else:
            words.append(tens[last_two // 10])
            if last_two % 10 != 0:
                words.append(ones[last_two % 10])
    
    return " ".join([w for w in words if w])  # Remove empty words

print("Number in words:", number_to_words(n))
