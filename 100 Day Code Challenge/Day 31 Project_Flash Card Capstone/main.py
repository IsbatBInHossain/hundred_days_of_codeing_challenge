from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TITLE = 'French'
WORD = 'English'
FILEPATH = "./data/french_words.csv"
TIME = 3
index = 0
timer = 0
# .........................Data Processing.................... #
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
    word_list = data.to_dict(orient='records')
else:
    word_list = data.to_dict(orient='records')


def delete_card():
    del word_list[index]
    df = pandas.DataFrame(word_list)
    df.to_csv("./data/words_to_learn.csv", index=False)
    random_word_selector()


def random_word_selector():
    global index, timer
    try:
        window.after_cancel(timer)
    except ValueError:
        pass
    word = random.choice(word_list)
    index = word_list.index(word)
    first_word = word_list[index][TITLE]
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(word_label, text=first_word, fill='black')
    canvas.itemconfig(lang_label, text=TITLE, fill='black')
    timer = window.after(1000*TIME, card_flip)


def card_flip():
    global index, timer
    second_word = word_list[index][WORD]
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(word_label, text=second_word, fill="#ffffff")
    canvas.itemconfig(lang_label, text=WORD, fill="#ffffff")


# .........................UI Setup.................... #
window = Tk()
window.title("Flasy")
window.geometry('900x700')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")

canvas = Canvas(height=530, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 265, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)
lang_label = canvas.create_text(400, 150, text=TITLE, font=('Ariel', 40, 'italic'))
word_label = canvas.create_text(400, 263, text=word_list[index][TITLE], font=('Ariel', 60, 'bold'))

right_button = Button(image=right, highlightthickness=0, borderwidth=0, command=delete_card)
right_button.grid(row=1, column=0)
wrong_button = Button(image=wrong, highlightthickness=0, borderwidth=0, command=random_word_selector)
wrong_button.grid(row=1, column=1)
random_word_selector()

window.mainloop()
