import tkinter as tk
from LoginFrame import LoginFrame
from RegisterFrame import RegisterFrame

# Style
font_h1 = ("Helvetica", 25, "bold")
font_Label = ("Helvetica", 14)
font_color = "red"


class Hauptfenster(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Anmeldung und Registrierung")
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.padx = int(width * 2 / 100)
        self.pady = int(height * 5 / 100)
        self.login_frame = LoginFrame(self)
        self.register_frame1 = RegisterFrame(self)

        self.current_frame = self.login_frame
        self.current_frame.pack(fill="both", pady=self.pady, padx=self.padx)
    

    def switch_to_login(self,e):
        self.current_frame.pack_forget()
        self.current_frame = self.login_frame
        self.current_frame.pack(fill="both", pady=self.pady, padx=self.padx)

    def switch_to_register1(self,e):
        self.current_frame.pack_forget()
        self.current_frame = self.register_frame1
        self.current_frame.pack()

  

# Erstelle eine Instanz der Hauptklasse
hauptfenster = Hauptfenster()

# Starte die Hauptloop des Hauptfensters
hauptfenster.mainloop()
