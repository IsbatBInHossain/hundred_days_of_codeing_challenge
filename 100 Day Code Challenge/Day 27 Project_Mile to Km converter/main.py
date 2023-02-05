from tkinter import *


def miles_to_km():
    mile = float(entry.get())
    km = round(mile * 1.60934, 2)
    label_2.config(text=f"{km}")


window = Tk()
window.minsize(width=250, height=100)
window.title("Mile to km converter")
window.config(padx=20, pady=20)

entry = Entry(width=7)
entry.grid(column=1, row=0, pady=10, ipadx=10)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2, pady=10)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text=f"0")
label_2.grid(column=1, row=1)

label_3 = Label(text="km")
label_3.grid(column=2, row=1)

label_4 = Label(text="Miles")
label_4.grid(column=2, row=0, padx=10, pady=10)

window.mainloop()
