import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

a = int(input("Enter 0 for Rock , 1 for Paper and 2 for Scissors :"))
b = random.randint(0,2)
list1 = [rock , paper ,scissors]
print(f"You Picked :\n{list1[a]}")
print(f"Computer Picked :\n{list1[b]}")
if a == b:
    print("Draw!!")
elif a == 0:
    if b == 2:
        print("You Win!!!")
    else:
        print("You Lose!")
elif a==1:
    if b == 0:
        print("You Win!!!")
    else:
        print("You Lose!")
elif a == 2:
    if b== 0:
        print("You Lose!")
    else:
        print("You Win!!!")
