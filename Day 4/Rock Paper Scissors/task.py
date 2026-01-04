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

options = [rock, paper, scissors]
player = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors\n"))
print(options[player])


ai = random.randint(0,2)
print(f"Computer chose: ")
print(options[ai])

if player == 0 and ai == 2:
    print("You win!")
elif player >= 3 or player < 0:
    print("You types an invalid number, You lose!")
elif ai == 0 and player == 2:
    print("You lose!")
elif player > ai:
    print("You win!")
elif ai > player:
    print("You lose!")
elif ai == player:
    print("Its a draw!")
