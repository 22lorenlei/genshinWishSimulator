#for the wanderlustInvocation banner
import random

fiveStarCharacters = ["Jean", "Qiqi", "Tighnari", "Keqing", "Mona", "Dehya", "Diluc"]
fiveStarWeapons = ["Amos' Bow", "Skyward Harp", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Skyward Pride", "Wolf's Gravestone", "Primordial Jade Winged-Spear", "Skyward Spine", "Aquila Favonia", "Skyward Blade"]

def chanceCalculator():
    chance = random.randint(1, 1001)

    #For five stars (1.6 percent)
    if 0 < chance < 17:
        return "5 star"+str(chance)
    #For four stars (13 percent)
    elif 18 < chance < 149:
        return "4 star"+str(chance)
    #Everything else (86.4 percent)
    else:
        return "3 star"+str(chance)
