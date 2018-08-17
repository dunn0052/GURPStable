import tkinter as tk
import GURPSCharacter

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.init_window()

    def init_window(self):
        self.player = GURPSCharacter.GURPSCharacter()
        
root = tk.Tk()
app = Window(master=root)
root.mainloop()
