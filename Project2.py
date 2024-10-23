import random

# This function generates 6 lottery numbers:
# - The first 5 numbers are randomly selected from a range of 1 to 69
# - The last number is randomly selected from a range of 1 to 26
# It then displays the numbers with specific spacing and provides a farewell message.

def lottery_program():
    # Greeting
    print("Welcome to the Lottery Number Generator Program!")
    print("Let's generate your lucky numbers...\n")

    # Generate the first 5 numbers between 1 and 69
    numbers = [random.randint(1, 69) for _ in range(5)]
    
    # Generate the last number between 1 and 26
    last_number = random.randint(1, 26)
    
    # Format the output with spaces (3 spaces between the 5th and 6th number)
    formatted_numbers = f"{numbers[0]} {numbers[1]} {numbers[2]} {numbers[3]} {numbers[4]}   {last_number}"
    
    # Display the generated numbers
    print("Your lottery numbers are:")
    print(formatted_numbers)
    
    # Farewell message
    print("\nGood luck! Thanks for using the program!")

# Call the function
lottery_program()
