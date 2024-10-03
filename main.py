from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list=password_letter+password_symbols+password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_input.get()
    email=email_input.get()
    password=password_input.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                      f"\nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            with open("data.txt","a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

            website_input.delete(0,END)
            password_input.delete(0, END)

            website_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

canvas=Canvas(width=200, height=200)
myimg=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=myimg)
canvas.grid(column=1, row=0)

website_text=Label(text="Website:")
website_text.grid(column=0, row=1)

website_input=Entry(width=36)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_text=Label(text="Email/Username:")
email_text.grid(column=0, row=2)

email_input=Entry(width=36)
email_input.insert(0, "prasiddha.shah1@gmail.com")
email_input.grid(column=1, row=2, columnspan=2)

password_text=Label(text="Password:")
password_text.grid(column=0, row=3)

password_input=Entry(width=21)
password_input.grid(column=1, row=3)

password_button=Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button=Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
