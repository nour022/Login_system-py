import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# style
font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 10)
# GUI   Done

root = tk.Tk()
root.geometry("700x550")
root.title("Register")
root.config(bg="#334257")

# Label Register Done
labelLogin = ttk.Label(text="Register", font=font_h1)

# Login Container Done

div = ttk.LabelFrame(root, labelwidget=labelLogin, labelanchor="n")

div.columnconfigure(0, weight=2, )
div.columnconfigure(1, weight=2, )
div.columnconfigure(2, weight=2, )

#  calculate padding with percentage value. Done
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
padx = int(width * 2 / 100)
pady = int(height * 5 / 100)
div.pack(fill="both", pady=pady, padx=padx)
# img  für user login Done
img = Image.open("user.png").resize((150, 150))
photo = ImageTk.PhotoImage(img)

label_img = ttk.Label(div, image=photo)
label_img.grid(row=0, column=1, sticky="n")

# Full Name  label
fullName_L = ttk.Label(div, text="Full Name:", font=font_Label)
fullName_L.grid(row=1, column=0, sticky="ne", pady=10)

fullName_eny = ttk.Entry(div)
fullName_eny.grid(row=1, column=1, sticky="we", pady=10)

# User Name L&eny
username_label = ttk.Label(div, text="Username: ", font=font_Label)
username_label.grid(row=2, column=0, sticky="ne", pady=10)

username_eny = ttk.Entry(div)
username_eny.grid(row=2, column=1, sticky="we", pady=10)

# Password label
password_L = ttk.Label(div, text="Password: ", font=font_Label)
password_L.grid(row=4, column=0, sticky="ne", pady=10)
password_eny = ttk.Entry(div)
password_eny.grid(row=4, column=1, sticky="we", pady=10)
passGenerator_btn = ttk.Button(div, text="Password Generator")
passGenerator_btn.grid(row=4, column=2, sticky="w", pady=10)

# Enter the password again
password_L_2 = ttk.Label(div,text="Password-Again: ",font=font_Label)
password_L_2.grid(row=6,column=0,sticky="ne",pady=10)
password_eny_2 = ttk.Entry(div)
password_eny_2.grid(row=6,column=1,sticky="we",pady=10)

# save date button
login_btn = ttk.Button(div, text="Register")
login_btn.grid(row=8, column=1, pady=20, sticky="n")

root.mainloop()
