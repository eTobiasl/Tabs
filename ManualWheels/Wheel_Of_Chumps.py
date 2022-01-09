from extract import *
import random

total = 0

print("PlayerX gets:")
for i in range(0, 5):
    rnumber = random.randrange(0, len(chumplist))
    unit = chumplist[rnumber]
    total += unit[2]*2
    print(unit[0])
print("\n", total, "\n")