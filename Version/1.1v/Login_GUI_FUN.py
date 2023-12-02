import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Style
font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 14)
font_color = "red"


class Login:
    def __init__(self):
        self.root = tk.Tk()
        win_width = 700
        win_height = 550
        monitor_center_x = self.root.winfo_screenwidth() / 2 - (win_width / 2)
        monitor_center_y = self.root.winfo_screenheight() / 2 - (win_height / 2)
        self.root.geometry("%dx%d+%d+%d" % (win_width, win_height, monitor_center_x, monitor_center_y))
        self.root.resizable(width=False, height=False)
        self.root.config(bg="#334257")
        # ----------------------Body-----------------------#
        # Label Login
        labelLogin = ttk.Label(text="Login", font=font_h1)
        # Login Container
        div = ttk.LabelFrame(self.root, labelwidget=labelLogin, labelanchor="n")
        div.pack(fill="both", pady=50, padx=50)
        div.columnconfigure(0, weight=2, )
        div.columnconfigure(1, weight=2, )
        div.columnconfigure(2, weight=2, )

        # img  für user login
        img = Image.open("user.png").resize((250, 250))
        photo = ImageTk.PhotoImage(img)

        label_img = ttk.Label(div, image=photo)
        label_img.grid(row=0, column=1, sticky="n")
        # Username label
        username_L = ttk.Label(div, text="Username: ", font=font_Label)
        username_L.grid(row=1, column=0, sticky="ne", pady=10)
        # Todo function to check the Username if fund in Excel file if
        #   True or send a messagebox with to option (cansel | Register)
        self.username_eny = ttk.Entry(div)
        self.username_eny.grid(row=1, column=1, sticky="we", pady=10)

        # Password label
        password_L = ttk.Label(div, text="Password: ", font=font_Label)
        password_L.grid(row=3, column=0, sticky="ne", pady=10)
        # TODO function to check the Password if active the button login or send a messagebox or label
        self.password_eny = ttk.Entry(div)
        self.password_eny.grid(row=3, column=1, sticky="we", pady=10)
        ttk.Label(div, text=".      .      .      .").grid(row=3, column=2)
        # TODO  function to save a data in csv with Pandas
        login_btn = ttk.Button(div, text="Log-in")
        login_btn.grid(row=5, column=1, pady=10, sticky="n")
        # -------------------End Body----------------------#
        self.root.mainloop()


main = Login()
##
# roll ?
# User Login  roll ? Verkufer : keufe
# if True save date in csv (username , Roll, Date, Budget)

##
# import tkinter as tk
# from tkinter import ttk,messagebox
# from PIL import Image, ImageTk
# import pandas
#
# # Style
# font_h1 = ("Helvetica", 25, "bold")
# font_Label = ("Helvetica", 14)
# font_color = "red"
#
#
# class Login:
#     def __init__(self):
#         self.div = None
#         self.username_eny = None
#         self.root = tk.Tk()
#
#         self.root.geometry("450x400")
#         self.root.title("Register")
#         self.root.resizable(width=False, height=False)
#         # ___________[Buttoms + Icons]_____________#
#
#         # <<<[Logo Icon]>>>>>
#         image_logo = Image.open("./Register-am/Register/images/logo.png").resize((250, 200))
#         photo_logo = ImageTk.PhotoImage(image_logo)
#         logo_lab = ttk.Label(self.root, image=photo_logo)
#         logo_lab.place(x=90, y=10)
#         # <<<[image_logo_keufer]>>>>>
#         image_logo_keufer = Image.open("./Register-am/Register/images/käufer.png").resize((70, 50))
#         photo_logo_keufer = ImageTk.PhotoImage(image_logo_keufer)
#
#         self.register_btn_keufer = tk.Button(self.root, text="Kaeufer", fg="black", width=125, bg="white",
#                                              cursor="hand2",
#                                              image=photo_logo_keufer, bd=1, relief="solid", compound="top",
#                                              font=("Courier", 12), command=self.log)
#         self.register_btn_keufer.place(x=80, y=233)
#
#         self.register_btn_keufer.bind("<Enter>", self.on_keufer)
#         self.register_btn_keufer.bind("<Leave>", self.on_leave_keufer)
#         # <<<[image_logo_verkeufer]>>>>>
#         image_logo_verkeufer = Image.open("./Register-am/Register/images/verkäfer.png").resize((70, 50))
#         photo_logo_verkeufer = ImageTk.PhotoImage(image_logo_verkeufer)
#
#         self.register_btn_verkeufer = tk.Button(self.root, text="verkaeufer", fg="black", width=125, bg="white",
#                                                 cursor="hand2",
#                                                 image=photo_logo_verkeufer, bd=1, relief="solid", compound="top",
#                                                 font=("Courier", 12), command=self.log)
#         self.register_btn_verkeufer.place(x=240, y=260)
#
#         self.register_btn_verkeufer.bind("<Enter>", self.on_verkeufer)  # wenn noch maus drauf ist
#         self.register_btn_verkeufer.bind("<Leave>",
#                                          self.on_leave_verkeufer)
#         # wenn kein leave Bind dann bleibt der bottom immer on
#
#         self.root.mainloop()
#
#     # ---------[Funcitons]----------#
#     def on_keufer(self, event=None):
#         self.register_btn_keufer.config(background="black", foreground="white")
#
#     def on_leave_keufer(self, event=None):
#         self.register_btn_keufer.config(background="white", foreground="black")
#
#     def on_verkeufer(self, event=None):
#         self.register_btn_verkeufer.config(background="black", foreground="white")
#
#     def on_leave_verkeufer(self, event=None):
#         self.register_btn_verkeufer.config(background="white", foreground="black")
#
#     def log(self):
#         self.root.geometry("830x400")
#         b1 = tk.Button(self.root, text="<", height=25, bd=1, relief="solid", bg="white", command=self.hide)
#         b1.place(x=810, y=5)
#
#         # TODO <<<Ein Frame für die Login oder registeren seite --- Bei login kommt log-in Frame und beim Registieren erschein den Nutzer reqistieren Frame>>>
#         register_Frame = tk.Frame(self.root, bg="#334257", bd=1, relief="solid")
#         register_Frame.place(x=450, y=5, width=356, height=390)
#
#         # ----------------------Body-----------------------#
#         # Label Login
#         labelLogin = ttk.Label(text="Login", font=font_h1)
#         # Login Container
#         self.div = ttk.LabelFrame(register_Frame, labelwidget=labelLogin, labelanchor="n")
#         self.div.pack(fill="both", pady=60)
#         self.div.columnconfigure(0, weight=2, )
#         self.div.columnconfigure(1, weight=2, )
#         self.div.columnconfigure(2, weight=2, )
#
#         # img  für user login
#         img = Image.open("user.png").resize((250, 250))
#         photo = ImageTk.PhotoImage(img)
#
#         label_img = ttk.Label(self.div, image=photo)
#         label_img.grid(row=0, column=1, sticky="n")
#         # Username label
#         username_L = ttk.Label(self.div, text="Username: ", font=font_Label)
#         username_L.grid(row=1, column=0, sticky="ne", pady=10)
#         # Todo function to check the Username if fund in Excel file if
#         #   True or send a messagebox with to option (cansel | Register)
#         self.username_eny = ttk.Entry(self.div)
#         self.username_eny.grid(row=1, column=1, sticky="we", pady=10)
#         self.username_eny.bind("<FocusOut>", func=self.check_username)
#         # Password label
#         password_L = ttk.Label(self.div, text="Password: ", font=font_Label)
#         password_L.grid(row=3, column=0, sticky="ne", pady=10)
#         # TODO function to check the Password if active the button login or send a messagebox or label
#         self.password_eny = ttk.Entry(self.div)
#         self.password_eny.grid(row=3, column=1, sticky="we", pady=10)
#         ttk.Label(self.div, text=".      .      .      .").grid(row=3, column=2)
#         # TODO  function to save a data in csv with Pandas
#         login_btn = ttk.Button(self.div, text="Log-in")
#         login_btn.grid(row=5, column=1, pady=10, sticky="n")
#         # -------------------End Body----------------------#
#
#     def check_username(self, ev):
#         username = self.username_eny.get()
#         passwd = self.password_eny.get()
#         if len(username) >= 0 and len(passwd) >= 0:
#             try:
#                 excel_file = pandas.read_excel('LoginDaten.xlsx')
#                 datas = excel_file.loc[excel_file["Username"] == username]
#                 if len(datas) != 0:
#
#                     print(datas)
#                     # TODO create a csv file and save a data after checking the password
#                 else:
#                     messagebox.showwarning(message="Hallo deine eingabe")
#                     str_commit.set("Deine Username ist Falsch")
#                                         error_Label.grid(row=2, column=1, sticky="we")
#                                         error_Label.config(foreground="red")
#                                         self.root.after(1000, error_Label.destroy)
#
#             except FileNotFoundError:
#                 pass
#
#     def hide(self, event=None):
#         self.root.geometry("450x400")
#
#
# main = Login()##
