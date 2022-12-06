# Part two
calories = []
listOfCalorieSums = []
topThree = []

def addToSum(strList):
    calorieSum = sum([eval(x) for x in strList])
    listOfCalorieSums.append(calorieSum)

with open('calories.txt') as f:
    lines = f.readlines()
    for i in lines:
        if i != '\n':
            calories.append(i)
        else:
            addToSum(calories)
            calories = []
    # New Stuff
    for i in range(3):
        topThree.append(max(listOfCalorieSums))
        listOfCalorieSums.remove(max(listOfCalorieSums))
    print(sum(topThree))