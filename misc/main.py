import random

victories = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}
def playerInput():
    print("Give an input")
    validInputs = ["rock", "paper", "scissors"]
    play = input()
    if play in validInputs:
        return play
    else: 
        raise Exception("Give a valid input")
    
def computerInput():
    validInputs = ["rock", "paper", "scissors"]
    return random.choice(validInputs)

def decision(playerInp, computerInp):
    decisionDict1 = {
        playerInp: computerInp
    }
    decisionDict2 = {
        computerInp: playerInp
    }
    if playerInp == computerInp:
        return "draw"
    for x,y in victories.items():
        for a,b in decisionDict1.items():
            if (x,y) == (a,b):
                    return True
    for x,y in victories.items():
        for a,b in decisionDict2.items():
            if (x,y) == (a,b):
                    return False    

def main():
    playerPlay = playerInput()
    computerPlay = computerInput()
    print(f"You played {playerPlay}")
    print(f"The computer played {computerPlay}")
    playerWon = decision(playerPlay, computerPlay)
    if playerWon == True:
        print("You won Congrats")
    elif playerWon == False: 
        print("You lost :(")
    else:
        print("It was a draw!")

if __name__ == "__main__":
    main()