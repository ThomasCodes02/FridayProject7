# Define the trivia questions and answers
trivia_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote 'Romeo and Juliet'?": "Shakespeare",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for water?": "H2O",
    "In which year did the Titanic sink?": "1912"
}

# Loop through the dictionary and prompt the user for answers
for question, correct_answer in trivia_questions.items():
    # Display the question
    user_answer = input(question + " ")
    
    # Check if the answer is correct and provide feedback
    if user_answer.strip().lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
    
    print()  # Add a newline for spacing
