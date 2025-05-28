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
print("Welcome to Rock, Paper and Scissors!")
user_input = int(input("Select a choice: 1 for Rock, 2 for Paper, 3 for scissors!"))
computer_input = random.randint(1, 3)
if  user_input >= 4:
    print("Please select numbers between 1 and 3\n")
elif user_input <= 0:
    print("Please select numbers between 1 and 3\n")
else:
    pass

if computer_input == 1:
    if user_input == 1:
        print(f"computer chose: rock{rock}")
        print(f"You chose: rock{rock}")
        print("Its a draw")
    elif user_input == 2:
        print(f"computer chose: rock{rock}")
        print(f"You chose: paper{paper}")
        print("You won")
    elif user_input == 3:
        print(f"computer chose: rock{rock}")
        print(f"You chose: scissors{scissors}")
        print("Computer won")
elif computer_input == 2:
    if user_input == 1:
        print(f"computer chose: paper{paper}")
        print(f"You chose: rock{rock}")
        print("Computer won")
    elif user_input == 2:
        print(f"computer chose: paper{paper}")
        print(f"You chose: paper{paper}")
        print("Its a draw")
    elif user_input == 3:
        print(f"computer chose: paper{paper}")
        print(f"You chose: scissors{scissors}")
        print("You won")
elif computer_input == 3:
    if user_input == 1:
        print(f"computer chose: scissors{scissors}")
        print(f"You chose: rock{rock}")
        print("You won")
    elif user_input == 2:
        print(f"computer chose: scissors{scissors}")
        print(f"You chose: paper{paper}")
        print("Computer won")
    elif user_input == 3:
        print(f"computer chose: scissors{scissors}")
        print(f"You chose: scissors{scissors}")
        print("Its a draw")
