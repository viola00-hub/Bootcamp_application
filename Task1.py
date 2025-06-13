# This program convert a list of digits into a single integer 
# For example: [8,3,5,1] becomes 8351

# How this works:
# This is similar to how you would write a number on paper (forming the number from left to right)
# The first digit is the highest place for example hundred, then tens, then ones
# In that way, logic here is that a number such as 8351 is formed from 8000 + 300 + 50 + 1
# So, in this program, we multiply the current digit by 10 (move it to the left) and then add next digit to the right side


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

    # Process/go through each degit in the list from left to right 
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
