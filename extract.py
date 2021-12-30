import openpyxl as pxl
import pandas as pd

file = "TABSUSE.xlsx"
data = pd.read_excel(file, usecols="A:M")
data.head() 
data = data.fillna("")


#print(data)
unitlist = []
chumplist = []
midlist = []
biglist = []
hugelist = []
speciallist = []

for i in range(0, len(data)-1):
    if data["Name"].iloc[i]:
        name = data["Name"].iloc[i]
        faction = data["Faction"].iloc[i]
        cost = int(data["Cost"].iloc[i])

        if cost <= 300:
            level = 1
            chumplist.append([name, faction, cost, level])
        elif cost < 1000:
            level = 2
            midlist.append([name, faction, cost, level])
        elif cost < 2000:
            level = 3
            biglist.append([name, faction, cost, level])
        elif cost <= 6000:
            level = 4
            hugelist.append([name, faction, cost, level])
        if faction == "Special":
            speciallist.append([name, faction, cost, level])

        unitlist.append([name, faction, cost, level])

#print(unitlist)