#for the wanderlustInvocation banner
import random

fiveStarCharacters = ["Jean", "Qiqi", "Tighnari", "Keqing", "Mona", "Dehya", "Diluc"]
fiveStarWeapons = ["Amos' Bow", "Skyward Harp", "Lost Prayer to the Sacred Winds", "Skyward Atlas", "Skyward Pride", "Wolf's Gravestone", "Primordial Jade Winged-Spear", "Skyward Spine", "Aquila Favonia", "Skyward Blade"]
fourStarCharacters = ["Faruzan", "Sayu", "Shikanoin Heizou", "Sucrose", "Chongyun", "Diona", "Kaeya", "Layla", "Mika", "Rosaria", "Collei", "Kaveh", "Kirara", "Yaoyao", "Beidou", "Dori", "Fischl", "Kujou Sara", "Kuki Shinobu", "Lisa", "Razor", "Gorou", "Ningguang", "Noelle", "Yun Jin", "Barbara", "Candace", "Xingqiu", "Amber", "Bennett", "Thoma", "Xiangling", "Xinyan", "Yanfei"]
fourStarWeapons = ["Favonius Warbow", "Rust", "Sacrifical Bow", "Stringless", "Eye of Perception", "Favonious Codex", "Sacrifical Fragments", "The Widsith", "Favonius Greatsword", "Rainslasher", "Sacrifical Greatsword", "The Bell", "Dragon's Bane", "Favonious Lance", "Favonious Sword", "Lion's Roar", "Sacrifical Sword", "The Flute"]
threeStarWeapons = ["Raven Bow", "Sharpshooter's Oath", "Slingshot", "Emerald Orb", "Magic Guide", "Thrilling Tales of Dragon Slayers", "Bloodtainted Greatsword", "Debate Club", "Ferrous Shadow", "Black Tassel", "Cool Steel", "Harbinger of Dawn", "Skyrider Sword"]
def chanceCalculator():
    chance = random.randint(1, 1001)

    #For five stars (1.6 percent)
    if 0 < chance < 17:
        fiveStarChance = random.randint(0, 2)
        if fiveStarChance == 1:
            characterChance = random.randint(0, len(fiveStarCharacters) - 1)
            return "5 star: "+fiveStarCharacters[characterChance]
        else:
            weaponChance = random.randint(0, len(fiveStarWeapons) - 1)
            return "5 star: "+fiveStarWeapons[weaponChance]
    #For four stars (13 percent)
    elif 18 < chance < 149:
        fourStarChance = random.randint(0, 2)
        if fourStarChance == 1:
            characterChance = random.randint(0, len(fourStarCharacters) - 1)
            return "4 star: "+fourStarCharacters[characterChance]
        else:
            weaponChance = random.randint(0, len(fourStarWeapons) - 1)
            return "4 star: "+fourStarWeapons[weaponChance]
    #Everything else (86.4 percent)
    else:
        threeStarChance = random.randint(0, len(threeStarWeapons) - 1)
        return "3 star: "+threeStarWeapons[threeStarChance]
