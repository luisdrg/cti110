# Luis Rivera Gonzalez
# 4/18/2025
# P5HW1
# Trivia game

'''
urllib.request: https://docs.python.org/3/howto/urllib2.html
html.unescape: https://stackoverflow.com/questions/2360598/how-do-i-unescape-html-entities-in-a-string-in-python-3-1
json: https://www.w3schools.com/python/python_json.asp
'''
import urllib.request # to rquest data from url
import json # to turn response into a Python dict
import html  # to clean up string
import random # to shuffle
import os # To clear screen

def fetch_trivia_questions(settings):
    # Getting data from API 
    url = f"https://opentdb.com/api.php?amount={settings['amount']}&category={settings['category']+8}"
    response = urllib.request.urlopen(url)
    data = json.load(response)

    questions = []

    for i in range(len(data['results'])):
        question_number = i + 1
        question_text = html.unescape(data['results'][i]['question'])
        correct_answer = html.unescape(data['results'][i]['correct_answer'])
        incorrect_answers = []
        for ans in data['results'][i]['incorrect_answers']:
            incorrect_answers.append(html.unescape(ans))

        all_choices = incorrect_answers + [correct_answer]
        random.shuffle(all_choices)

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
    print(f"Player: {player['name']} \t\tScore: {player['score']} out of {question['number']}")
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

    # Check answer
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

def options():
    amount = 0
    while amount < 1 or amount > 50:
        amount = int(input("Questions amount (max 50): "))

    cat = 0
    print("Select a Category:\n1. General Knowledge\t2. Books\t\t3. Film\t\t\t4. Music\t\t5. Musical & Theatres")
    print("6. Television\t\t7. Video Games\t\t8. Board Games\t\t9. Nature\t\t10. Computers")
    print("11. Math\t\t12. Mythology\t\t13. Sports\t\t14. Geography\t\t15. History")
    print("16. Politics\t\t17. Art\t\t\t18. Celebrities\t\t19. Animals\t\t20. Vehicles")
    while cat < 1 or cat > 20:
        cat = int(input("Enter a number for Category: "))
    return {"amount":amount, "category":cat}

def main(): 
    player = createPlayer()
    settings = options()
    questions = fetch_trivia_questions(settings)
    for question in questions:
        ask_question(player, question)
    show_game_over(player, questions)

# call the mains
if __name__ == "__main__":
    main()