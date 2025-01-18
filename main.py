import json
import random

def load_json(file_path):
    """Load a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON file {file_path}.")
        return None

def select_questions(questions, level, num_questions=10):
    """Select a random set of questions for the chosen level."""
    level_questions = [q for q in questions if q['level'] == level]
    return random.sample(level_questions, min(num_questions, len(level_questions)))

def get_encouragement_message(messages, level, score):
    """Get the encouragement message based on the level and score."""
    for score_range, message in messages[level].items():
        start, end = map(int, score_range.split('-'))
        if start <= score <= end:
            return message
    return "No message available."

def quiz_game():
    """Main function for the quiz game."""
    # Load questions and messages from JSON files
    questions = load_json('questions.json')
    messages = load_json('messages.json')

    if not questions or not messages:
        print("Error: Missing required files. Ensure 'questions.json' and 'messages.json' exist.")
        return

    # Welcome the player
    print("Welcome to the Quiz Game!")
    print("Choose your level: easy, medium, or hard.\n")

    # Get the level from the user
    level = input("Enter the level you want to play (easy, medium, hard): ").lower()
    if level not in messages:
        print("Invalid level. Exiting the game.")
        return

    # Select 10 random questions for the chosen level
    selected_questions = select_questions(questions, level)
    if not selected_questions:
        print(f"No questions available for level {level}.")
        return

    score = 0  # Initialize score

    # Start the quiz
    for i, question in enumerate(selected_questions):
        print(f"\nQ{i+1}/{len(selected_questions)}: {question['question']}")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")

        try:
            user_choice = int(input("Enter the number of your choice: "))
            if question['options'][user_choice - 1] == question['answer']:
                print("Correct!\n")
                score += 1
            else:
                print(f"Wrong, the correct answer was : {question['answer']}")
        except (ValueError, IndexError):
            print("Invalid choice. Moving to the next question.\n")

    # Display the final score and encouragement message
    encouragement = get_encouragement_message(messages, level, score)
    print(encouragement)
    print(f"Your score is: {score}/{len(selected_questions)}")

if __name__ == "__main__":
    quiz_game()
