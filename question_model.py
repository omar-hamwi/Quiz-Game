class  Quiz:
    def __init__(self,q_text,q_answer):
        self.text=q_text
        self.answer=q_answer
    
new_question=Quiz("what your name","my name omar")
print(new_question.answer)
