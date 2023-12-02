import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def create_scroll_frame():
    # Create the root window
    root = tk.Tk()
    root.geometry("500x500")

    # Create the menu frame
    menu = tk.Frame(root)
    menu.config(background="#334257")
    menu.pack(fill="both")

    # Create labels for the menu
    label1 = ttk.Label(menu, text="Logo", background="#334257", foreground="#fff")
    label1.pack(side="left", pady=10, padx=30)
    label_wg = ttk.Label(menu, text="Einkaufswagen", background="#334257", foreground="#fff")
    label_wg.pack(side="right", pady=10, padx=30)

    # Create a Scrollbar frame
    scroll_frame = ttk.Frame(root)
    scroll_frame.pack(fill=tk.BOTH, expand=True)

    # Create a Canvas for the Scroll Frame
    canvas = tk.Canvas(scroll_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Create a Scrollbar for the Canvas
    scrollbar = ttk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Connect the Scrollbar to the Canvas
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    # Create a Frame inside the Canvas for the content
    content_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=content_frame, anchor=tk.NW)

    # Set the desired width of the content frame
    content_frame.configure(width=800, padding=[200, 10])

    # Add content to the frame (example with Labels)
    card_img = Image.open("user.png").resize((160, 160))
    photo = ImageTk.PhotoImage(card_img)
    for r in range(0, 6):
        for i in range(0, 3):
            card = tk.Frame(content_frame)
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

    # Uncomment the following code to add additional labels to the content frame
    # for i in range(50):
    #     label = ttk.Label(content_frame, text=f"Inhalt {i}")
    #     label.pack(pady=10)

    # Update the Canvas to display the correct area
    canvas.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))

    # Create the footer frame
    footer = tk.Frame(root)
    footer.pack(fill="both")
    footer.config(background="#334257")

    # Create a label for the footer
    label3 = tk.Label(footer, text="footer", background="#334257", foreground="#fff")
    label3.pack(pady=10, padx=10)

    # Start the main loop of the window
    root.mainloop()

# Call the function to create the scroll frame
create_scroll_frame()
