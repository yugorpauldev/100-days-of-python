import tkinter

window = tkinter.Tk()
window.title= ("Mile to Km Converter")
window.minsize(width = 200, height = 200)
window.config(padx=50,pady=30)

#Creating all titles
miles_title = tkinter.Label(text="Miles", font=("Arial", 12))
miles_title.grid(column=2, row = 0)


equal_title = tkinter.Label(text="is equal to", font=("Arial",12))
equal_title.grid(column=0, row=1)

value_title = tkinter.Label(text="0", font=("Arial", 12))
value_title.grid(column=1, row = 1)
value_title.config(padx=20)

km_title = tkinter.Label(text="Km", font=("Arial",12))
km_title.grid(column=2,row = 1)



#Entry
milage_entry = tkinter.Entry(width=10)
milage_entry.grid(column=1, row = 0)


#Button
def calculate_clicked():
    #Get the value from the entry multiply and round it to 2 decimal places
    new_value = round(float(milage_entry.get()) * 1.6,2)
    new_value = str(new_value) # convert it back to a string in order to be displayed
    value_title["text"] = new_value

calculate_button = tkinter.Button(text="Calculate", command=calculate_clicked)
calculate_button.grid(column=1, row=2)



window.mainloop()

