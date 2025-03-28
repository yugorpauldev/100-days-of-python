import tkinter


window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=400, height=350)



#Label

my_label = tkinter.Label(text="I am a Label",font=("Arial",24))
my_label.grid(column=0, row= 0)

my_label["text"] = "New Text"
my_label.config(text="New Text")

#Button
def button_clicked():
    #print("I got Clicked")
    new_label = input.get()
    my_label["text"] = new_label

button = tkinter.Button(text="CLick me", command=button_clicked)
button.grid(column=1,row = 1)
new_button = tkinter.Button(text="Second one")
new_button.grid(column=2, row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=2)

print(input.get())





window.mainloop()


