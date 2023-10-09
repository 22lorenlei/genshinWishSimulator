#for the wanderlustInvocation banner
import random
def chanceCalculator():
    chance = random.randint(1, 1000)
    if chance < 110 and chance > 10:
        return "4 star"+str(chance)
    elif chance < 10:
        return "5 star"+str(chance)
    else:
        return "3 star"+str(chance)
