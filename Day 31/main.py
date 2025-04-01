from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}
try:
    df = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    old_df = pd.read_csv("data/french_words.csv")
    words = old_df.to_dict('records')
else:
    words = df.to_dict('records')


def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(canvas_image,image=flashcard)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_text, text= current_card["French"], fill="black")
    flip_timer = window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image,image=flashcard_back)

def remove_item():
    words.remove(current_card)
    new_df = pd.DataFrame(words)
    new_df.to_csv("words_to_learn.csv", index=False)


def combined():
    generate_word()
    remove_item()



    #_________________________________CREATING THE UI ___________________________



window = Tk()
window.config(padx=50,pady=50, bg= BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=600, width=800,bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 300, image=flashcard)
card_title = canvas.create_text(400,150,text="title", font=("Arial", 50, "italic"))
card_text = canvas.create_text(400,275,text="Word", font=("Arial",60,"bold"))
canvas.grid(row=0, column=0, columnspan=2, pady=0)

my_image = PhotoImage(file="images/wrong.png")
my_image2 = PhotoImage(file="images/right.png")
button_wrong = Button(image=my_image, highlightthickness=0)
button_right = Button(image=my_image2, highlightthickness=0,command=combined)

button_right.grid(row=1,column=0)
button_wrong.grid(row=1,column=1)



generate_word()

window.mainloop()