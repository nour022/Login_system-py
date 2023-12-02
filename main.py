from tkinter import ttk, messagebox
import tkinter as tk
import pandas, re, random
from PIL import Image, ImageTk
from datetime import date

# Style
font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 14)
font_color = "red"


class Main:
    def __init__(self):
        self.checkPasswd = ""
        self.main = tk.Tk()
        win_width = 700
        win_height = 570
        monitor_center_x = self.main.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = self.main.winfo_screenheight() / 2 - (win_height / 2)
        self.main.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        self.main.resizable(width=False, height=False)
        self.main.config(bg="#334257")
        self.root = tk.Frame(self.main)
        self.root.pack()
        # ------------------------------ Register ------------------------------#
        # Login Container
        labelLogin = ttk.Label(text="Register", font=font_h1)
        self.div1 = ttk.LabelFrame(self.root, labelwidget=labelLogin, labelanchor="n")
        self.div1.columnconfigure(0, weight=2, )
        self.div1.columnconfigure(1, weight=2, )
        self.div1.columnconfigure(2, weight=2, )
        #  calculate padding with percentage value.
        width = self.main.winfo_screenwidth()
        height = self.main.winfo_screenheight()
        self.padx = int(width * 2 / 100)
        self.pady = int(height * 5 / 100)
        # self.div1.pack(fill="both", pady=pady, padx=padx)

        # img  für user login
        img = Image.open("user.png").resize((160, 160))
        photo = ImageTk.PhotoImage(img)

        label_img = ttk.Label(self.div1, image=photo)
        label_img.grid(row=0, column=1, sticky="n")

        # Full Name  label
        self.fA = False
        fullName_L = ttk.Label(self.div1, text="Full Name:", font=font_Label)
        fullName_L.grid(row=1, column=0, sticky="ne", pady=10)

        self.fullName_eny = ttk.Entry(self.div1)
        # self.fullName_eny.config()
        self.fullName_eny.grid(row=1, column=1, sticky="we", pady=10)
        # one event FocusOut for FullName To check a size of value
        self.fullName_eny.bind("<FocusOut>", func=self.check_name)
        # User Name L&eny
        username_label = ttk.Label(self.div1, text="Username: ", font=font_Label)
        username_label.grid(row=2, column=0, sticky="ne", pady=10)

        self.username_eny = ttk.Entry(self.div1)
        self.username_eny.grid(row=2, column=1, sticky="we", pady=10)
        # one event FocusOut for username To check if value is valid
        self.username_eny.bind("<FocusOut>", func=self.check_username)
        self.fU = False
        # Password label
        password_L = ttk.Label(self.div1, text="Password: ", font=font_Label)
        password_L.grid(row=4, column=0, sticky="ne", pady=10)
        self.password_eny = ttk.Entry(self.div1)
        self.password_eny.grid(row=4, column=1, sticky="we", pady=10)
        self.passGenerator_btn = ttk.Button(self.div1, text="Password Generator", command=self.generat_password)
        self.passGenerator_btn.grid(row=4, column=2, sticky="w", pady=10)

        # Enter the password again
        password_L_2 = ttk.Label(self.div1, text="Password-Again: ", font=font_Label)
        password_L_2.grid(row=6, column=0, sticky="ne", pady=10)
        self.password_eny_2 = ttk.Entry(self.div1, show="*")
        self.password_eny_2.grid(row=6, column=1, sticky="we", pady=10)
        # one event FocusOut for Password To check if value is valid
        self.password_eny_2.bind("<FocusOut>", func=self.check_password)
        self.fP = False
        # done create a function to save all data.
        # save date button
        self.login_btn = ttk.Button(self.div1, text="Register", command=self.save_data)
        self.login_btn.grid(row=8, column=1, pady=20, sticky="n")
        # ------------------------------ End Register ------------------------------#
        # ------------------------------ Login ------------------------------#

        # ----------------------Body-----------------------#
        # Label Login
        labelLogin = ttk.Label(text="Login", font=font_h1)
        # Login Container
        self.div = ttk.LabelFrame(self.root, labelwidget=labelLogin, labelanchor="n")
        self.div.pack(fill="both", pady=50, padx=50)
        self.div.columnconfigure(0, weight=2, )
        self.div.columnconfigure(1, weight=2, )
        self.div.columnconfigure(2, weight=2, )

        # img  für user login

        label_img = ttk.Label(self.div, image=photo)
        label_img.grid(row=0, column=1, sticky="n")
        # Username label
        username_L = ttk.Label(self.div, text="Username: ", font=font_Label)
        username_L.grid(row=1, column=0, sticky="ne", pady=10)
        # Todo function to check the Username if fund in Excel file if
        #   True or send a messagebox with to option (cansel | Register)
        self.username_eny_L = ttk.Entry(self.div)
        self.username_eny_L.grid(row=1, column=1, sticky="we", pady=10)
        self.username_eny_L.bind("<FocusOut>", func=self.check_username_l)
        # Password label
        password_L = ttk.Label(self.div, text="Password: ", font=font_Label)
        password_L.grid(row=3, column=0, sticky="ne", pady=10)
        # TODO function to check the Password if active the button login or send a messagebox or label
        self.password_eny_L = ttk.Entry(self.div, show="*")
        self.password_eny_L.grid(row=3, column=1, sticky="we", pady=10)
        ttk.Label(self.div, text=".      .      .      .").grid(row=3, column=2)
        # TODO  function to save a data in csv with Pandas
        login_btn = ttk.Button(self.div, text="Log-in", command=self.save_date)
        login_btn.grid(row=5, column=1, pady=10, sticky="n")
        label_register = ttk.Label(self.div, text="Sing Up")
        label_register.grid(row=6, column=1, pady=10, sticky="n")
        label_register.bind("<Button>", self.reLayout)
        # -------------------End Body----------------------#
        self.main.mainloop()

    def check_username_l(self, e):
        username = self.username_eny_L.get()

        if len(username) >= 0:
            try:
                excel_file = pandas.read_excel('LoginDaten.xlsx')
                datas = excel_file.loc[excel_file["Username"] == username]
                str_commit = tk.StringVar()
                error_Label = tk.Label(self.div, textvariable=str_commit)
                if len(datas) != 0:
                    self.checkPasswd = str(datas["Password"]).split(" ")[4].split("\n")[0]
                    # TODO create a csv file and save a data after checking the password
                else:
                    # messagebox.showwarning(message="Hallo deine eingabe")
                    str_commit.set("Deine Username ist Falsch")
                    error_Label.grid(row=2, column=1, sticky="we")
                    error_Label.config(foreground="red")
                    self.root.after(2000, error_Label.destroy)


            except FileNotFoundError:
                pass

    def save_date(self):
        username = self.username_eny_L.get()
        if self.password_eny_L.get() == self.checkPasswd:
            excel_file = pandas.read_excel('LoginDaten.xlsx')
            datas = excel_file.loc[excel_file["Username"] == username]
            datum = date.today()
            try:
                with open("login.csv", "w") as file:
                    file.write(f"{datas} | {datum} | verkaeufer")
            except FileNotFoundError:
                with open("login.csv", "a") as file:
                    file.write(f"{datas} | {datum} | verkaeufer")
            self.root.pack_forget()
            self.homePage()

    # ------------------------------ Register ------------------------------#
    def reLayout(self, r):
        self.div.pack_forget()
        self.div1.pack(fill="x", pady=self.pady, padx=self.padx)

    def check_name(self, event):
        size = len(self.fullName_eny.get())
        if size < 6:
            # Todo label eingeugen statt messagebox!
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
                    # Todo label eingeugen statt messagebox!
                    messagebox.showinfo(
                        message=f"Diese Username {username} ist Schon besitzt versuchen sie andere username")
                else:
                    self.fU = True
            except FileNotFoundError:
                self.fU = True
        else:
            # Todo label eingeugen statt messagebox!
            messagebox.showinfo(
                message=f"Der eingegebene Benutzername {username} ist zu kurz. Bitte verwenden Sie einen Benutzernamen mit mindestens 5 Zeichen.")

    def check_password(self, e):
        pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&\(\)])[A-Za-z\d@\(\)$!%*?&+**,&%#*!#@]{8,}$"
        passwd = self.password_eny.get()
        if re.match(pattern, passwd):
            if passwd == self.password_eny_2.get():
                self.fP = True
            else:
                # Todo label eingeugen statt messagebox!
                messagebox.showinfo(
                    message="Die eingegebenen Passwörter\n stimmen nicht überein. \nBitte überprüfen Sie Ihre Eingabe\n oder nutzen sie unsere Password Genariter")
        else:
            # Todo label eingeugen statt messagebox!
            messagebox.showinfo(
                message="mindestens 8 Zeichen lang \nmindestens eine Kleinbuchstabe\nmindestens eine Großbuchstabe\nmindestens eine Zahl\nmindestens ein Sonderzeichen")

    def generat_password(self):
        self.password_eny.delete(0, tk.END)
        self.password_eny_2.delete(0, tk.END)
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                   't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O',
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
            self.delet_data()
            self.div1.pack_forget()
            self.root.pack()
        else:
            # Todo label eingeugen statt messagebox!
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

    # -------------Home------------#
    def homePage(self):
        self.main.resizable(width=True, height=True)
        self.main.config(bg="#fff")
        menu = tk.Frame(self.main)
        menu.config(background="#334257")
        menu.pack(fill="both", )

        label1 = ttk.Label(menu, text="Logo", background="#334257", foreground="#fff")
        label1.pack(side="left", pady=10, padx=30)
        label_wg = ttk.Label(menu, text="Einkaufswagen", background="#334257", foreground="#fff")
        label_wg.pack(side="right", pady=10, padx=30)

        body = tk.Frame(self.main, bg="#334257")
        body.pack(fill="both", padx=30)

        def test(e):
            body.pack_forget()

        label2 = tk.Label(body, text="Main", )
        label2.pack()
        label2.bind("<Button 1>", func=test)
        footer = tk.Frame(self.main)
        footer.pack(fill="both")
        footer.config(background="#334257")

        label3 = tk.Label(footer, text="footer", background="#334257", foreground="#fff")
        label3.pack(pady=10, padx=10)


test = Main()
