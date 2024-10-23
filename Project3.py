import random  # Importing the random module to generate random numbers

def number_guessing_game():
    # Ask the user if they want to play the game and convert the input to lowercase
    play_game = input("Do you want to play the number guessing game? (yes/no): ").lower()
    
    # Check if the user said "yes"
    if play_game == "yes":
        # Generate a random number between 1 and 10
        random_number = random.randint(1, 10)
        
        # Ask the user to guess a number between 1 and 10, and convert it to an integer
        guess = int(input("Guess a number between 1 and 10: "))
        
        # Check if the guessed number matches the random number
        if guess == random_number:
            # If the guess is correct, print a congratulatory message
            print("Congrats! You've guessed the number!")
        else:
            # If the guess is incorrect, show the correct number and prompt them to try again
            print(f"Try Again. The correct number was {random_number}.")
    else:
        # If the user said "no," print a message indicating they chose not to play
        print("Maybe Next Time.")

# Call the function to start the game
number_guessing_game()
