import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# style
font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 14)
# GUI
class Login:
    def __init__(self):
        root = tk.Tk()
        root.geometry("700x600")
        root.title("Log-in")

        root.config(bg="#334257")
        # Label Login
        labelLogin = ttk.Label(text="Login", font=font_h1)

        # # Frame Container  : 2 grid
        # fr_Container = ttk.LabelFrame(root,height=700, width=700,labelanchor="n")
        # fr_Container.pack(fill="both",pady=50,padx=50,ipadx=50,ipady=50)
        # fr_Container.columnconfigure(0,weight=1,)
        # fr_Container.columnconfigure(1,weight=1,)

        # Login Container
        div = ttk.LabelFrame(root, labelwidget=labelLogin, labelanchor="n")
        div.pack(fill="both", pady=50, padx=50)
        div.columnconfigure(0, weight=2, )
        div.columnconfigure(1, weight=2, )
        div.columnconfigure(2, weight=2, )
        # img  für user login
        img = Image.open("../user.png").resize((250, 250))
        photo = ImageTk.PhotoImage(img)

        label_img = ttk.Label(div, image=photo)
        label_img.grid(row=0, column=1, sticky="n")
        # Username label
        username_L = ttk.Label(div, text="Username: ", font=font_Label)
        username_L.grid(row=1, column=0, sticky="ne", pady=10)
        username_eny = ttk.Entry(div)
        username_eny.grid(row=1, column=1, sticky="we", pady=10)

        # Password label
        password_L = ttk.Label(div, text="Password: ", font=font_Label)
        password_L.grid(row=2, column=0, sticky="ne", pady=10)
        password_eny = ttk.Entry(div)
        password_eny.grid(row=2, column=1, sticky="we", pady=10)
        ttk.Label(div, text=".      .      .      .").grid(row=2, column=2)
        # passGenerator_btn = ttk.Button(div, text="Password Generator")
        # passGenerator_btn.grid(row=2, column=2, sticky="w", pady=10)

        login_btn = ttk.Button(div, text="Log-in")
        login_btn.grid(row=3, column=1, pady=10, sticky="n")

        # Password verseness?

        ver_pass_L = ttk.Label(div, text="Password vergessen?")
        ver_pass_L.grid(row=4, column=1, pady=10)

        root.mainloop()
# main = Login()