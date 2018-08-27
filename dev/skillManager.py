#skill manager

import crw
from GURPSCharacter import *

# calculate skill level from character point in skill, character stat and skill modifer tables
def getSkill(character, skill):
    skillPoints = character.skill[skill][0]#get point value of the skill
    print(skillPoints)
    skillData = crw.findData(file = "data/characters/BASE/Skills", name = skill) # find base skill entry
    print(skillData)
    skillTable = crw.findData(file = "data/characters/BASE/SkillCost", name = skillData[2]) # find difficulty of skill
    print(skillTable)
    try:
        if skillPoints > skillTable[9]:
            return 5 + (skillPoints - skillTable[9])/4 + character.stat[skillData[1]][0] # if off the chart
        return skillTable.index(skillPoints) - 4 + character.stat[skillData[1]][0] #gives skill modifier
        print("success")
    except:
        print("not found")

