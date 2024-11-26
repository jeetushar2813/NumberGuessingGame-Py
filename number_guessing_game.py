import random
import os
import time

def clear_console():
    # Clear the console based on the OS
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 20
    number_to_guess = random.randint(1, 20)
    attempts = 0
    max_attempts = 10  # Limit number of attempts
    guessed_correctly = False
    
    while not guessed_correctly and attempts < max_attempts:
        # Ask the user for a guess
        guess = input(f"Guess a number between 1 and 20 (Attempt {attempts + 1}/{max_attempts}): ")
        
        # Validate input to ensure it's a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        # Clear the console after each guess
        # time.sleep(1)  # Adding a small delay to let the user see the feedback before clearing
        clear_console()

        # Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            break
        
        if attempts == max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {number_to_guess}.")
            break

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'y':
        number_guessing_game()

if __name__ == "__main__":
    number_guessing_game()
