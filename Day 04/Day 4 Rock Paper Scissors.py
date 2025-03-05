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

#Write your code below this line 👇

print("Welcome to ROCK, PAPER, SCISSORS")

options = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_choice = random.randint(0,2)

print(options[choice])

print("Computer chose:")
print(" ")
print(options[computer_choice])


if choice == computer_choice:
    print("It's a draw")   
elif choice == 0 and computer_choice == 1:
    print("You lose, Paper covers the rock!")
elif choice == 0 and computer_choice == 2:
    print("You win, Rock smashes the Scissors!")
elif choice == 1 and computer_choice == 0:
    print("You win, Paper covers the rock")
elif choice == 1 and computer_choice == 2:
    print("You lose, Scissors cut the Paper")
elif choice == 2 and computer_choice == 0:
    print("You lose, Rock smashes the scissors")
elif choice == 2 and computer_choice == 1:
    print("You win, Scissors cut the Paper")



      
