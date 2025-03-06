#Password Generator Project
from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# Lists made to save each character selected at random
chosen_letter = []
chosen_symbols = []
chosen_numbers = []

#loop that runs through x times taking into account provided amout
#Then each randomly chosen item is appendeded to the list of letters
for letter in range(nr_letters):
    chosen_letter.append(choice(letters))

for number in range(nr_numbers):
    chosen_numbers.append(choice(numbers))
    
for number in range(nr_symbols):
    chosen_symbols.append(choice(symbols))

combined_pass = chosen_letter + chosen_symbols+ chosen_numbers

#function used to shuffle through a selected list reordering its items
shuffle(combined_pass)

#loop to put all characters of the combined list already shuffled
#To the string variable password
password = ""
for word in combined_pass:
    password += word

print(f"Your password is {password}")
    

    
    




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
