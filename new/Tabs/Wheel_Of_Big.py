from extract import *
import random

total = 0

print("PlayerX gets:")
rnumber = random.randrange(0, len(biglist))
unit = biglist[rnumber]
total += unit[2]
print(unit[0])
print("\n", total, "\n")