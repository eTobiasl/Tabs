from extract import *
import random

total = 0

print("PlayerX can pick:")
for i in range(0, 10):
    rnumber = random.randrange(0, len(speciallist))
    unit = speciallist[rnumber]
    speciallist.remove(unit)
    total += unit[2]*2
    print(unit[0])
    
print("\n")