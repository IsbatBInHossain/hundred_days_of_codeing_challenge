from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
tick_number = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_pomodoro():
    global timer
    global reps
    global tick_number
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    tick_number = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def tick():
    global tick_number
    tick_number += 1
    ticks = "✔" * tick_number
    tick_label.config(text=ticks)


def start_timer():
    global reps
    reps += 1
    work = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    if reps <= 8:
        if reps % 8 == 0:
            timer_label.config(text="Break", fg=RED)
            tick()
            raise_above_all()
            count_down(long_break)
            reset_pomodoro()
        elif reps % 2 == 0:
            tick()
            raise_above_all()
            timer_label.config(text="Break", fg=PINK)
            count_down(short_break)
        else:
            raise_above_all()
            timer_label.config(text="Work", fg=GREEN)
            count_down(work)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(time):
    minutes = math.floor(time/60)
    seconds = time % 60
    count = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=count)
    if time > 0:
        global timer
        timer = window.after(1000, count_down, time-1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
def raise_above_all():
    window.state('zoomed')
    window.state("normal")
    window.attributes('-topmost', True)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=204, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", font=(FONT_NAME, 30, "bold"), fill='white')
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="reset", highlightthickness=0, command=reset_pomodoro)
reset_button.grid(column=2, row=2)

tick_label = Label(text="", fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)


window.mainloop()
