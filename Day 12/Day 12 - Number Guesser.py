import random


def easy():
    chances = 10

    estado = True

    while estado:
            print(f"You have {chances} attempts remaining to guess the number.")
            
            choice = int(input("Make a guess:\n"))


            if choice == random_number:
                print(f"You guessed it right the number is {choice}")
                estado = False
                
            elif choice < random_number:
                print("The number you chose is too low\n Guess Again.")

            elif choice > random_number:
                print("The number you chose is too high\n Guess Again")

            if choice < random_number or choice > random_number:
                      chances = chances - 1
            if chances == 0:
                print("You have lost!")
                estado = False

def hard():    
    chances = 5

    estado = True
    while estado:
            print(f"You have {chances} attempts remaining to guess the number.")
            
            choice = int(input("Make a guess:\n"))

            if choice == random_number:
                print(f"You guessed it right the number is {choice}.")
                estado = False
                
            elif choice < random_number:
                print("The number you chose is too low\n Guess Again")

            elif choice > random_number:
                print("The number you chose is too high\n Guess Again")

            if choice < random_number or choice > random_number:
                      chances = chances - 1
            if chances == 0:
                print("You have lost! No more Chances left!")
                estado = False


print("I'm thinking of a number between 1 and 100.")
random_number = random.randrange(1,100)
choice = input("Choose a difficulty. Type 'easy' or 'hard': \n")

if choice == "easy":
    easy()
elif choice == "hard":
    hard()

