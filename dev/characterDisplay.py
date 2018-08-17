from tkinter import *
from GURPSCharacter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.init_window()

    def init_window(self):
        #Player Data
        self.player = GURPSCharacter()

        #set title
        self.title = self.player.fluff["Name"][0] + " - " + self.player.fluff["Player"][0]
        self.master.title(self.title)

        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=None)
        filemenu.add_command(label="Open", command=None)
        filemenu.add_command(label="Save", command=None)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.client_exit)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=None)


    def client_exit(self):
        self.master.destroy()
        #exit()
        
#begin window 
root = Tk()
app = Window(master=root)
root.mainloop()
