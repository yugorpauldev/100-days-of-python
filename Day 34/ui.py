from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.score = quiz_brain.score

        self.score_label = Label(text=f"Score:{self.score}",font=("arial",10),bg=THEME_COLOR,fg="white", anchor="e")
        self.score_label.grid(row=0,column=1,padx=20,pady=20)

        self.canvas = Canvas(width=300, height=265, bg="white", highlightthickness=0)
        #self.background_img = PhotoImage(file="images/Background.png")
        #self.canvas.create_image(148,125,image=self.background_img)
        self.question_text =  self.canvas.create_text(148,125,
                                                      text="Testing the grounds",
                                                      font=("arial",20, "italic"),
                                                      width= 280 )
        self.canvas.grid(row=1,column=0, columnspan=2,pady=20)

        self.true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=self.true_img,highlightthickness=0, command = self.answer_right)
        self.true_btn.grid(row=2,column=0,padx=20,pady=20)

        self.false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(image=self.false_img,highlightthickness=0, command= self.answer_wrong)
        self.false_btn.grid(row=2,column=1,padx=20,pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)

    def answer_right(self):
        answer = "True"
        is_right = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score:{self.quiz.score}")
        self.give_feedback(is_right)


    def answer_wrong(self):
        answer = "False"
        is_right = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score:{self.quiz.score}")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.reset_background)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.reset_background)

    def reset_background(self):
        self.canvas.config(bg="white")
        self.get_next_question()