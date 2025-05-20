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
game = ["rock", "paper", "scissors"]
game_image = [rock,paper,scissors]

print(game)

print("\npress 0 - rock\npress 1 - paper\npress 2 - scissors\n")
computer_In = random.randint(0,2)
user_In = int(input("What is your choice: \n"))

if user_In >=3 or user_In<0:
    print("Invlalid Input")
    
else: 

    if game[computer_In] == game[user_In]:
        print(f"\nYou choose {game[user_In]}:")
        print(game_image[user_In])
        print(f"\nComputer choose {game[computer_In]}:")
        print(game_image[computer_In])
        print("Match draw")

    elif user_In ==0 and computer_In == 2:
        print(f"\nYou choose {game[user_In]}:")
        print(game_image[user_In])
        print(f"\nComputer choose {game[computer_In]}:")
        print(game_image[computer_In])
        print("You Win!")

    elif user_In < computer_In:
        print(f"\nYou choose {game[user_In]}:")
        print(game_image[user_In])
        print(f"\nComputer choose {game[computer_In]}:")
        print(game_image[computer_In])
        print("You Loose!")

    elif user_In> computer_In:
        print(f"\nYou choose {game[user_In]}:")
        print(game_image[user_In])
        print(f"\nComputer choose {game[computer_In]}:")
        print(game_image[computer_In])
        print("You Win!")
