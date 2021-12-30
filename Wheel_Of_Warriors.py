import random
factions = ["Tribal", "Farmer", "Ancient", "Medieval", "Viking", "Dynasty", "Reneissance", "Pirate", "Spooky", "Wild West", "Good", "Evil", "Legacy", "Wheel Of Secret", "250pts or less", "500pts or more", "Ranged units", "Melee units", "Opponent's choice", "Your choice", "Wheel of Wacky", "Wheel of Wacky"]
rnumber = random.randrange(0, len(factions))
print(factions[rnumber])
print(len(factions))
print(len("hello"))