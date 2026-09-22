import random
from game_data import data
from art import logo , vs


'''TO Do1 :- print logo and print compare A 
    To do2 :- print Vs logo and type Against B
    TO do 3 : - print Who has more followers if right ans then B becomes A and B is a new value 
     and score goes up by1
    TO do 4 :- if wrong ans then game ends and your score is printed '''
def Pick_Random_B(A):#this is because there is case where A == B
    while True:
        B = random.randint(0, 49)
        if B != A:
            return B


A = random.randint(0,49)
B = Pick_Random_B(A)
def Make_guess(points):
    print(logo)
    if points > 0 :
        print(f"You are Correct!! , Your Points are {points}")
    print(f"\nCompare A:{data[A]['name']} , {data[A]['description']} , {data[A]['country']}")
    print(vs)
    print(f"Against B: {data[B]['name']} , {data[B]['description']} ,{data[B]['country']}")
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    print(20*"\n")
    return guess


def Max(A,B):
    if(data[A]['follower_count']> data[B]['follower_count']):
        return "a"
    else:
        return "b"


guess_wrong = False
points = 0
guess = Make_guess(points)

while not guess_wrong:
    correct_ans = Max(A,B)
    if(correct_ans == guess):
        points += 1
        A = B
        B = Pick_Random_B(A)
        guess = Make_guess(points)
    else:
        print(f"Sorry ,That's Wong .\nFinal Score is {points}")
        guess_wrong = True
