#quiz.py

QUESTIONS = {
    "Who are the bad guys in Star Wars":"Sith",
    "Who are the good guys in Star Wars":"Jedi",
    "Who is Leia's brother?":"Luke",
    "Who is Bruce Wayne?":"Batman"
}

for question, correct_answer in QUESTIONS.items():
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct Answer!")
    else:
        print("Incorrect Answer!")