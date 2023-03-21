import json
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(END, f"{password}")

    # pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    shift = randint(11111, 99999)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cap_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                    "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def caesar(start_text, shift_amount):
        end_text = ""
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            elif char in cap_alphabet:
                position = cap_alphabet.index(char)
                new_position = position + shift_amount
                end_text += cap_alphabet[new_position]
            else:
                end_text += char
        return end_text

    e_shift = shift
    shift = shift % 26
    e_password = caesar(start_text=password, shift_amount=shift)

    new_data = {
        website:
            {
                "email": username,
                "password": e_password,
                "ref_id": e_shift
            }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Caution!!", message="Please don't leave any fields Empty ")
    else:
        try:
            with open("Your-Data.json", mode="r") as file:
                # loading data
                data = json.load(file)

        except FileNotFoundError:
            with open("Your-Data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:

            # updating data
            data.update(new_data)

            with open("Your-Data.json", 'w') as file:

                json.dump(data, file, indent=4)

        finally:
            with open("Your-Data.json", 'r') as file:
                data = json.load(file)
                website_show.delete(0, END)
                for key, value in data.items():
                    website_show.insert(1, f'{key}')
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.delete(0, END)


# ---------------------------- Show Data ------------------------------ #


def show_data():
    website = website_entry.get()

    # added listbox selection to search 
    for i in website_show.curselection():
        website = website_show.get(i)

    if website == "":
        messagebox.showinfo(title="Caution!!", message="Please don't leave any fields Empty ")
    else:
        try:
            with open("Your-Data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No Data File Found")
        else:
            try:
                new_data = data[website]
            except KeyError:
                messagebox.showwarning(title="Error",
                                       message=f"You didn't save the {website} account, yet.\nGo and Save it")
            # except :
            #     messagebox.showwarning(title="Error", message="Enter website")
            else:

                alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                cap_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H",
                                "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
                                "Z"]

                def caesar(start_text, shift_amount):
                    end_text = ""
                    for char in start_text:
                        if char in alphabet:
                            position = alphabet.index(char)
                            new_position = position - shift_amount
                            end_text += alphabet[new_position]
                        elif char in cap_alphabet:
                            position = cap_alphabet.index(char)
                            new_position = position - shift_amount
                            end_text += cap_alphabet[new_position]
                        else:
                            end_text += char
                    return end_text

                shift = new_data['ref_id']
                e_password = new_data["password"]
                shift = shift % 26
                d_password = caesar(start_text=e_password, shift_amount=shift)

                messagebox.showinfo(title="Your Password", message=f"Website: {website}\n"
                                                                   f"Email: {new_data['email']}\n"
                                                                   f"Password: {d_password}")


# ------------------------ Remove Password ---------------------------- #

def remove_password():
    website = website_entry.get()

    # added listbox selection to search 
    for i in website_show.curselection():
        website = website_show.get(i)

    if website == "":
        messagebox.showinfo(title="Caution!!", message="Please don't leave any fields Empty ")
    else:
        try:
            with open("Your-Data.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Error", message="No Data File Found")
        else:
            try:
                new_data = data[website]
            except KeyError:
                messagebox.showwarning(title="Error",
                                       message=f"You didn't save the {website} account, yet.\nGo and Save it")
            else:
                new_data = {key: value for key, value in data.items() if key != website}
                with open("Your-Data.json", 'w') as file:
                    json.dump(new_data, file, indent=4)
                messagebox.showwarning(title="Removed",
                                       message=f"Your Password for {website} is been Removed.\n")

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                with open("Your-Data.json", 'r') as file:
                    data = json.load(file)
                    website_show.delete(0, END)
                    for key, value in data.items():
                        website_show.insert(1, f'{key}')
                


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PassWord Manager.")
window.config(padx=50, pady=50, bg="#99d2de")

canvas = Canvas(width=200, height=200, bg="#99d2de", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website
website_label = Label(text="Website :", bg="#99d2de")
website_label.grid(column=0, row=1)

website_entry = Entry(width=31)
website_entry.grid(column=1, row=1)
website_entry.focus()

website_show = Listbox(width=31, height=5, bg="#8fb1b8", fg="white")

try:
    with open("Your-Data.json", 'r') as file:
        data = json.load(file)
        list_id = 0
        for key, value in data.items():
            website_show.insert(list_id, f'{key}')
            list_id += 1
except FileNotFoundError:
    website_show.insert(1, '')
else:
    # website_show.insert(1, '')
    None
      
website_show.grid(column=1,row=2)

# empty label
empty_label = Label(bg="#99d2de")
empty_label.grid(column=0, row=2)

# username
id_username_label = Label(text="Email/Username :", bg="#99d2de")
id_username_label.grid(column=0, row=3)

username_entry = Entry(width=49)
username_entry.grid(column=1, row=3, columnspan=2)
# username_entry.insert(END, "@gmail.com")

# empty label
empty_label = Label(bg="#99d2de")
empty_label.grid(column=0, row=4)

# password
password_label = Label(text="Password :", bg="#99d2de")
password_label.grid(column=0, row=5)

password_entry = Entry(width=31)
password_entry.grid(column=1, row=5)

# empty label
empty_label = Label(bg="#99d2de")
empty_label.grid(column=0, row=6)

empty_label = Label(bg="#99d2de")
empty_label.grid(column=0, row=8)

# button
generate_pass_button = Button(text="Generate Password", borderwidth=0.5)
generate_pass_button.config(command=generate_password)
generate_pass_button.grid(column=2, row=5)

add_button = Button(text="Add", width=42, borderwidth=0.5)
add_button.config(command=save_data)
add_button.grid(column=1, row=7, columnspan=2)

search_button = Button(text="Search", width=14, borderwidth=0.5)
search_button.config(command=show_data)
search_button.grid(column=2, row=1)

remove_button = Button(text="Delete Password", width=42, borderwidth=0.5)
remove_button.config(command=remove_password)
remove_button.grid(column=1, row=9, columnspan=2)


window.mainloop()
