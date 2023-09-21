import random

# Generate a random secret number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the user's guess and the number of attempts
guess = None
attempts = 0

print("Welcome to the Number Guessing Game!")

# Main game loop
while guess != secret_number:
    try:
        # Get the user's guess as input
        guess = int(input("Guess the secret number (between 1 and 100): "))
        
        # Increment the number of attempts
        attempts += 1
        
        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"Correct! You guessed the secret number {secret_number} in {attempts} attempts.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")

# End of the game
print("Thank you for playing!")
