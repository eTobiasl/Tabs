import random
from extract import *
import time

loselist = ["+1500pts", "Delete up to 1000pts from enemy", "Reset, pick two factions, +500pts", "+1500pts", "Wheel Of Big", "3x Wheel Of Mid", 
            "5x Wheel Of Chumps, times two", "Reset, use secret faction, +500pts"]
factions = ["Tribal", "Farmer", "Ancient", "Medieval", "Viking", "Dynasty", "Reneissance", "Pirate", "Spooky", "Wild West", "Good", "Evil", 
            "Legacy", "Wheel Of Secret", "250pts or less", "500pts or more", "Ranged units", "Melee units", "Opponent's choice", "Your choice", 
            "Wheel of Wacky", "Wheel of Wacky"]
specials = ["Rotate the line permanently", "Players can place units wherever", "Place each other's units", "Wheel of Huge, add to both sides", 
            "Both players get 3000pts", "Both players use the secret faction", "Change win condition", "Both players can reset as much as they want", 
            "Both players spin wheel of big twice"]

def Wheel_Of_Units(players, rolls, type, number):
    time.sleep(3)
    if type == "small":
        units = chumplist
    elif type == "mid":
        units = midlist
    elif type == "big":
        units = biglist
    elif type == "huge":
        units = hugelist

    total = 0

    if len(players) == 1:
        print(str(players[0].getName()) + " gets " + str(number) +  " of:")
    else:
        print("Both players get" + str(number) +  " of:")

    for i in range(0, rolls):
        rnumber = random.randrange(0, len(units))
        unit = units[rnumber]
        total += unit[2]
        print(unit[0])
        for i in range(0, len(players)):
            players[i].setUnits(unit[0])

    total = total*number

    print("\nTotal cost: ", total, "\n")

    for i in range(0, len(players)):
        players[i].addPoints(total)

def Wheel_Of_Wacky(player, enemy):
    rule = "nothing"
    rnumber = random.randrange(0, len(specials))
    wacky = specials[rnumber]
    rule = None
    print("The wheel of wacky decrees '" + str(wacky) + "'")
    
    time.sleep(2)

    if rnumber == 0 or rnumber == 1 or rnumber == 2 or rnumber == 6:
        rule = wacky
    elif rnumber == 3:
        Wheel_Of_Units([player, enemy], 1, "huge", 1)
    elif rnumber == 4:
        player.addPoints(3000)
    elif rnumber == 5:
        player.giveFaction("Secret")
        enemy.giveFaction("Secret")
    elif rnumber == 7:
        player.setReset(True)
    elif rnumber == 8:
        Wheel_Of_Units([player], 2, "big", 1)
        Wheel_Of_Units([enemy], 2, "big", 1)

    return rule



def Wheel_Of_Losers(player, enemy):
    print(str(player.getName()) + " gets to spin the wheel of losers! \n")
    print("...")
    rnumber = random.randrange(0, len(loselist))
    time.sleep(3)
    print(str(player.getName()) + " rolls '" + str(loselist[rnumber]) + "'")
    if (rnumber == 0) or (rnumber == 3):
        player.addPoints(1500)
    elif rnumber == 1:
        enemy.addPoints(-1000)
    elif (rnumber == 2):
        player.addPoints(500)
        player.giveFaction("Pick two")
        player.setReset(True)
    elif rnumber == 4:
        Wheel_Of_Units([player], 1, "big", 1)
    elif rnumber == 5:
        Wheel_Of_Units([player], 3, "mid", 1)
    elif rnumber == 6:
        Wheel_Of_Units([player], 5, "small", 2)
    elif rnumber == 7:
        player.addPoints(500)
        player.giveFaction("Special")
        player.setReset(True)

    time.sleep(3)

def Wheel_Of_Warriors(player, enemy):
    rule = "nothing"
    playerName = player.getName()
    rnumber = random.randrange(0, len(factions))
    print(str(playerName) + " spins the wheel of warriors")

    time.sleep(2)

    if rnumber < 20:
        playerFaction = factions[rnumber]
        print(str(playerName) + " gets to choose units from '" + str(playerFaction) + "'")
        player.giveFaction(playerFaction)
    else:
        print(str(playerName) + " lands on the wheel of wacky")
        rule = Wheel_Of_Wacky(player, enemy)

    time.sleep(3)
    return rule