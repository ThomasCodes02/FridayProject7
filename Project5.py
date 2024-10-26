# Define functions for each color
def redText(text):
    return f"\033[31m{text}\033[0m"

def blueText(text):
    return f"\033[34m{text}\033[0m"

def greenText(text):
    return f"\033[32m{text}\033[0m"

def yellowText(text):
    return f"\033[33m{text}\033[0m"

def brownText(text):  # Brown can be achieved with a specific yellow code in some terminals
    return f"\033[33;2m{text}\033[0m"

# Main Program Logic

# Display each color function with sample text
print(redText("This is red text"))
print(blueText("This is blue text"))
print(greenText("This is green text"))
print(yellowText("This is yellow text"))
print(brownText("This is brown text"))

# User input for custom text and color choice
color_choice = input("Choose a color (red, blue, green, yellow, brown): ").strip().lower()
text_input = input("Enter the text you want to display: ")

# Dictionary to match color choices with functions
color_functions = {
    "red": redText,
    "blue": blueText,
    "green": greenText,
    "yellow": yellowText,
    "brown": brownText
}

# Display the text in the chosen color if the color is valid
if color_choice in color_functions:
    print(color_functions[color_choice](text_input))
else:
    print("Invalid color choice.")
