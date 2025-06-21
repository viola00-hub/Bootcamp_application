"""
Number Guessing Game 

This program creates a game where the computer picks a random number (integer) between 1 and 100, 
and the player tries to guess it. If the guess is correct, a congratulatory message is printed; 
otherwise, the program hints whether the guess is higher or lower than the secret number. 
The game continues until the player guesses correctly. 

Each time player give an input, it must be a number between 1 and 100, otherwise program 
prompts for a valid input.  
"""

import random # This allows computer compute a random number

def generate_rand_num():
    """
    Generate a random integer between 1 and 100 (inclusive)
    """
    return random.randint(1,100)


def get_guess_num():
    """
    Prompt the player to give their guess number and check input's validity 
    """
    while True: #Keep asking until we get a valid input (guess)
        guess_num = input("Please enter your guess (1-100): ")

        # Check validity of player's input 
        if guess_num.isdigit(): # Make sure player input a string including all digit(s) (e.g., "12" is fine, "abc" is not)
            guess_num = int(guess_num) # Convert input string to integer so it can be compared with its range (1 to 100)
            # Notify player if their input is out of allow range (e.g., 120)
            if guess_num < 1 or guess_num > 100:
                print("Input must be within 1 to 100")
            else:
                return guess_num # If input is valid, return it
        else:
            print("Input must be a number")


def check_guess_num(guess_num, generated_num):
    """
    Compare guess number and secret number to see whether they match
    If the guess does not match, program notifies the player whether their guess is higher or lower than the secret number 
    """
    if generated_num == guess_num:
        # Player guessed the correct number 
        print ("Congratulation! You got it")
        print (f"The secret number is {generated_num}")
        return True # End game

    # Keep notifying when player's input does not match secret number 
    elif guess_num > generated_num:
         # Input number is too high
        print ("This number is higher than our secret number")
    elif guess_num < generated_num:
         # Input number is too low
        print ("This number is lower than our secret number")     
    return False # Game continues 


def let_play():
    """
    Main function to execute guessing game
    """
    # Generate secret number at the start of the game
    generated_num = generate_rand_num()

    # Keep prompting for a new input and check that input's validity until player guess the the correct secret number
    while True:
        guess_num = get_guess_num()
        if check_guess_num(guess_num, generated_num):
            return # Stop the game when a correct guess is presented


# Call main function to start a game 
let_play()


# ___________TEST CASES___________
# Example how this program works

# Please enter your guess (1-100): abc
# Input must be a number
# Please enter your guess (1-100): 123
# Input must be within 1 to 100
# Please enter your guess (1-100): 
# Input must be a number
# Please enter your guess (1-100): 45
# This number is lower than our secret number
# Please enter your guess (1-100): 67
# This number is lower than our secret number
# Please enter your guess (1-100): 90
# This number is higher than our secret number
# Please enter your guess (1-100): 89
# Congratulation! You got it
# The secret number is 89
