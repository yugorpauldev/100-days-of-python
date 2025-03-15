from game import data as data
import random
from art14 import logo, vs

# Function that selects Random Thing
def select_random(data):
    diferentes = False
    escolha_1 = random.choice(data)
    
    while not diferentes:
        escolha_2 = random.choice(data)

        if escolha_2 == escolha_1:
            escolha_2 = random.choice(data)
        else:
            diferentes = True
    return escolha_1,escolha_2
# Function that compares which has more followers

def compare(esc1,esc2,choice):

    if choice == "a":
        if esc1['follower_count'] > esc2['follower_count']:
            return 1
        else:
            return 0
    elif choice == "b":
        if esc2['follower_count'] > esc1['follower_count']:
            return 1
        else:
            return 0


def game():

    Score = 0
    cont = True
    print("Seja bem Vindo ao Jogo de Comparacao de Seguidores")
    
    while cont:
        print(logo)
        esc1,esc2 = select_random(data)

        print(f"Compare A: {esc1['name']}, {esc1['description']} - {esc1['follower_count']}.")

        print(vs)

        print(f"Against B: {esc2['name']}, {esc2['description']} - {esc2['follower_count']}.")

        choice = input("Who has more followers?: ").lower()

        resultado = compare(esc1,esc2,choice)

        if resultado == 1:
            Score = Score + 1
            print(f"Your score is {Score}")  
        else:
            cont = False
    print(logo)
    print(f"Wrong Answer!\nYou Lost and your Score was {Score}.")


game()





     


