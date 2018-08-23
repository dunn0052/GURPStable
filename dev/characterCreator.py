# Character creator

from GURPSCharacter import *
from crw import *
class newChar:
    def __init__(self):
        #init new character with base human stats
        self.char = GURPSCharacter()
        setData("data/characters/BASE/Stats", self.char.stat)
        # test base points
        self.char.point = 125

# stat2 goes up with stat1 if defined
    def adjSTAT(self, file, stat1, stat2 = None, value = 1):
        # grabs row data
        tmp1 = findData(file, stat1)
        self.char.stat[stat1] += value
        #deduct oint cost based on value or add if removed
        self.char.point -= value*int(tmp1[2])
        if stat2 != None:
            self.char.stat[stat2] += value
