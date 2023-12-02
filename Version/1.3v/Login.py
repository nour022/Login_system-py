import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import pandas
from datetime import date

# Style
font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 14)
font_color = "red"


class Login:
    def __init__(self):
        self.checkPasswd = ""
        self.root = tk.Tk()
        win_width = 700
        win_height = 570
        monitor_center_x = self.root.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = self.root.winfo_screenheight() / 2 - (win_height / 2)
        self.root.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#334257")
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
        img = Image.open("../../user.png").resize((250, 250))
        photo = ImageTk.PhotoImage(img)

        label_img = ttk.Label(self.div, image=photo)
        label_img.grid(row=0, column=1, sticky="n")

        # Username label
        username_L = ttk.Label(self.div, text="Username: ", font=font_Label)
        username_L.grid(row=1, column=0, sticky="ne", pady=10)
        # Todo function to check the Username if fund in Excel file if
        #   True or send a messagebox with to option (cansel | Register)
        self.username_eny = ttk.Entry(self.div)
        self.username_eny.grid(row=1, column=1, sticky="we", pady=10)
        self.username_eny.bind("<FocusOut>", func=self.check_username)
        # Password label
        password_L = ttk.Label(self.div, text="Password: ", font=font_Label)
        password_L.grid(row=3, column=0, sticky="ne", pady=10)
        # TODO function to check the Password if active the button login or send a messagebox or label
        self.password_eny = ttk.Entry(self.div, show="*")
        self.password_eny.grid(row=3, column=1, sticky="we", pady=10)
        ttk.Label(self.div, text=".      .      .      .").grid(row=3, column=2)
        #
        # TODO  function to save data in a csv file using Pandas
        login_btn = ttk.Button(self.div, text="Log-in", command=self.save_data)
        login_btn.grid(row=5, column=1, pady=10, sticky="n")
        label_register = ttk.Label(self.div, text="Sing Up")
        label_register.grid(row=6, column=1, pady=10, sticky="n")
        # label_register.bind("<Button>", self.reLayout)
        # -------------------End Body----------------------#
        self.root.mainloop()

    def check_username(self, event):
        username = self.username_eny.get()

        if len(username) >= 0:
            try:
                excel_file = pandas.read_excel('../../LoginDaten.xlsx')
                datas = excel_file.loc[excel_file["Username"] == username]
                str_commit = tk.StringVar()
                error_Label = ttk.Label(self.div, textvariable=str_commit)
                if len(datas) != 0:
                    self.checkPasswd = str(datas["Password"]).split(" ")[4].split("\n")[0]
                    # TODO create a csv file and save data after checking the password
                else:
                    str_commit.set("Dein Benutzername ist falsch")
                    error_Label.grid(row=2, column=1, sticky="we")
                    error_Label.config(foreground="red")
                    self.root.after(1000, error_Label.destroy)

            except FileNotFoundError:
                pass

    def save_data(self):
        username = self.username_eny.get()
        if self.password_eny.get() == self.checkPasswd:
            try:
                excel_file = pandas.read_excel('LoginDaten.xlsx')
                datas = excel_file.loc[excel_file["Username"] == username]
                datum = date.today()
                with open("login.csv", "a") as file:
                    file.write(f"{datas} | {datum} | verkaeufer\n")
                messagebox.showinfo(message="Login erfolgreich!")
                self.username_eny.delete(0, tk.END)
                self.password_eny.delete(0, tk.END)
            except FileNotFoundError:
                messagebox.showerror(message="Fehler beim Lesen der Daten")
        else:
            messagebox.showerror(message="Falsches Passwort")

main = Login()
