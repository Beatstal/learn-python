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

ARTS = [rock, paper, scissors]
NAMES = ["Rock (0)", "Paper (1)", "Scissors (2)"]

raw = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors:\n").strip()

if not raw.isdigit() or int(raw) not in (0, 1, 2):
    print("Invalid choice. Please run again and enter 0, 1, or 2.")
else:
    user = int(raw)
    bot = random.randint(0, 2)

    print("\nYou chose:", NAMES[user])
    print(ARTS[user])
    print("Computer chose:", NAMES[bot])
    print(ARTS[bot])

    if user == bot:
        print("Result: Draw")
    elif (user - bot) % 3 == 1:
        print("Result: You win!")
    else:
        print("Result: You lose")
