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

u = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors "))

if u == 0:
    print(rock)
elif u == 1:
    print(paper)
elif u == 2 :
   print(scissors)
else:
    print("You typed an invalid number, you lose!")

if u in range(3):
    print("computer chose")
    l = [rock,paper,scissors]
    c = random.randint(0,2)
    print(l[c])
    if  (c == 1 and u == 0) or (c == 2 and u == 1) or (c ==0 and u == 2):
        print("you lose")
    elif (c == 0 and u == 1) or (c == 1 and u == 2) or (c == 2 and u == 0):
        print("you Win")
    else:
        print("its a draw")
