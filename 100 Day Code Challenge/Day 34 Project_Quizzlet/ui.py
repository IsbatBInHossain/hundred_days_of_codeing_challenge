from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.text = self.canvas.create_text(150, 125, text="Text goes here", font=('Ariel', 20, 'italic'), width=270)
        self.score_label = Label(text="Score: 0", font='Ariel', background=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)
        tick = PhotoImage(file='images/true.png')
        cross = PhotoImage(file='images/false.png')
        self.right_button = Button(image=tick, highlightthickness=0, borderwidth=0, command=self.right_button)
        self.wrong_button = Button(image=cross, highlightthickness=0, borderwidth=0, command=self.wrong_button)
        self.right_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)
        self.show_question()
        self.wait = None
        self.window.mainloop()

    def show_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.text, text=q_text)

    def final_score(self):
        self.canvas.itemconfig(self.text, text=f"Your final score is {self.quiz.score}")
        self.right_button.config(state='disabled')
        self.wrong_button.config(state='disabled')

    def score(self):
        score = self.quiz.score
        self.score_label.config(text=f"Score: {score}")

    def right_button(self):
        user_answer = 'True'
        self.give_feedback(self.quiz.check_answer(user_answer))

    def wrong_button(self):
        user_answer = 'False'
        self.give_feedback(self.quiz.check_answer(user_answer))

    def give_feedback(self, response):
        if response:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.wait = self.window.after(1000, self.refresh)

    def refresh(self):
        self.score()
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.show_question()
        else:
            self.final_score()
