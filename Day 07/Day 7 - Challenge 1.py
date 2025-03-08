import random

#Step 1


word_list = ["ardvark", "baboon", "camel"]

#Randomly choose a word from the list
chosen_word = random.choice(word_list)

#Ask user to guess a particular letter
guess = input("Guess the letter: ").lower()


#Loop Through the length of the word to check all
#repetitions of a character and if they are right
for x in chosen_word:
    
    if guess == chosen_word[x]:
        print("Right")

    else:
        print("Wrong")
    
