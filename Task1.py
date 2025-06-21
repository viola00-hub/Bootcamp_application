# This program convert a list of digits into a single integer 
# For example: [8,3,5,1] becomes 8351

# How this works:
# Imagine writing a number step by step: you start with 0, then add each digit one by one.
# For example, 8351 is built by starting with 0, then adding 8 to make 8, shifting left by multiplying it by 10 to add 3 (80 + 3 = 83),
# shifting again to add 5 (830 + 5 = 835), and finally adding 1 (8350 + 1 = 8351).

# Algorithmic approach step by step:
# 1. Start with result of 0 
# 2. Go through each digit in the list, we make space for new digit by moving the current digits to the left
# 3. Add the new digit to the existing number, new digit will stay on right side
# 4. Repeat this process until the last digit in the list is added 


def convert_digits(given_list):
    """
    This function takes a list of digit and turns it into an integer
    """
    # Start with empty result 
    result = 0

    # Process/go through each digit in the list from left to right 
    for digit in given_list:
        # Shift the current result to the left by multiplying it by 10 
        # Then add the new digit to the right
        result = result * 10 + digit 

    return result


# ___________TEST CASES___________
print(convert_digits([8,3,5,1])) # Expect 8351
print(convert_digits([3,8])) # Expect 38
print(convert_digits([0,3,7,1])) # Expect 371
print(convert_digits([])) # Expect 0
