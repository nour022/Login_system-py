import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("500x500")
menu = tk.Frame(root)
menu.config(background="#334257")
menu.pack(fill="both", )

label1 = ttk.Label(menu, text="Logo", background="#334257", foreground="#fff")
label1.pack(side="left", pady=10, padx=30)
label_wg = ttk.Label(menu, text="Einkaufswagen", background="#334257", foreground="#fff")
label_wg.pack(side="right", pady=10, padx=30)

body = tk.Frame(root)
body.pack(fill="both", padx=30)

cards = tk.Frame(body)
cards.pack()

card_img = Image.open("user.png").resize((160, 160))
photo = ImageTk.PhotoImage(card_img)
for r in range(0, 4):
    for i in range(0, 1):
        card = tk.Frame(cards)
        card.grid(column=i, row=r)

        img_label = tk.Label(card, image=photo)
        img_label.pack()
        card_name = tk.Label(card, text="Name")
        card_name.pack()
        card_BS = tk.Label(card, text="Lorem ipsum dolor, sit amet consectetur adipisicing elit!")
        card_BS.pack()
        card_PR = tk.Label(card, text="$152000")
        card_PR.pack()
        card_btn = ttk.Button(card, text="Add to cart")
        card_btn.pack()

# def test(e):
#     body.pack_forget()
# label2 = tk.Label(body,text="Main",)
# label2.pack()
# label2.bind("<Button 1>",func=test)


footer = tk.Frame(root)
footer.pack(fill="both")
footer.config(background="#334257")

label3 = tk.Label(footer, text="footer", background="#334257", foreground="#fff")
label3.pack(pady=10, padx=10)

root.mainloop()
