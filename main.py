from question_model import Quiz
from data import question_data
from quiz_brain import Quiz_brain
question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"] 
    new_question=Quiz(question_text,question_answer)
    question_bank.append(new_question)

print(question_bank[0].answer)
quize=Quiz_brain(question_bank)
quize.next_question()
