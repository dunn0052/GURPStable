from tkinter import *
from GURPSCharacter import *

class CWindow(Frame):
    def __init__(self, master=None, character = None):
        Frame.__init__(self, master)
        self.CinitWindow(character)
       

    def CinitWindow(self, character):
        #set title
        self.player = character
        # if set to new char prompt for name
        self.title = self.player.fluff["Name"][0] + " - " + self.player.fluff["Player"][0]
        self.master.title(self.title)
        self.tracker = {}
        #self.displayCharacter()
        self.editCharacter()
        
        
        
    # format stat item
    def displayStat(self, stat, value, grid_row, grid_column, justification = "nw", bg_color = None, font = None):
        text = StringVar()
        text.set(stat + ": " + str(value))
        self.tracker[stat] = text  
        Label(self.master, textvariable=self.tracker[stat], anchor = justification, bg = bg_color, font = font).grid(row = grid_row, column = grid_column)
    # 
    def displayAllStat(self, row, column, dictionary, offset = 0, font = None):
        offset = offset
        for item in dictionary:
            Label(self.master, text = item).grid(row = row + offset, column = column, font = font)
            offset +=1
        return offset


    def updateStatDisplay(self, path, stat1, stat2 = None, variable = 1):
        self.player.adjSTAT(path, stat1, stat2, variable)
        self.tracker[stat1].set(stat1 +": " + str(self.player.stat[stat1][0]))
        if stat2 != None:
            self.tracker[stat2].set(stat2 +": " + str(self.player.stat[stat2][0]))
        return True # could be used in lambda button

    def plusButton(self, stat1, stat2, value):
        return
        
    def displayCharacter(self):
        p = self.player.stat
        # directed display because dictionaries have no set order
        self.displayStat("ST", p["ST"][0], 0, 1)
        self.displayStat("DX", p["DX"][0], 1, 1)
        self.displayStat("IQ", p["IQ"][0], 2, 1)
        self.displayStat("HT", p["HT"][0], 3, 1)
        self.displayStat("HP", p["HP"][0], 0, 2)
        self.displayStat("WILL", p["WILL"][0], 1, 2)
        self.displayStat("PER", p["PER"][0], 2, 2)
        self.displayStat("FP", p["FP"][0], 3, 2)

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
        
    def editCharacter(self):
        p = self.player.stat
        # directed display because dictionaries have no set order
        self.displayStat("ST", p["ST"][0], 0, 1)
        self.displayStat("DX", p["DX"][0], 1, 1)
        self.displayStat("IQ", p["IQ"][0], 2, 1)
        self.displayStat("HT", p["HT"][0], 3, 1)
        self.displayStat("HP", p["HP"][0], 0, 3)
        self.displayStat("WILL", p["WILL"][0], 1, 3)
        self.displayStat("PER", p["PER"][0], 2, 3)
        self.displayStat("FP", p["FP"][0], 3, 3)
        Button(self.master, text ="+", command = lambda:self.updateStatDisplay("data\characters\BASE\Stats", "ST", "HP", 1)).grid(row = 0, column = 2)
        Button(self.master, text ="-", command = lambda:self.updateStatDisplay("data\characters\BASE\Stats", "ST", "HP", -1)).grid(row = 0, column = 0)         

#begin window
def runCWindow(Croot = None, character = None):
    app = CWindow(master=Croot, character = character)
    Croot.mainloop()


c = GURPSCharacter()
c.loadCharacter(name = "test")
runCWindow(Tk(), c)
