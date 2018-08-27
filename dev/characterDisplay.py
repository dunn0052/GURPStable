from tkinter import *
from GURPSCharacter import *
import skillManager

class CWindow(Frame):
    def __init__(self, master=None, character = None):
        Frame.__init__(self, master)
        self.CinitWindow(character)
       

    def CinitWindow(self, character):
        #set title
        self.player = character
        # if set to new char prompt for name
        #self.title = self.player.fluff["Name"][0] + " - " + self.player.fluff["Player"][0]
        #self.master.title(self.title)
        #tracker holds text variable reference
        # self.tracker[stat] = [textvariable, label reference]
        self.tracker = {}
        self.displayCharacter()
        #self.newCharacter()
        #self.editCharacter()
           
        
    # format stat item
    def displayStat(self, stat, value, grid_row, grid_column, justification = "w", bg_color = None, font = None):
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
            self.displayStat(stat = item, value = dictionary[item][0], grid_row = row + offset, grid_column = column, font = font)
            offset +=1
        return offset

    def displayAllSkills(self, row, column, dictionary, offset = 0, font = None):
        offset = offset
        for item in dictionary:
            self.displayStat(stat = item, value = skillManager.getSkill(self.player, item), grid_row = row + offset, grid_column = column, font = font)
            offset +=1
        return offset

    def displayAP(self, row, column):
        Label(self.master, text = "Advantages and Perks", font = "bold").grid(row=row, column=column)
        adv_offset = self.displayAllStat(row = row+1, column = column, dictionary = self.player.advantage)
        perk_offset = self.displayAllStat(row = row+1, column = column, dictionary = self.player.perk, offset = adv_offset)
        Label(self.master, text = "Disadvantages and Quirks", font = "bold").grid(row=row+ perk_offset, column=0)
        dis_offset = self.displayAllStat(row = row+1, column = column, dictionary = self.player.disadvantage, offset = perk_offset)
        self.displayAllStat(row = row+1, column = column, dictionary = self.player.quirk, offset = dis_offset)

    def displaySkills(self, row, column):
        Label(self.master, text = "Skills", font = "bold").grid(row = row, column = column)
        self.displayAllSkills(row = row + 1, column = column, dictionary = self.player.skill)

    def displayInventory(self, row, column):
        Label(self.master, text = "Weapons, Armor, and Items", font = "bold").grid(row = row, column = column)
        wpn_offset = self.displayAllStat(row = row+1, column = column, dictionary = self.player.weapon)
        arm_offset =self.displayAllStat(row = row+1, column = column, dictionary = self.player.armor, offset = wpn_offset)
        self.displayAllStat(row = row+1, column = column, dictionary = self.player.item, offset = arm_offset)        

    def updateStatDisplay(self, path, stat1, stat2 = None, value = 1, free = False):
        #actually changes character stats
        self.player.adjSTAT(path, stat1, stat2, value, free = free)
        self.tracker["Points"][0].set("Points" + ": " + str(self.player.stat["POINTS"][0]))
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
        self.displayStat("HP", p["HP"][0], 0, 2)
        self.displayStat("WILL", p["WILL"][0], 1, 2)
        self.displayStat("PER", p["PER"][0], 2, 2)
        self.displayStat("FP", p["FP"][0], 3, 2)
        self.displayStat("SPEED", p["SPEED"][0], 4, 1)
        self.displayStat("MOVE", p["MOVE"][0], 4, 2) 
        self.displayStat("Name", self.player.fluff["Name"][0], 0, 0, font = "bold")
        self.displayStat("Player", self.player.fluff["Player"][0], 1, 0, font = "bold")
        self.displayStat("Points", self.player.fluff["POINTS"][0], 2, 0, font = "bold")
        
        self.displayAP(row = 5, column = 0)
        self.displaySkills(row = 5, column = 1)
        self.displayInventory(row = 5, column = 2)



        
    def editCharacter(self):
        p = self.player.stat
        # directed display because dictionaries have no set order
        self.displayStat("Points", self.player.stat["POINTS"][0], grid_row = 2, grid_column = 6, font = "bold")
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
        return True

    def newCharacter(self):
        self.player = GURPSCharacter()
        self.player.loadCharacter(name = "New", header = True)
        self.enterName()
   

    def enterName(self):
        # enterName -> enterPoints -> editCharacter
        n = Tk()
        enterName = Entry(n)
        enterName.insert(0, "Enter Name")
        enterName.bind("<Button-1>", lambda x: enterName.delete(0, "end"))
        enterName.grid(row = 0, column = 0, columnspan = 2)
        cancel = Button(n, text = "Cancel", command = lambda: n.destroy())
        cancel.grid(row = 1, column = 0)
        # hack that button because .destroy() doesn't return True
        okay = Button(n, text = "Ok", command = lambda: self.getName(enterName) and n.destroy())
        okay.grid(row = 1, column = 1)
        # run the popup to the topup
        n.attributes('-topmost', True)

    def getName(self, entry):
        self.player.fluff["Name"][0] = entry.get()
        self.enterPoints()
        return True

    def enterPoints(self):
        n = Tk()
        enterPoints = Entry(n)
        enterPoints.insert(0, "Enter Points")
        enterPoints.bind("<Button-1>", lambda x: enterPoints.delete(0, "end"))
        enterPoints.grid(row = 0, column = 0, columnspan = 2)
        cancel = Button(n, text = "Cancel", command = lambda: n.destroy())
        cancel.grid(row = 1, column = 0)
        # hack that button because .destroy() doesn't return True
        okay = Button(n, text = "Ok", command = lambda: self.getPoints(enterPoints) and n.destroy())
        okay.grid(row = 1, column = 1)
        # run the popup to the topup
        n.attributes('-topmost', True)

    def getPoints(self, entry):
        self.player.stat["POINTS"][0] = int(entry.get())
        self.editCharacter()
        return True
        
#begin window
def runCWindow(Croot = None, character = None):
    app = CWindow(master=Croot, character = character)
    Croot.mainloop()

# test edit interface
c = GURPSCharacter()
c.loadCharacter(name = "test", header = True)
#c.saveCharacter(name = c.fluff["Name"][0])
runCWindow(Tk(), c)

