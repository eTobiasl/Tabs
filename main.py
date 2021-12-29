from Player import Player

print("\n"*2+"="*30+" TABS point counter " + "="*30+"\n"*2)


p1 = Player(input("[Player 1] name\n: "))
p2 = Player(input("[Player 2] name\n: "))

maxWins = 5


while p1.getWins() < maxWins and p2.getWins() < maxWins:
    print("\n"*2+"="*30+" Menu "+"="*30+"\n"*2)
    print("Round ["+str(p1.getWins() + p2.getWins())+"]")
    print("[0] - Display info\n[1] - Add Points\n[2] - Subtract Points\n[3] - Add Win")
    
    userInput = input("Select from the menu:\n")

    print("\n[0] - Player1 ("+p1.getName()+")\n[1] - Player2 ("+p2.getName()+")")
    if userInput != "0":
        selectedPlayerInput = input("Select which player to effect:\n")
    else:
        selectedPlayerInput = "0"

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
        addedPoints = input("\nAdd points ("+selectedPlayer.getName()+"):\n")
        selectedPlayer.addPoints(int(addedPoints))
    
    elif userInput == "2":
        subtractedPoints = input("\nSubtract points ("+selectedPlayer.getName()+"):\n")
        selectedPlayer.subtractPoints(int(subtractedPoints))

    elif userInput == "3":
        selectedPlayer.addWin()
        otherPlayer.addLoss()

        selectedPlayer.addPoints(2500)
        otherPlayer.addPoints(2500)

