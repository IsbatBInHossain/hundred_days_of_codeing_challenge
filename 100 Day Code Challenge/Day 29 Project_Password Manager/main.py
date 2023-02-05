from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.delete(0, END)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    user_id = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:
            {
                "e-mail": user_id,
                "password": password,
            }
    }

    if website == "" or user_id == "" or password == "":
        messagebox.showerror(title="Error", message='Please insert all the inputs')
    else:
        if messagebox.askokcancel(title=website, message=f'\nEmail: {user_id}'
                                                         f'\nPassword: {password}\nIs it okay to save?'):
            try:
                with open("password.json", mode='r') as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("password.json", mode='w') as file:
                    json.dump(new_data, fp=file, indent=4)
            else:
                with open("password.json", mode='w') as file:
                    json.dump(data, fp=file, indent=4)
            finally:
                website_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
                email_entry.insert(0, "isbat31416@gmail.com")
                pyperclip.copy(password)
                password_entry.delete(0, 'end')
                website_entry.focus()


# ---------------------------- Search Passwords ------------------------------- #
def search_password():
    website = website_entry.get()
    try:
        with open("password.json", mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]['e-mail']
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"E-mail: {email}\nPassword: {password}")
            pyperclip.copy(password)
        else:
            messagebox.showerror(title="Error", message=f"No details on {website} found on database")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
logo = PhotoImage(file="logo.png")
canvas = Canvas(width=180, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=29)
website_entry.grid(row=1, column=1, sticky=W)
website_entry.focus()
email_entry = Entry(width=49)
email_entry.grid(row=2, column=1, columnspan=2, sticky=W)
email_entry.insert(0, "isbat31416@gmail.com")
password_entry = Entry(width=29)
password_entry.grid(row=3, column=1, sticky=W)

# Buttons
generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(row=3, column=2, sticky=W)
add_button = Button(text="Add", width=41, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky=W)
search_button = Button(text="Search", width=15, command=search_password)
search_button.grid(row=1, column=2, sticky=W)
window.mainloop()
