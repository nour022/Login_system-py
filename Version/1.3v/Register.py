from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import pandas, re, random
from GUI.Login_GUI import Login

font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 10, "bold")
border_style = tk.SOLID


class Register:
    def __init__(self):
        self.root = tk.Tk()
        win_width = 700
        win_height = 550
        monitor_center_x = self.root.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = self.root.winfo_screenheight() / 2 - (win_height / 2)
        self.root.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        self.root.resizable(width=False, height=False)

        self.root.title("Register")
        self.root.config(bg="#334257")

        # Label Register
        label_login = ttk.Label(text="Register", font=font_h1)

        # Login Container
        div = ttk.LabelFrame(self.root, labelwidget=label_login, labelanchor="n")
        div.columnconfigure(0, weight=2)
        div.columnconfigure(1, weight=2)
        div.columnconfigure(2, weight=2)
        # calculate padding with percentage value.
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        padx = int(width * 2 / 100)
        pady = int(height * 5 / 100)
        div.pack(fill="both", pady=pady, padx=padx)

        # Image for user login
        img = Image.open("../../user.png").resize((150, 150))
        photo = ImageTk.PhotoImage(img)

        label_img = ttk.Label(div, image=photo)
        label_img.grid(row=0, column=1, sticky="n")

        # Full Name label
        self.fA = False
        full_name_label = ttk.Label(div, text="Full Name:", font=font_Label)
        full_name_label.grid(row=1, column=0, sticky="ne", pady=10)

        self.full_name_entry = ttk.Entry(div)
        self.full_name_entry.grid(row=1, column=1, sticky="we", pady=10)
        # one event FocusOut for FullName To check the size of the value
        self.full_name_entry.bind("<FocusOut>", func=self.check_name)

        # User Name Label & Entry
        username_label = ttk.Label(div, text="Username: ", font=font_Label)
        username_label.grid(row=2, column=0, sticky="ne", pady=10)

        self.username_entry = ttk.Entry(div)
        self.username_entry.grid(row=2, column=1, sticky="we", pady=10)
        # one event FocusOut for username To check if the value is valid
        self.username_entry.bind("<FocusOut>", func=self.check_username)
        self.fU = False

        # Password label
        password_label = ttk.Label(div, text="Password: ", font=font_Label)
        password_label.grid(row=4, column=0, sticky="ne", pady=10)
        self.password_entry = ttk.Entry(div)
        self.password_entry.grid(row=4, column=1, sticky="we", pady=10)
        self.pass_generator_btn = ttk.Button(div, text="Password Generator", command=self.generate_password)
        self.pass_generator_btn.grid(row=4, column=2, sticky="w", pady=10)

        # Enter the password again

        password_label_2 = ttk.Label(div, text="Password-Again: ", font=font_Label)
        password_label_2.grid(row=6, column=0, sticky="ne", pady=10)
        self.password_entry_2 = ttk.Entry(div)
        self.password_entry_2.grid(row=6, column=1, sticky="we", pady=10)
        # one event FocusOut for Password To check if the value is valid
        self.password_entry_2.bind("<FocusOut>", func=self.check_password)
        self.fP = False
        # Save data button
        self.register_btn = ttk.Button(div, text="Register", command=self.save_data)
        self.register_btn.grid(row=8, column=1, pady=20, sticky="n")
        self.root.mainloop()

    def check_name(self, event):
        size = len(self.full_name_entry.get())
        if size < 6:
            messagebox.showinfo(message=f"Your name must be at least 6 characters long. Current size: {size}")
        else:
            self.fA = True

    def check_username(self, e):
        username = self.username_entry.get()
        if len(username) > 4:
            try:
                excel_file = pandas.read_excel('LoginDaten.xlsx')
                datas = excel_file.loc[excel_file["Username"] == username]
                print(datas)
                if len(datas) != 0:
                    messagebox.showinfo(
                        message=f"This username '{username}' is already taken. Please choose another username.")
                else:
                    self.fU = True
            except FileNotFoundError:
                self.fU = True
        else:
            messagebox.showinfo(
                message=f"The entered username '{username}' is too short. Please use a username with at least 5 characters.")

    def check_password(self, e):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&\(\)])[A-Za-z\d@\(\)$!%*?&+**,&%#*!#@]{8,}$"
        password = self.password_entry.get()
        if re.match(pattern, password):
            if password == self.password_entry_2.get():
                self.fP = True
            else:
                messagebox.showinfo(
                    message="The entered passwords do not match. Please check your input or use our Password Generator.")
        else:
            messagebox.showinfo(
                message="Password requirements:\n- Minimum length of 8 characters\n- At least one lowercase letter\n- At least one uppercase letter\n- At least one digit\n- At least one special character")

    def generate_password(self):
        self.password_entry.delete(0, tk.END)
        self.password_entry_2.delete(0, tk.END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '@', '%', '&', '(', ')', '*', '+']
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        for _ in range(nr_letters):
            password_list.append(random.choice(letters))

        for _ in range(nr_symbols):
            password_list += random.choice(symbols)

        for _ in range(nr_numbers):
            password_list += random.choice(numbers)

        random.shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.insert(0, password)
        self.password_entry_2.insert(0, password)
        self.check_password("")

    def save_data(self):
        if self.fU and self.fP and self.fA:
            username = self.username_entry.get()
            password = self.password_entry.get()
            full_name = self.full_name_entry.get()
            data = {
                'Full Name': [full_name], 'Username': [username], 'Password': [password], "roll": False,
                "Budget": 100000
            }
            new_data = pandas.DataFrame(data)
            try:
                excel_file = pandas.read_excel('LoginDaten.xlsx')
            except FileNotFoundError:
                # create new Excel file with new data
                new_data.to_excel('LoginDaten.xlsx', index=False)
                # excel_file = pandas.read_excel('LoginDaten.xlsx')
            # append new data to existing Excel file
            updated_data = pandas.concat([excel_file, new_data])
            updated_data.to_excel('LoginDaten.xlsx', index=False)
            self.clear_data()
            self.root.destroy()
            main = Login()
        else:
            print(f"Username {self.fU} : Password {self.fP} : Fullname {self.fA}")
            messagebox.showerror(message="Hello, please check your input.")

    def clear_data(self):
        messagebox.showinfo(message=f"Username: {self.username_entry.get()}\nPassword: {self.password_entry.get()}")
        self.password_entry.delete(0, tk.END)
        self.password_entry_2.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.full_name_entry.delete(0, tk.END)
        self.fU = False
        self.fA = False
        self.fP = False

root = Register()