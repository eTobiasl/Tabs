from Player import Player
from wheels import *

print("\n"*2+"="*30+" TABS point counter " + "="*30+"\n"*2)


p1 = Player(input("[Player 1] name\n: "))
p2 = Player(input("[Player 2] name\n: "))
p1.addPoints(2500)
p2.addPoints(2500)

maxWins = 5


while p1.getWins() < maxWins and p2.getWins() < maxWins:
    print("\n"*2+"="*30+" Menu "+"="*30+"\n"*2)
    print("Round ["+str(p1.getWins() + p2.getWins())+"]")
    print("[0] - Display info\n[1] - Start round\n[2] - Add Points\n[3] - Subtract Points\n[4] - Add Win\n[5] - End Game")
    
    userInput = input("Select from the menu:\n")

    print("\n[0] - Player1 ("+p1.getName()+")\n[1] - Player2 ("+p2.getName()+")")
    if (userInput == "0") or (userInput == "5") or (userInput == "1"):
        selectedPlayerInput = "0"
    else:
        selectedPlayerInput = input("Select which player to affect:\n")

    if selectedPlayerInput == "0":
        selectedPlayer = p1
        otherPlayer = p2
    elif selectedPlayerInput == "1":
        selectedPlayer = p2
        otherPlayer = p1

    if userInput == "0":
        print("\n== "+selectedPlayer.getName()+" ==\nPoints: "+str(selectedPlayer.getPoints())+"\nWins: "+str(selectedPlayer.getWins())+"\nLosses: "+str(selectedPlayer.getLosses()))
        print("\n== "+otherPlayer.getName()+" ==\nPoints: "+str(otherPlayer.getPoints())+"\nWins: "+str(otherPlayer.getWins())+"\nLosses: "+str(otherPlayer.getLosses()))
        input("-- Press enter to continue --")
    
    elif userInput == "1":
        print("")
        gamerule = "nothing"
        while not p1.getFaction():
            gamerule = Wheel_Of_Warriors(p1, p2)
        while not p2.getFaction():
            gamerule = Wheel_Of_Warriors(p2, p1)

        print("\nThe current gamerule is '" + str(gamerule) + "'")

        print("\n" + str(p1.getName()) + " has " + str(p1.getPoints()) + " points, " + str(p1.getReset()) + ", can choose from '" + str(p1.getFaction()) + "', and needs to place: ")
        p1Units = p1.getUnits()
        if len(p1Units) > 0:
            for unit in p1.getUnits():
                print(unit)
        else:
            print("Nothing in particular")

        print("\n" + str(p2.getName()) + " has " + str(p2.getPoints()) + " points, " + str(p2.getReset()) + ", can choose from '" + str(p2.getFaction()) +  "', and needs to place: ")
        p2Units = p2.getUnits()
        if len(p2Units) > 0:
            for unit in p2Units:
                print(unit)
        else:
            print("Nothing in particular")
        
        roundEndInput = input("\nRound over? Type anything to continue")

        p1.resetFaction()
        p2.resetFaction()
        p1.setReset(False)
        p2.setReset(False)
        p1.resetUnits()
        p2.resetUnits()

    elif userInput == "2":
        addedPoints = input("\nAdd points ("+selectedPlayer.getName()+"):\n")
        selectedPlayer.addPoints(int(addedPoints))
    
    elif userInput == "3":
        subtractedPoints = input("\nSubtract points ("+selectedPlayer.getName()+"):\n")
        selectedPlayer.subtractPoints(int(subtractedPoints))

    elif userInput == "4":
        print(str(selectedPlayer.name) + " wins!")
        if selectedPlayer.getWins() == 5:
            print(str(selectedPlayer.getName()) + " wins the game!")
            userInput = input("Continue? \n[0]: Yes \n[1] No")
            if userInput == "1":
                print("Exiting...")
                break
        else:
            selectedPlayer.addWin()
            otherPlayer.addLoss()
            selectedPlayer.addPoints(2500)
            otherPlayer.addPoints(3000)

            time.sleep(1)
            Wheel_Of_Losers(otherPlayer, selectedPlayer)
            lastloss = selectedPlayer

    elif userInput == "5":
        print("Exiting...")
        break

