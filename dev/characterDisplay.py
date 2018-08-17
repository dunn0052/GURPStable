from tkinter import *
from GURPSCharacter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.initWindow()

    def initWindow(self, name = None):
        #Player Data
        self.player = GURPSCharacter(name = "test")

        #set title
        self.title = self.player.fluff["Name"][0] + " - " + self.player.fluff["Player"][0]
        self.master.title(self.title)
        self.displayCharacter()
        
    # format stat item
    def displayStat(self, stat, value, grid_row, grid_column, justification = "nw", bg_color = None):
        Label(root, text = stat + ": " + str(value), anchor = justification, bg = bg_color).grid(row = grid_row, column = grid_column)

    def displayCharacter(self):
        p = self.player.stat
        # directed display because dictionaries have no set order
        self.displayStat("ST", p["ST"][0], 0, 0)
        self.displayStat("DX", p["DX"][0], 1, 0)
        self.displayStat("IQ", p["IQ"][0], 2, 0)
        self.displayStat("HT", p["HT"][0], 3, 0)
        self.displayStat("HP", p["ST"][0], 0, 1)
        self.displayStat("WILL", p["ST"][0], 1, 1)
        self.displayStat("PER", p["ST"][0], 2, 1)
        self.displayStat("FP", p["ST"][0], 3, 1)

        self.displayStat("Name", self.player.fluff["Name"][0], 0, 2)
        self.displayStat("Player", self.player.fluff["Player"][0], 1, 2)
        
        Label(root, text = "Advantages and Perks").grid(row=4, column=0)
        adv_offset = self.displayAllStat(row = 5, column = 0, dictionary = self.player.advantage)
        perk_offset = self.displayAllStat(row = 5 + adv_offset, column = 0, dictionary = self.player.perk)
        Label(root, text = "Disadvantages and Quirks").grid(row=5 + perk_offset, column=0)
        dis_offset = self.displayAllStat(row = 5 + perk_offset, column = 0, dictionary = self.player.disadvantage)
        self.displayAllStat(row = 5 + dis_offset, column = 0, dictionary = self.player.quirk)

        Label(root, text = "Skills").grid(row = 4, column = 1)
        self.displayAllStat(row = 5, column = 1, dictionary = self.player.skill)

        Label(root, text = "Weapons and Armor").grid(row = 4, column = 2)
        self.displayAllStat(row = 5, column = 1, dictionary = self.player.weapon)
        self.displayAllStat(row = 5, column = 1, dictionary = self.player.armor)
        
    def displayAllStat(self, row, column, dictionary):
        offset = 0
        for item in dictionary:
            self.displayStat(text = item).grid(row = row + offset, column = column)
            offset +=1
        return offset
        
##        work best for GM control
##        menu = Menu(root)
##        root.config(menu=menu)
##        filemenu = Menu(menu)
##        menu.add_cascade(label="File", menu=filemenu)
##        filemenu.add_command(label="New", command=None)
##        filemenu.add_command(label="Open", command=None)
##        filemenu.add_command(label="Save", command=None)
##        filemenu.add_separator()
##        filemenu.add_command(label="Exit", command=self.client_exit)
##
##        helpmenu = Menu(menu)
##        menu.add_cascade(label="Help", menu=helpmenu)
##        helpmenu.add_command(label="About...", command=None)
##
##
##    def client_exit(self):
##        self.master.destroy()
##        #exit()
        
#begin window 
root = Tk()
app = Window(master=root)
root.mainloop()
