FGHimport random

# Function to play the number guessing game
def number_guessing_game():
    # Step 1: Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Try to guess it!")

    # Step 2: Start a loop for the player to guess the number
    while True:
        # Step 3: Get user input
        user_guess = input("Enter your guess: ")

        # Validate the input
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1
        
        # Step 4: Compare the guess to the secret number
        if user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly in {attempts} attempts.")
            break

# Start the game
number_guessing_game()
