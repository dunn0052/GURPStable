# Gurps Character instance
import crw

class GURPSCharacter:
    def __init__(self, name):
        self.stat = {}
        self.item = {}
        self.weapon = {}
        self.armor = {}
        self.advantage = {}
        self.perk = {}
        self.disadvantage = {}
        self.quirk = {}
        self.skill = {}
        self.fluff = {}

        #character data init - get char data by name folder
        self.setData("data/characters/" + name + "/Stats", self.stat)
        self.setData("data/characters/" + name + "/Items", self.item)
        self.setData("data/characters/" + name + "/Armor", self.armor)
        self.setData("data/characters/" + name + "/Weapons", self.weapon)
        self.setData("data/characters/" + name + "/Advantages", self.advantage)
        self.setData("data/characters/" + name + "/Perks", self.perk)
        self.setData("data/characters/" + name + "/Disadvantages", self.disadvantage)
        self.setData("data/characters/" + name + "/Quirks", self.quirk)
        self.setData("data/characters/" + name + "/Skills", self.skill)
        self.setData("data/characters/" + name + "/Fluff", self.fluff)

    #read data from csv - name as key, list value as val
    def setData(self, path, dictionary, header = False):
        temp = crw.getData(path)
        for item in temp[not header:]:
            dictionary[item[0]] = item[1:]    
