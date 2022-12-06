
# Part one
calories = []

listOfCalorieSums = []

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
    print(max(listOfCalorieSums))