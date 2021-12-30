import random
lose = ["+1500pts", "Delete 1000pts from enemy", "Reset, pick two factions, +500pts", "+1500pts", "Wheel Of Big", "3x Wheel Of Mid", "5x Wheel Of Chumps, times two", "Reset, use secret faction, +500pts"]
rnumber = random.randrange(0, len(lose))
print(lose[rnumber])
