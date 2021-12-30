import random
specials = ["Rotate the line permanently", "Players can place units wherever", "Place each other's units", "Wheel of Huge, add to both sides", "Both players get 3000pts", "Both players use the secret faction", "Change win condition", "Both players can reset as much as they want", "Both players spin wheel of big twice"]
rnumber = random.randrange(0, len(specials))
print(specials[rnumber])
