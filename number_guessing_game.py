import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Set the number of allowed attempts
    attempts_allowed = 10
    attempts = 0
    
    while attempts < attempts_allowed:
        try:
            guess = int(input(f"\nAttempt {attempts + 1} of {attempts_allowed}. Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    if attempts == attempts_allowed and guess != secret_number:
        print(f"\nSorry, you've used all your attempts. The number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
