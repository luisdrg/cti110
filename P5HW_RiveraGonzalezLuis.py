# Luis Rivera Gonzalez
# 4/18/2025
# P5HW1
# Trivia game

import urllib.request # to rquest data from url
import json # to turn response into a Python dict
import html  # to clean up string
import random # to shuffle
import os # To clear screen

def fetch_trivia_questions():
    # Getting data from API
    url = "https://opentdb.com/api.php?amount=10&category=21"
    response = urllib.request.urlopen(url)
    data = json.load(response)

    # Store all question data as dictionaries in a list
    questions = []

    for i in range(10):
        question_number = i + 1
        question_text = html.unescape(data['results'][i]['question'])
        correct_answer = html.unescape(data['results'][i]['correct_answer'])
        incorrect_answers = [html.unescape(ans) for ans in data['results'][i]['incorrect_answers']]

        # Combine and shuffle choices
        all_choices = incorrect_answers + [correct_answer]
        random.shuffle(all_choices)

       # Create question dictionary
        questions.append({
            "number": question_number,
            "text": question_text,
            "choices": all_choices,
            "correct_answer": correct_answer
        })

    return questions

def createPlayer():
    player_name = ""
    while(player_name == ""):
        player_name = input("Enter name: ")
        
    player = { "name" : player_name, "score" : 0, "correct_questions" : [] }
    return player
   
def ask_question(player, question):
    os.system('clear')
    print(f"Player: {player['name']} \t\tScore: {player['score']} out of 10")
    print(f"============================================ Question {question['number']} ============================================")
    print(f"{question['text']}")
    answer = 0
    if len(question['choices']) == 2:
        print("1) True\n2) False")
        while True:
            answer = int(input("Enter your answer (1 or 2): "))
            if answer in [1, 2]:
                # switch case in python
                match(answer):
                    case 1:
                        selected_choice = "True"
                    case 2:
                        selected_choice = "False"

                break
            print("Invalid input. Try again.")
    else:
        for i in range(len(question['choices'])):
            print(f"{i+1}) {question['choices'][i]}")
        while True:
            answer = int(input("Enter your answer (1-4): "))
            if answer in [1, 2, 3, 4]:
                selected_choice = question['choices'][answer - 1]
                break
            print("Invalid input. Try again.")

    if selected_choice == question['correct_answer']:
        print("✅Correct!")
        player['score'] += 1
        player['correct_questions'].append(question['number'])
    else:
        print(f"❌ Wrong! The correct answer was: {question['correct_answer']}")

    input("\nPress Enter to continue...")

def show_game_over(player, questions):
    os.system('clear')
    print("🎉 GAME OVER 🎉")
    print(f"Thanks for playing, {player['name']}!")
    print("=====================================================")
    print(f"Final Score: {player['score']} out of {len(questions)}")

    if player['score'] == len(questions):
        print("🏆 Perfect score! You're a trivia master!")
    elif player['score'] >= len(questions) * 0.7:
        print("🔥 Great job! You really know your stuff!")
    elif player['score'] >= len(questions) * 0.4:
        print("👍 Not bad! A bit more practice and you'll ace it.")
    else:
        print("😅 Tough game, huh? Try again and beat your score!")

    print("\n✅ Correctly Answered Questions:")
    for correct in player['correct_questions']:
        q = questions[correct - 1]
        print(f"\nQuestion {q['number']}) {q['text']}")
        if len(q['choices']) == 2:
            print("1) True\n2) False")
        else:
            for i in range(len(q['choices'])):
                print(f"{i+1}) {q['choices'][i]}")
        print(f"Correct Answer: {q['correct_answer']}")
    print("=====================================================")


def main(): 
    player = createPlayer()
    questions = fetch_trivia_questions()
    for question in questions:
        ask_question(player, question)
    show_game_over(player, questions)

# call the mains
if __name__ == "__main__":
    main()