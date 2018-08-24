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


    def loadCharacter(self, path = "data/characters/", name = None):
        # character data init - get char data by name folder
        self.loadData(path + name + "/Stats", self.stat)
        self.loadData(path + name + "/Items", self.item)
        self.loadData(path + name + "/Armor", self.armor)
        self.loadData(path + name + "/Weapons", self.weapon)
        self.loadData(path + name + "/Advantages", self.advantage)
        self.loadData(path + name + "/Perks", self.perk)
        self.loadData(path + name + "/Disadvantages", self.disadvantage)
        self.loadData(path + name + "/Quirks", self.quirk)
        self.loadData(path + name + "/Skills", self.skill)
        self.loadData(path + name + "/Fluff", self.fluff)

    def saveCharacter(self, path = "data/characters/saveTest/", name = None):
        #fix save to load all data
        crw.setData(path = path, name = "Stats", data = self.formatCharacter(self.stat))
        return

    def formatCharacter(self, dictionary):
        n = []
        for name in dictionary:
            n.append([name] + dictionary[name])
        return n

    # read data from csv - name as key, list value as val
    # header true => read first row
    def loadData(self, path, dictionary, header = False):
        temp = crw.getData(path)
        for item in temp[not header:]:
            dictionary[item[0]] = item[1:]

    # stat2 goes up with stat1 if defined
    def adjSTAT(self, file, stat1, stat2 = None, value = 1, free = False):
        # grabs row data
        tmp1 = crw.findData(file, stat1)
        self.stat[stat1][0] += value
        # point adjust based on value sign -- dumb speed
        if not free:
            if value > 0:
                self.stat["POINTS"][0] -= int(tmp1[2])
            else:
                self.stat["POINTS"][0] += int(tmp1[2])
        if stat2 != None:
            self.stat[stat2][0] += value
        return True # could be used in a button lambda
