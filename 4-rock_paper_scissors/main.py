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
game_list = [rock, paper, scissors]

comp_choice = random.randrange(0,len(game_list))

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_list[user_choice])

print(f"Computer chose:\n{game_list[comp_choice]}")

if user_choice == 0 and comp_choice == 2:
    print("You win!")

elif comp_choice == 0 and comp_choice == 2:
    print("You lose!")

elif user_choice > comp_choice:
    print("You win!")

elif user_choice < comp_choice:
    print("You lose!")

elif user_choice == comp_choice:
    print("Draw!")
    
else:
    print("You have to chose among 0, 1, and 2")





