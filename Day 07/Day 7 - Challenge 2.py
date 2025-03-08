import random

#Step 1


word_list = ["ardvark", "baboon", "camel", "dog"]

#Randomly choose a word from the list
chosen_word = random.choice(word_list)

print(f"The chosen word was {chosen_word}")

#Ask user to guess a particular letter
guess = input("Guess the letter: ").lower()

#Create list display
display = []
for x in chosen_word:

    display.append("_")
    

#Loop Through the length of the word to check all
#repetitions of a character and if they are right
for index in range(0, len(chosen_word)):

    if guess == chosen_word[index]:
        display[index] = guess


print(display)
        
    
