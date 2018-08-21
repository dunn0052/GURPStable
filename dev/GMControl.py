# GM control window
# app => GM window reference for items, party, encounters etc...
# self.master Tk() object for window reference

from characterDisplay import *
from GURPSCharacter import GURPSCharacter
from tkinter import *

from GMfileCascade import *
from GMpartyCascade import *

class GMWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.GMinitWindow()

    def GMinitWindow(self):
        self.master.title("GM Control")
        menu = Menu(root)
        root.config(menu=menu)

# party hold references to members
# encounters hold party references of combatants
        self.party = []
        self.encounters = [[]]

# Cascade menus
        self.fileMenu(menu)
        self.partyMenu(menu)
        self.encounterMenu(menu)
        self.battleMenu(menu)
        self.mapMenu(menu)
##      self.helpMenu()

# cascade options -- functions loaded through each function file
# fill in functions as you go along

# Since buttons demand a no argument function
# you can pass a default argument by embedding it into a lambda
# multiple functions can be run by logical short circuts
# string with and while each function returns True

    def fileMenu(self, menu):
        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=None)
        filemenu.add_command(label="Open", command=None)
        filemenu.add_command(label="Save", command=None)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=lambda : clientExit(self.master))

    def partyMenu(self, menu):
        partymenu = Menu(menu)
        menu.add_cascade(label="Party", menu=partymenu)
        partymenu.add_command(label="Add Member", command=lambda : addMember(self.master, app))
        partymenu.add_command(label="Display Party", command=lambda : displayParty(self.master, app))
        partymenu.add_command(label="New", command=lambda : newParty(app))
        partymenu.add_command(label="Open", command=None)
        partymenu.add_command(label="Save", command=None)

    def battleMenu(self, menu):
        battlemenu = Menu(menu)
        menu.add_cascade(label="Battle", menu=battlemenu)
        battlemenu.add_command(label="Begin Battle", command=None)
        battlemenu.add_command(label="End Battle", command=None)

    def mapMenu(self, menu):
        mapmenu = Menu(menu)
        menu.add_cascade(label="Map", menu=mapmenu)
        mapmenu.add_command(label="New Map", command=None)
        mapmenu.add_command(label="Open Map", command=None)

    def encounterMenu(self, menu):
        encountermenu = Menu(menu)
        menu.add_cascade(label="Encounter", menu=encountermenu)
        encountermenu.add_command(label="New Encounter", command=None)
        encountermenu.add_command(label="Open Encounter", command=None)
        encountermenu.add_command(label="Save Encounter", command=None)

##    def helpMenu(self, menu = menu):
##        helpmenu = Menu(menu)
##        menu.add_cascade(label="Help", menu=helpmenu)
##        helpmenu.add_command(label="About", command=None)       

        
#begin window 
root = Tk()
app = GMWindow(master=root)
root.mainloop()
