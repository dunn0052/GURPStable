# Player window
from tkinter import *
from GURPSCharacter import *
from PfileCascade import *

class PWindow(Frame):
    def __init__(self, master = None):
        Frame.__init__(self,master)
        self.PinitWindow()

    def PinitWindow(self):
        self.master.title("Player Control")
        menu = Menu(Proot)
        Proot.config(menu=menu)
        self.fileMenu(menu)

    def fileMenu(self, menu):
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=Pnew)
        filemenu.add_command(label="Open", command=Popen)
        filemenu.add_command(label="Save", command=Psave)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda : clientExit(self.master))

#begin window
Proot = Tk()
papp = PWindow(master = Proot)
Proot.mainloop()
