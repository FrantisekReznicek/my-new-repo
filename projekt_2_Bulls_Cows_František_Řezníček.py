"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: František Řezníček
email: reznicek.frantisek@gmail.com
discord: frantisekkosmo
"""

import random
# function to generate secret four ditgit number
def generate_secret_number():
    """Generates a secret 4-digit number with unique digits."""
    digits = list(range(10))  # list of digits 0-9
    random.shuffle(digits)   # shuffle the digits
    if digits[0] == 0:
        digits[0], digits[1] = digits[1], digits[0]  # ensure the first digit is not 0
    secret_number = ''.join(map(str, digits[:4]))  # take first 4 digits as the secret number
    return secret_number

# function to print welcome message according to Engeto academy task
def welcome_message():
    """Displays the welcome message and returns the secret number."""
    secret_number = generate_secret_number()
    print("Hi there!")
    print("-----------------------------------------------")
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-----------------------------------------------")
    print("Enter a number:")
    print("-----------------------------------------------")
    return secret_number

# function to check if the user guess is four digit number which is not starting by 0
def is_valid_guess(guess):
    """Checks if the user's guess is valid."""
    if len(guess) != 4:
        return False, "Your guess must be exactly 4 digits."
    if not guess.isdigit():
        return False, "Your guess must only contain digits."
    if len(set(guess)) < 4:
        return False, "Your guess must have all unique digits."
    if guess[0] == '0':
        return False, "Your guess must not start with 0."
    return True, None

# function to evaluate if the guessed numbers has bulls (right number on the right spot) and cows (right number on the wrong spot) in comparison to secret number
def evaluate_guess(secret, guess):
    """Evaluates the user's guess against the secret number."""
    bulls = 0
    cows = 0
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def play_game():
    """Main game loop, which calls previously defined functions welcome_message, is_valid_guess and evaluate_guess."""
    secret_number = welcome_message()
    guesses = 0
    
    while True:
        user_input = input(">>> ")
        
        valid, error_msg = is_valid_guess(user_input)
        if not valid:
            print(error_msg)
            continue
        
        bulls, cows = evaluate_guess(secret_number, user_input)
        guesses += 1
        
        if bulls == 4:
            print(f"{bulls} bulls, {cows} cow{'s' if cows != 1 else ''}")
            print(f"Correct, you've guessed the right number in {guesses} {'guesses' if guesses != 1 else 'guess'}!")
            print("That's amazing!")
            break
        else:
            print(f"{bulls} bull{'s' if bulls != 1 else ''}, {cows} cow{'s' if cows != 1 else ''}")

if __name__ == "__main__":
    play_game()


