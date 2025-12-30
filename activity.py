import requests
import random 
import html

#education-focused categories (genarel knowlegde science history etc.)
EDUCATION_CATEGORY_ID=9 #genarel knowledge category(most educational)
API_URL = f"https://opentdb.com/api.php?amount=10&category={EDUCATION_CATEGORY_ID}&type=multiple"

def get_education_questions():
    response=requests.get(API_URL)
    if response.status_code==200:
        data=response.json()
        if data["response_code"]==0 and data["results"]:
            return data["results"]
    return None
    
def run_quiz():
    questions=get_education_questions()
    if not questions:
        print("Failed to fetch educational questions")
        return
    score=0
    print("\n Welcome to the Educational quiz!\n")
    for i,q in enumerate(questions,1):
        question=html.unescape(q["question"])
        correct=html.unescape(q["correct_answer"])
        incorrects=[html.unescape(a)for a in q["incorrect_answers"]]

        options=incorrects+[correct]
        random.shuffle(options)

        print(f"Questions {i}:{question}")
        for idx,option in enumerate(options,1):
            print(f"{idx}.{option}")

        #input validation
        while True:
            try:
                choice=int(input("\nYour answer (1-4):"))
                if 1 <=choice <= 4:
                    break
                else:
                    print("Enter a number between 1 and 4.")

            except ValueError:
                print("Invalid input! Enter a number")

        if options[choice-1]==correct:
            print("Correct!\n")
            score +=1

        else:
            print(f"wrong! correct answer:{correct}\n")

    print("Quiz finished!")
    print(f"Final Score:{score}/{len(questions)}")
    print(f"percentage:{(score)/len(questions)*100:.1f}%")

if __name__=="__main__":
    run_quiz()
