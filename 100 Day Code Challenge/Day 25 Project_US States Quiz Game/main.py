from turtle import Turtle, Screen
import pandas

FONT = ('Ariel', 8, 'normal')
states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state.to_list()
turt = Turtle()
turt.penup()
turt.hideturtle()

screen = Screen()
screen.bgpic("blank_states_img.gif")
screen.title("U.S States Game")
correct_guess = 0
correct_guess_list = []
while correct_guess < 50:
    guess = screen.textinput(title=f"{correct_guess}/50 states guessed", prompt="What's another state name?").title()
    if guess in state_names:
        guessed_state = states_data[states_data.state == guess]
        turt.goto(x=int(guessed_state.x), y=int(guessed_state.y))
        turt.write(guess)
        correct_guess += 1
        correct_guess_list.append(guess)

    elif guess == 'Exit':
        break

    else:
        turt.goto(0, 0)
        correct_guess = correct_guess

missed_states = [state for state in state_names if state not in correct_guess_list]

df = pandas.DataFrame(missed_states)

df.to_csv("states_to_learn.csv")

