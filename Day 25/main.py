import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

#importing data and converting states to a list
data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()

#Getting the answer of the state and capitalizing it

guessed_states = []

while len(guessed_states) < 50:
    answer_capitalized = screen.textinput(title="Guess the state", prompt="what's another state's name?").title()

    if answer_capitalized in all_states:
        guessed_states.append(answer_capitalized)
        show_state = turtle.Turtle()
        show_state.hideturtle()
        show_state.penup()

        state = data[data.state == answer_capitalized]
        state_x_coord = int(state.x)
        state_y_coord = int(state.y)
        show_state.goto(state_x_coord, state_y_coord)
        show_state.write(answer_capitalized)


# def get_mouse_click_cor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_cor)

turtle.mainloop()



#screen.exitonclick()