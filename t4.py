import random
rock =('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

paper =('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

scissors =('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')

game_images = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if user < 0 or user >= 3:
    print("You typed an invalid number, you lose!")
else:
 print(game_images[user])

computer = random.randint(0, 2) 
print(f"computer chose {computer}")
print(game_images[computer])
if user == 0 and computer == 0:
    print("Draw")
elif user == 0 and computer == 1:
    print("You lose")
elif user == 0 and computer == 2:
    print("You win")    
elif user == 1 and computer == 0:
    print("You win")
elif user == 1 and computer == 1:
    print("Draw")
elif user == 1   and computer == 2:
    print("You lose")   
elif user == 2 and computer == 0:
    print("You lose")
elif user == 2 and computer == 1:
    print("You win")
elif user == 2 and computer == 2:
    print("Draw")
else:
    print(" You typed an invalid number, you lose!")