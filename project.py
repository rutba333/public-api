import requests
import html
import random

def fetch_questions():
    url = "https://opentdb.com/api.php?amount=5&type=multiple"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["results"]
    else:
        print("Failed to fetch questions")
        return []

def run_quiz():
    questions = fetch_questions()
    score = 0

    for i, q in enumerate(questions, start=1):
        question = html.unescape(q["question"])
        correct = html.unescape(q["correct_answer"])
        incorrect = [html.unescape(ans) for ans in q["incorrect_answers"]]

        options = incorrect + [correct]
        random.shuffle(options)

        print(f"\nQ{i}: {question}")
        for idx, option in enumerate(options, start=1):
            print(f"{idx}. {option}")

        try:
            answer = int(input("Enter option number: "))
            if options[answer - 1] == correct:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! Correct answer: {correct}")
        except:
            print("Invalid input!")

    print("\n🎉 Quiz Finished!")
    print(f"Your Score: {score} / {len(questions)}")

# Run the quiz
run_quiz()
