from tkinter import ttk, messagebox
import tkinter as tk
from PIL import Image, ImageTk
import pandas, re, random
from GUI.Login_GUI import Login
font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 10,"bold")
boder_eny = tk.SOLID


class Register:
    def __init__(self):
        self.root = tk.Tk()
        win_width = 700
        win_height = 550
        monitor_center_x = self.root.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = self.root.winfo_screenheight() / 2 - (win_height / 2)
        self.root.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        self.root.resizable(width=False,height=False)

        self.root.title("Register")
        self.root.config(bg="#334257")
        # Label Register
        labelLogin = ttk.Label(text="Register", font=font_h1)

        # Login Container
        div = ttk.LabelFrame(self.root, labelwidget=labelLogin, labelanchor="n")
        div.columnconfigure(0, weight=2, )
        div.columnconfigure(1, weight=2, )
        div.columnconfigure(2, weight=2, )
        #  calculate padding with percentage value.
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        padx = int(width * 2 / 100)
        pady = int(height * 5 / 100)
        div.pack(fill="both", pady=pady, padx=padx)

        # img  für user login
        img = Image.open("user.png").resize((150, 150))
        photo = ImageTk.PhotoImage(img)

        label_img = ttk.Label(div, image=photo)
        label_img.grid(row=0, column=1, sticky="n")

        # Full Name  label
        self.fA = False
        fullName_L = ttk.Label(div, text="Full Name:", font=font_Label)
        fullName_L.grid(row=1, column=0, sticky="ne", pady=10)

        self.fullName_eny = ttk.Entry(div)
        # self.fullName_eny.config()
        self.fullName_eny.grid(row=1, column=1, sticky="we", pady=10)
        # one event FocusOut for FullName To check a size of value
        self.fullName_eny.bind("<FocusOut>", func=self.check_name)
        # User Name L&eny
        username_label = ttk.Label(div, text="Username: ", font=font_Label)
        username_label.grid(row=2, column=0, sticky="ne", pady=10)

        self.username_eny = ttk.Entry(div)
        self.username_eny.grid(row=2, column=1, sticky="we", pady=10)
        # one event FocusOut for username To check if value is valid
        self.username_eny.bind("<FocusOut>", func=self.check_username)
        self.fU = False
        # Password label
        password_L = ttk.Label(div, text="Password: ", font=font_Label)
        password_L.grid(row=4, column=0, sticky="ne", pady=10)
        self.password_eny = ttk.Entry(div)
        self.password_eny.grid(row=4, column=1, sticky="we", pady=10)
        self.passGenerator_btn = ttk.Button(div, text="Password Generator", command=self.generat_password)
        self.passGenerator_btn.grid(row=4, column=2, sticky="w", pady=10)

        # Enter the password again
        password_L_2 = ttk.Label(div, text="Password-Again: ", font=font_Label)
        password_L_2.grid(row=6, column=0, sticky="ne", pady=10)
        self.password_eny_2 = ttk.Entry(div)
        self.password_eny_2.grid(row=6, column=1, sticky="we", pady=10)
        # one event FocusOut for Password To check if value is valid
        self.password_eny_2.bind("<FocusOut>", func=self.check_password)
        self.fP = False
        # done create a function to save all data.
        # save date button
        self.login_btn = ttk.Button(div, text="Register", command=self.save_data)
        self.login_btn.grid(row=8, column=1, pady=20, sticky="n")
        self.root.mainloop()

    def check_name(self, event):
        size = len(self.fullName_eny.get())
        if size < 6:
            messagebox.showinfo(message=f"current your name min < 6 case your \t{size} !!")
        else:
            self.fA = True

    def check_username(self, e):
        username = self.username_eny.get()
        if len(username) > 4:
            try:
                excel_file = pandas.read_excel('LoginDaten.xlsx')
                datas = excel_file.loc[excel_file["Username"] == username]
                print(datas)
                if len(datas) != 0:
                    messagebox.showinfo(
                        message=f"Diese Username {username} ist Schon besitzt versuchen sie andere username")
                else:
                    self.fU = True
            except FileNotFoundError:
                self.fU = True
        else:
            messagebox.showinfo(
                message=f"Der eingegebene Benutzername {username} ist zu kurz. Bitte verwenden Sie einen Benutzernamen mit mindestens 5 Zeichen.")

    def check_password(self, e):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&\(\)])[A-Za-z\d@\(\)$!%*?&+**,&%#*!#@]{8,}$"
        passwd = self.password_eny.get()
        if re.match(pattern, passwd):
            if passwd == self.password_eny_2.get():
                self.fP = True
            else:
                messagebox.showinfo(
                    message="Die eingegebenen Passwörter\n stimmen nicht überein. \nBitte überprüfen Sie Ihre Eingabe\n oder nutzen sie unsere Password Genariter")
        else:
            messagebox.showinfo(
                message="mindestens 8 Zeichen lang \nmindestens eine Kleinbuchstabe\nmindestens eine Großbuchstabe\nmindestens eine Zahl\nmindestens ein Sonderzeichen")

    def generat_password(self):
        self.password_eny.delete(0, tk.END)
        self.password_eny_2.delete(0, tk.END)
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

        for char in range(nr_letters):
            password_list.append(random.choice(letters))

        for char in range(nr_symbols):
            password_list += random.choice(symbols)

        for char in range(nr_numbers):
            password_list += random.choice(numbers)

        random.shuffle(password_list)

        password = ""
        for char in password_list:
            password += char
        self.password_eny.insert(0, password)
        self.password_eny_2.insert(0, password)
        self.check_password("")

    def save_data(self):
        if self.fU and self.fP and self.fA:
            username = self.username_eny.get()
            password = self.password_eny.get()
            full_name = self.fullName_eny.get()
            data = {
                'Full Name': [full_name], 'Username': [username], 'Password': [password], "roll": False, "Budget": 0
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
            self.delet_data()
            self.root.destroy()
            main = Login()
        else:
            print(f"Username {self.fU} : Password {self.fP} : Fullname {self.fA}")
            messagebox.showerror(message="Hallo deine Eingabe")

    def delet_data(self):
        messagebox.showinfo(message=f"Username : {self.username_eny.get()} \nPassword: {self.password_eny.get()}")
        self.password_eny.delete(0, tk.END)
        self.password_eny_2.delete(0, tk.END)
        self.username_eny.delete(0, tk.END)
        self.fullName_eny.delete(0, tk.END)
        self.fU = False
        self.fA = False
        self.fP = False


root = Register()
