# Gurps Character instance
import crw

class GURPSCharacter:
    def __init__(self):
        self.stat = {}
        self.item = {}
        self.advantage = {}
        self.perk = {}
        self.disadvantage = {}
        self.quirk = {}
        self.skill = {}
        self.fluff = {}

        #character data init
        self.setData("data/newStats", self.stat)
        self.setData("data/newItems", self.item)
        self.setData("data/newAdvantages", self.advantage)
        self.setData("data/newPerks", self.perk)
        self.setData("data/newDisadvantages", self.disadvantage)
        self.setData("data/newQuirks", self.quirk)
        self.setData("data/newSkills", self.skill)
        self.setData("data/newFluff", self.fluff)

    def setData(self, path, dictionary, header = False):
        temp = crw.getData(path)
        for item in temp[not header:]:
            dictionary[item[0]] = item[1:]
