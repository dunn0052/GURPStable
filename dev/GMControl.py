from characterDisplay import *
from GURPSCharacter import GURPSCharacter
from tkinter import *

class GMWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.GMinitWindow()

    def GMinitWindow(self):
        self.master.title("GM Control")
        menu = Menu(root)
        root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=None)
        filemenu.add_command(label="Open", command=None)
        filemenu.add_command(label="Save", command=None)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.clientExit)

        partymenu = Menu(menu)
        menu.add_cascade(label="Party", menu=partymenu)
        partymenu.add_command(label="Add Member", command=self.AddMember)
        partymenu.add_command(label="Display Party", command=self.DisplayParty)
        partymenu.add_command(label="New", command=self.NewParty)
        partymenu.add_command(label="Open", command=None)
        partymenu.add_command(label="Save", command=None)

        helpmenu = Menu(menu)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About", command=None)

        self.party = []


    def clientExit(self):
        self.master.destroy()
        #exit()

    # party controls
    def NewParty(self):
        self.party = []

    def AddMember(self):
        self.load_window_f()
        
    def DisplayParty(self):
        runCWindow(Tk())
        return
    

    #Window Functions
    def load_window_f(self):
        load_window = self.load_window= Toplevel(self.master)
        self.load_window_entry = Entry(self.load_window)
        self.load_window_entry.grid(row=0,column=0, columnspan = 2)
        self.load_window_button = Button(self.load_window, text="Load", command=self.load_char)
        self.load_window_button.grid(row=1,column=0)
        self.load_cancel_button = Button(self.load_window, text ="Cancel", command=self.load_window.destroy)
        self.load_cancel_button.grid(row=1,column=1)

    def load_char(self, name = None):
        self.load_window.transient(self.master)
        #self.reset_root(bg_keep = True)
        try:
            Member = GURPSCharacter(name = str(self.load_window_entry.get()))
            self.party.append(Member)
            print(self.party)
        except:
            self.error_window_popup(window = self.load_window, error_message = ("Could not find " + self.load_window_entry.get()))
            return
        self.load_window.withdraw()

    def error_window_popup(self, window, error_message = "", parent_close = False):
            error_window = self.error_window = Toplevel(window)
            self.error_label = Label(self.error_window, text = error_message).grid(row=0,column=0)
            if not parent_close:
                self.error_ok_button = Button(self.error_window, text = "Ok", command=self.error_window.withdraw).grid(row=1,column=0)
            elif parent_close:
                self.error_ok_button = Button(self.error_window, text = "Ok", command=lambda: self.error_window.withdraw() or window.withdraw()).grid(row=1,column=0)
                # black magic -- or runs each function to determine any is true

    def reset_root(self, bg_keep = False):
        list = root.grid_slaves()
        for l in list:
            if bg_keep and l == bg:
                continue
            else:
                l.destroy()

#begin window 
root = Tk()
app = GMWindow(master=root)
root.mainloop()
