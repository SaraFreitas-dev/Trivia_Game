from src.data import question_data
import random 

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def random_question():
        question = random.choice(question_data)
        return question["text"], question["answer"]          
    


