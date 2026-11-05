#TODO : asking the questions
#TODO : checking if the ans was correct
#TODO : checking if we're  at the end of the quiz
class QuizBrain:
    def __init__(self,list):
        self.q_number = 0
        self.q_list = list
        self.score = 0

    def next_Q(self):
        current_q = self.q_list[self.q_number]
        User_Ans = input(f"Q.{self.q_number + 1}) {current_q.Text} . (True/False):").lower()
        self.check_ans(User_Ans , current_q.Answer)
        self.q_number += 1

    def Still_Has_Q(self):
        return self.q_number < len(self.q_list)

    def check_ans(self , User_Ans , correctAns):
        if User_Ans.lower() == correctAns.lower():
            self.score += 1
            print(f"You Got it Right\nYour Score is {self.score}/{self.q_number + 1}")
        else:
            print(f"You Got it Wrong!!\nYour Score is {self.score}/{self.q_number + 1}")

