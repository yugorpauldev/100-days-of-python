print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
''')

print("Welcome to you adventure game!\n Your mission is to find the treasure")

dire = input("You are in a hall do you want to go to the left or the right\n").lower()

if dire == "left":

    ask1 = input("You found a river filled with dark crocodiles that will likely bite you\nwill you swim or wait\n").lower()
    if ask1 == "wait":

        ask2 = input("You have three doors in front of you choose one between \n Red, Blue and Yellow\n").lower()
        if ask2 == "yellow":
            print("You found the Treasure, Congratulations!")
        elif ask2 == "red":
            print("You were Burned by fire, Game Over!")
        elif ask2 == "blue":
            print("You were eatean by beasts, Game Over!")
        else:
            print("Game Over")


    else:
        print("You got attacked by trout, Game over")
    




else:
    print("You fell into a hole, Game Over!")
