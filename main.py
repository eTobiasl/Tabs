from Player import Player
from wheels import *
import random

print("\n"*2+"="*30+" TABS multiplayer assistant " + "="*30+"\n"*2)


p1 = Player(input("[First player] name:\n"))
p2 = Player(input("[Second player] name:\n"))

p1.addPoints(2500)
p2.addPoints(2500)

startingPlayer = random.randint(0,1)

if startingPlayer == 0:
    p1.setStartingPlayer()
else:
    p2.setStartingPlayer()


maxWins = int(input("How many rounds to win?\n"))


while p1.getWins() < maxWins and p2.getWins() < maxWins:
    print("\n"*2+"="*30+" Menu "+"="*30+"\n"*2)
    print("Round ["+str(p1.getWins() + p2.getWins())+"]")
    print("[0] - Display info\n[1] - Start round\n[2] - More Options\n[3] - End Game")
    
    userInput = input("Select from the menu:\n")

    if userInput == "0":
        print("\n== "+p1.getName()+" ==\nPoints: "+str(p1.getPoints())+"\nWins: "+str(p1.getWins())+"\nLosses: "+str(p1.getLosses()))
        print("\n== "+p2.getName()+" ==\nPoints: "+str(p2.getPoints())+"\nWins: "+str(p2.getWins())+"\nLosses: "+str(p2.getLosses()))
        input("-- Press enter to continue --\n")
    
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
        
        if p1.checkIfPlayerStarts():
            print("\n["+p1.getName()+"] has to place their units first")
        elif p2.checkIfPlayerStarts():
            print("\n["+p2.getName()+"] has to place their units first")

        roundEndInput = input("-- Round over? press enter to continue --\n")

        p1.resetFaction()
        p2.resetFaction()
        p1.setReset(False)
        p2.setReset(False)
        p1.resetUnits()
        p2.resetUnits()
        
        roundWinner = input("\n== Who won the round? ==\n[0] - Player 1 ("+str(p1.getName())+")\n[1] - Player 2 ("+str(p2.getName())+")\n")
        if roundWinner == "0":
            roundWinnerPlayer = p1
            roundLoserPlayer = p2
        elif roundWinner == "1":
             roundWinnerPlayer = p2
             roundLoserPlayer = p1

        roundWinnerPlayer.addWin()
        roundLoserPlayer.addLoss()
        print(str(roundWinnerPlayer.getName()) + " won the round!")
       
        
        input("-- Press enter to continue --\n")

        time.sleep(1)
        Wheel_Of_Losers(roundLoserPlayer, roundWinnerPlayer)
        lastloss = roundLoserPlayer

    elif userInput == "2":
        print("\n"*2+"="*30+" Submenu "+"="*30+"\n"*2)
        print("[0] - Add Points\n[1] - Subtract Points\n[2] - Add Win")
        underMenuInput = input("Select from the submenu:\n")

        print("\n[0] - Player 1 ("+p1.getName()+")\n[1] - Player 2 ("+p2.getName()+")")
        selectedPlayerInput = input("Select which player to affect:\n")

        if selectedPlayerInput == "0":
            selectedPlayer = p1
            otherPlayer = p2
        elif selectedPlayerInput == "1":
            selectedPlayer = p2
            otherPlayer = p1

        if underMenuInput == "0":
            addedPoints = input("\nAdd points ("+selectedPlayer.getName()+"):\n")
            selectedPlayer.addPoints(int(addedPoints))
        
        elif underMenuInput == "1":
            subtractedPoints = input("\nSubtract points ("+selectedPlayer.getName()+"):\n")
            selectedPlayer.subtractPoints(int(subtractedPoints))

        elif underMenuInput == "2":
            if selectedPlayer.getWins() == maxWins:
                print(str(selectedPlayer.getName()) + " wins the game!")
                userInput = input("Continue? \n[0]: Yes \n[1] No")
                if userInput == "1":
                    print("Exiting...")
                    break
            else:
                selectedPlayer.addWin()
                otherPlayer.addLoss()

                time.sleep(1)
                Wheel_Of_Losers(otherPlayer, selectedPlayer)
                lastloss = otherPlayer

    elif userInput == "3":
        print("Exiting...")
        print("\n"+p1.getName() + "Ended the game with ["+ str(p1.getWins()) + "] wins and [" + str(p1.getLosses()) + "] lossses")
        print(p2.getName() + "Ended the game with ["+ str(p2.getWins()) + "] wins and [" + str(p2.getLosses()) + "] lossses")

        if p1.getWins() > p2.getWins():
            print(p1.getName() + " Won most rounds with [" + str(p1.getWins()) + "] wins!")
        else:
            print(p2.getName() + " Won most rounds with [" + str(p2.getWins()) + "] wins!")
        break

