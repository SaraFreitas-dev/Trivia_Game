from src.question_model import Question
from src.ascii import logo
from colorama import init, Fore


# Initialize colorama
init(autoreset=True)

class Quiz_brain:

    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.end_game = False


    def game_intro(self):
        print(logo)   
        start = input("Welcome ! In this Trivia Game you will be given 10 weird questions. \nYour mission is to guess right as many as you can! \nAre you ready to start? Press any key.") 
        print(start)


    def ask_question(self):
        question_text, question_answer = Question.random_question()
        self.total_questions += 1
        
        while True:
            answer = input(f"{Fore.BLUE}Question n.{self.total_questions}: {question_text} Is it 'True' or 'False'? {Fore.RESET}").lower()

            if answer in ["true", "false"]:   
                if answer == question_answer:
                    self.score += 1
                    print(f"Correct ! Your Score is Now: {self.score} Points.")
                else:
                    print(f"Wrong answer ! Your Score keeps being: {self.score} Points.")    
                break
            else:
                print("Invalid Input.")    


    def restart(self):
        while self.end_game:
            repeat_game = input("Would you like to play again? Type 'Yes' or 'No': ").lower()
            if repeat_game == "yes":
                self.reset_quiz()
                self.run_quiz()
                break
            elif repeat_game == "no":
                print("Thanks for playing, see you soon !")
                break
            else:
                print("Invalid input.")


    def reset_quiz(self):
        self.score = 0
        self.total_questions = 0
        self.end_game = False



    def run_quiz(self):
        self.game_intro()
        while self.total_questions < 10:            
            self.ask_question()
        print(f"Quiz finished! Your final score is {self.score}/{self.total_questions}.")
        self.end_game = True
        self.restart()
