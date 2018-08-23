# Character edit window
from tkinter import *
from characterCreator import *
from characterDisplay import *

class CEWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.CEinitWindow()

    def CEinitWindow(self):
        self.player = newChar()
        self.drawStat()
        
    def drawStat(self):
        p = self.player.char.stat
        self.displayStat("ST", p["ST"][0], 0, 1)
        self.displayStat("DX", p["DX"][0], 1, 1)
        self.displayStat("IQ", p["IQ"][0], 2, 1)
        self.displayStat("HT", p["HT"][0], 3, 1)
        self.displayStat("HP", p["ST"][0], 0, 2)
        self.displayStat("WILL", p["ST"][0], 1, 2)
        self.displayStat("PER", p["ST"][0], 2, 2)
        self.displayStat("FP", p["ST"][0], 3, 2)
        
# format stat item (from characterDisplay.py)
    def displayStat(self, stat, value, grid_row, grid_column, justification = "nw", bg_color = None, font = None):
        Label(self.master, text = stat + ": " + str(value), anchor = justification, bg = bg_color, font = font).grid(row = grid_row, column = grid_column)

#begin window
def runCEWindow(CEroot = None):
    app = CEWindow(master=CEroot)
    Croot.mainloop()
