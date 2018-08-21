#GM party cascade functions
from characterDisplay import *
from GURPSCharacter import GURPSCharacter
from tkinter import *


# window is tk GM control window
# app reference GM window items

# party controls
def newParty(app):
    #clears party ?
    app.party = []

def addMember(window, app):
    load_window_f(window, app)
    
def removeMember(window):
    return
    
def displayParty(window, app):
    # bug or feature? Party members must have unique names?
    # each Tk() instance might have to be a seperate reference -- prob not
    for player in app.party:
        runCWindow(Tk(), character = player)


#Window Functions
def load_window_f(window, app):
    load_window = window.load_window= Toplevel(window)
    window.load_window_entry = Entry(window.load_window)
    window.load_window_entry.grid(row=0,column=0, columnspan = 2)
    window.load_window_button = Button(window.load_window, text="Load", command=lambda: load_char(window, app))
    window.load_window_button.grid(row=1,column=0)
    window.load_cancel_button = Button(window.load_window, text ="Cancel", command=load_window.destroy)
    window.load_cancel_button.grid(row=1,column=1)

def load_char(window,app, name = None):
    window.load_window.transient(window)
    #self.reset_root(bg_keep = True)
    try:
        Member = GURPSCharacter()
        Member.loadCharacter(name = str(window.load_window_entry.get()))
        app.party.append(Member)
    except:
        error_window_popup(root = window, window = window.load_window, error_message = ("Could not find " + window.load_window_entry.get()))
        return
    window.load_window.withdraw()

def error_window_popup(root, window, error_message = "", parent_close = False):
        error_window = root.error_window = Toplevel(window)
        root.error_label = Label(root.error_window, text = error_message).grid(row=0,column=0)
        if not parent_close:
            root.error_ok_button = Button(root.error_window, text = "Ok", command=root.error_window.withdraw).grid(row=1,column=0)
        elif parent_close:
            root.error_ok_button = Button(root.error_window, text = "Ok", command=lambda: root.error_window.withdraw() or window.withdraw()).grid(row=1,column=0)
            # black magic -- or runs each function to determine any is true

#clears original window of any widgets
def reset_root(self, bg_keep = False):
    list = root.grid_slaves()
    for l in list:
        if bg_keep and l == bg:
            continue
        else:
            l.destroy()

