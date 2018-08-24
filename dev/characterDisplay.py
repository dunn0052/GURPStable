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
        #tracker holds text variable reference
        # self.tracker[stat] = [textvariable, label reference]
        self.tracker = {}
        #self.displayCharacter()
        self.editCharacter()
           
        
    # format stat item
    def displayStat(self, stat, value, grid_row, grid_column, justification = "nw", bg_color = None, font = None):
        text = StringVar()
        text.set(stat + ": " + str(value))
        self.tracker[stat] = [text]  
        L = Label(self.master, textvariable=self.tracker[stat][0], anchor = justification, bg = bg_color, font = font)
        # .grid after declaration so info can be displayed
        L.grid(row = grid_row, column = grid_column)
        self.tracker[stat].append(L)
        return True

    def displayAllStat(self, row, column, dictionary, offset = 0, font = None):
        offset = offset
        for item in dictionary:
            Label(self.master, text = item).grid(row = row + offset, column = column, font = font)
            offset +=1
        return offset

    def updateStatDisplay(self, path, stat1, stat2 = None, value = 1, free = False):
        #actually changes character stats
        self.player.adjSTAT(path, stat1, stat2, value, free = free)
        print(self.player.stat["POINTS"][0])
        # changes displayed stats
        self.tracker[stat1][0].set(stat1 +": " + str(self.player.stat[stat1][0]))
        if stat2 != None:
            self.tracker[stat2][0].set(stat2 +": " + str(self.player.stat[stat2][0]))
        return True # could be used in lambda button

    def plusButton(self, stat1, stat2, value, row, column, path = "data\characters\BASE\Stats" ):
        # could pass reference to master to make funciton more generic
        Button(self.master, text ="+", command = lambda: self.updateStatDisplay(path, stat1, stat2, value)).grid(row = row, column = column)

    def minusButton(self, stat1, stat2, value, row, column, path = "data\characters\BASE\Stats" ):
        Button(self.master, text ="-", command = lambda: self.updateStatDisplay(path, stat1, stat2, value)).grid(row = row, column = column)       
        
    def adjustButtons(self, stat1, stat2, value, path = "data\characters\BASE\Stats"):
        # grab label coordinates to display buttons around label, jfc
        self.plusButton(stat1, stat2, value, self.tracker[stat1][1].grid_info()["row"], self.tracker[stat1][1].grid_info()["column"]+1, path)
        self.minusButton(stat1, stat2, -value, self.tracker[stat1][1].grid_info()["row"], self.tracker[stat1][1].grid_info()["column"]-1, path)
        
    def displayCharacter(self):
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
        self.adjustButtons("ST", "HP", 1)
        self.displayStat("DX", p["DX"][0], 1, 1)
        self.adjustButtons("DX", stat2 = None, value = 1)
        
        self.displayStat("IQ", p["IQ"][0], 2, 1)
        # Manually adjust IQ since adjustButtons only moves 1 extra stat
        Button(self.master, text ="+", command = lambda: self.updateStatDisplay(path = "data\characters\BASE\Stats", stat1 = "IQ", stat2 = "PER", value = 1) and self.updateStatDisplay(path = "data\characters\BASE\Stats", stat1 = "WILL", stat2 = None, value = 1, free = True)).grid(row = 2, column = 2)
        Button(self.master, text ="-", command = lambda: self.updateStatDisplay(path = "data\characters\BASE\Stats", stat1 = "IQ", stat2 = "PER", value = -1) and self.updateStatDisplay(path = "data\characters\BASE\Stats", stat1 = "WILL", stat2 = None, value = -1, free = True)).grid(row = 2, column = 0)

        self.displayStat("HT", p["HT"][0], 3, 1)
        self.adjustButtons("HT", "FP", 1)
        self.displayStat("HP", p["HP"][0], 0, 4)
        self.adjustButtons("HP", stat2 = None, value = 1)
        self.displayStat("WILL", p["WILL"][0], 1, 4)
        self.adjustButtons("WILL", stat2 = None, value = 1)
        self.displayStat("PER", p["PER"][0], 2, 4)
        self.adjustButtons("PER", stat2 = None, value = 1)
        self.displayStat("FP", p["FP"][0], 3, 4)
        self.adjustButtons("FP", stat2 = None, value = 1)
        self.displayStat("SPEED", p["SPEED"][0], 4, 1)
        self.adjustButtons("SPEED", stat2 = None, value = 0.25)
        self.displayStat("MOVE", p["MOVE"][0], 4, 4)
        self.adjustButtons("MOVE", stat2 = None, value = 1)

        #fluff corner
        self.displayStat("Name", self.player.fluff["Name"][0], grid_row = 0, grid_column = 6, font = "bold")
        self.displayStat("Player", self.player.fluff["Player"][0], grid_row = 1, grid_column = 6, font = "bold")
            
#begin window
def runCWindow(Croot = None, character = None):
    app = CWindow(master=Croot, character = character)
    Croot.mainloop()

# test edit interface
c = GURPSCharacter()
c.loadCharacter(name = "test", header = True)
c.saveCharacter(name = c.fluff["Name"][0])
runCWindow(Tk(), c)

