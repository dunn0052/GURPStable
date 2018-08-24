# Gurps Character instance
import crw

class GURPSCharacter:
    def __init__(self):
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
        #temp test points
        self.point = 125

        
    def loadCharacter(self, path = "data/characters/", name = None):
        # character data init - get char data by name folder
        self.setData(path + name + "/Stats", self.stat)
        self.setData(path + name + "/Items", self.item)
        self.setData(path + name + "/Armor", self.armor)
        self.setData(path + name + "/Weapons", self.weapon)
        self.setData(path + name + "/Advantages", self.advantage)
        self.setData(path + name + "/Perks", self.perk)
        self.setData(path + name + "/Disadvantages", self.disadvantage)
        self.setData(path + name + "/Quirks", self.quirk)
        self.setData(path + name + "/Skills", self.skill)
        self.setData(path + name + "/Fluff", self.fluff)

    # read data from csv - name as key, list value as val
    # header true => read first row
    def setData(self, path, dictionary, header = False):
        temp = crw.getData(path)
        for item in temp[not header:]:
            dictionary[item[0]] = item[1:]    

    # stat2 goes up with stat1 if defined
    def adjSTAT(self, file, stat1, stat2 = None, value = 1, free = False):
        # grabs row data
        tmp1 = crw.findData(file, stat1)
        self.stat[stat1][0] += value
        #deduct point cost based on value or add if removed
        if not free:
            self.point -= value*int(tmp1[2])
        if stat2 != None:
            self.stat[stat2][0] += value
        return True # could be used in a button lambda
