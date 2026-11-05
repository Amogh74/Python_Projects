from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
Q_Bank = []
for question in question_data:
    question_text = question["text"]
    question_ans = question["answer"]
    new_question = Question(question_text,question_ans)
    Q_Bank.append(new_question)

quiz = QuizBrain(Q_Bank)
while QuizBrain.Still_Has_Q(quiz):
    quiz.next_Q()
    print("\n")

print(f"You Have Completed The Quiz!!\nFinal Score :{quiz.score} Correct Out Of {len(quiz.q_list)}")