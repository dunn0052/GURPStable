from tkinter import *
from GURPSCharacter import *

class CWindow(Frame):
    name = ""
    def __init__(self, master=None, name = ""):
        self.name = name
        Frame.__init__(self, master)
        self.CinitWindow()
       

    def CinitWindow(self):
        #Player Data
        self.player = GURPSCharacter(name = self.name)

        #set title
        self.title = self.player.fluff["Name"][0] + " - " + self.player.fluff["Player"][0]
        self.master.title(self.title)
        self.displayCharacter()
        
        
    # format stat item
    def displayStat(self, stat, value, grid_row, grid_column, justification = "nw", bg_color = None, font = None):
        Label(self.master, text = stat + ": " + str(value), anchor = justification, bg = bg_color, font = font).grid(row = grid_row, column = grid_column)

    def displayCharacter(self):
        p = self.player.stat
        # directed display because dictionaries have no set order
        self.displayStat("ST", p["ST"][0], 0, 1)
        self.displayStat("DX", p["DX"][0], 1, 1)
        self.displayStat("IQ", p["IQ"][0], 2, 1)
        self.displayStat("HT", p["HT"][0], 3, 1)
        self.displayStat("HP", p["ST"][0], 0, 2)
        self.displayStat("WILL", p["ST"][0], 1, 2)
        self.displayStat("PER", p["ST"][0], 2, 2)
        self.displayStat("FP", p["ST"][0], 3, 2)

        self.displayStat("Name", self.player.fluff["Name"][0], 0, 0, font = "bold")
        self.displayStat("Player", self.player.fluff["Player"][0], 1, 0, font = "bold")
        
        Label(self.master, text = "Advantages and Perks", font = "bold").grid(row=4, column=0)
        adv_offset = self.displayAllStat(row = 5, column = 0, dictionary = self.player.advantage)
        perk_offset = self.displayAllStat(row = 5, column = 0, dictionary = self.player.perk, offset = adv_offset)
        Label(self.master, text = "Disadvantages and Quirks", font = "bold").grid(row=5+ perk_offset, column=0)
        dis_offset = self.displayAllStat(row = 6, column = 0, dictionary = self.player.disadvantage, offset = perk_offset)
        self.displayAllStat(row = 6, column = 0, dictionary = self.player.quirk, offset = dis_offset)

        Label(self.master, text = "Skills", font = "bold").grid(row = 4, column = 1)
        self.displayAllStat(row = 5, column = 1, dictionary = self.player.skill)

        Label(self.master, text = "Weapons, Armor, and Items", font = "bold").grid(row = 4, column = 2)
        wpn_offset = self.displayAllStat(row = 5, column = 2, dictionary = self.player.weapon)
        arm_offset =self.displayAllStat(row = 5, column = 2, dictionary = self.player.armor, offset = wpn_offset)
        self.displayAllStat(row = 5, column = 2, dictionary = self.player.item, offset = arm_offset)
        
    def displayAllStat(self, row, column, dictionary, offset = 0, font = None):
        offset = offset
        for item in dictionary:
            Label(self.master, text = item).grid(row = row + offset, column = column, font = font)
            offset +=1
        return offset

#begin window
def runCWindow(Croot = None, name = None):
    app = CWindow(master=Croot, name = name)
    Croot.mainloop()
