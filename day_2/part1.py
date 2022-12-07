

play = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

outcome = {
    "loss": 0,
    "draw": 3,
    "win": 6,
}   

def parse(text):
        textArr = []
        for i in text:
            textArr.append(i)
        
        return decision(textArr)
        
# A, X = rock
# B, Y = paper
# C, Z = scissors 
def decision(textArr):
    score = 0
    print(textArr[2])
    # Rock
    if textArr[0] == "A":
        # Rock V Paper 8
        if textArr[2] == "Y":
            score = updateScore(play["paper"], outcome["win"], score)
            print(textArr)
        

        # Rock V Scissors 3
        elif textArr[2] == "Z":
            score = updateScore(play["scissors"], outcome["loss"], score)
            
        # Rock V Rock 4
        elif textArr[2] == "X":
            score = updateScore(play["rock"], outcome["draw"], score)
            
    if textArr[0] == "B":
        # Paper V Rock 7
        if textArr[2] == "X":
            score = updateScore(play["rock"], outcome["loss"], score)

        # Paper V Scissors 3
        elif textArr[2] == "Z":
            score = updateScore(play["scissors"], outcome["win"], score)
            
        # Paper V Paper 5
        elif textArr[2] == "Y":
            score = updateScore(play["paper"], outcome["draw"], score)
            
    if textArr[0] == "C":
        # Scissors V Paper 2
        if textArr[2] == "Y":
            score = updateScore(play["paper"], outcome["loss"], score)

        # Scissors V Rock
        elif textArr[2] == "X":
            score = updateScore(play["rock"], outcome["win"], score)
            
        # Scissors V Scissors
        elif textArr[2] == "Z":
            score = updateScore(play["scissors"], outcome["draw"], score)
        
    print(score)
    return score

def updateScore(play, outcome, score):
        return score + play + outcome

with open("puzzle.txt") as f:
    # t = ['B', '', 'Y']
    scoreList = []
    lines = f.readlines()
    for i in lines:
        scoreList.append(parse(i))
    print(sum(scoreList))
    
    
        
    
    
            
    

    

    
