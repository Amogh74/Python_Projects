import random
logo = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
"""
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
Computer_Number = random.randint(1,100)
lives = 10
Difficulty = input("Choose a difficulty. Type 'Easy' or 'Hard':").lower()
if(Difficulty == "hard"):
    lives = 5
counter = lives
while(lives>0):
    print(f"You have {lives} attempts remaining to guess the number.")
    Guess = int(input("Make a Guess:"))
    if(Guess > Computer_Number):
        print("Too High!!")
        lives -= 1
        counter -= 1
    elif(Guess < Computer_Number):
        print("Too Low!!!")
        lives -= 1
        counter -= 1

    else:
        print(f"You got it! The answer was {Computer_Number}")
        lives = 0

if counter == 0:
    print("You Have Lost , Try Again Next Time.")
