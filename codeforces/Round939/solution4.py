length = int(input())
xs = list(map(int, input().split(" ")))

def MEX(xs, ignoreCount):
    ignoreIndex = len(xs)
    ignored = 0
    for i in range(ignoreIndex):
        if xs[i] >= ignoreIndex:
            if ignored >= ignoreCount:
                ignoreIndex = i
                break
            ignored += 1
    if ignoreIndex == len(xs):
        if ignoreIndex * ignoreIndex > sum(xs):
            return ([ignoreIndex] * ignoreIndex, ignoreIndex * ignoreIndex)
        else: 
            return (xs, sum(xs))
    ignoreList, ignoreSum = MEX(xs, ignoreCount + 1)
    notIgnoredFstList, notIgnoredFstSum = MEX(xs[:ignoreIndex], ignoreCount)
    notIgnoredSndList, notIgnoredSndSum = MEX(xs[ignoreIndex+1:], 0)
    notIgnoredSum = notIgnoredFstSum + notIgnoredSndSum + xs[ignoreIndex]
    if ignoreSum > notIgnoredSum:
        return (ignoreList, ignoreSum)
    else: 
        return (notIgnoredFstList + [xs[ignoreIndex]] + notIgnoredSndList, notIgnoredSum)
    
solutionList, solutionSum = MEX(xs, 0)

changeList = []
index = 0
while index < length: 
    if solutionList[index] != xs[index]: 
        check = -1
        while True:
            if solutionList[index] == xs[index+check]:
                check -= 1
            else:
                break
        defaultShift = 1 if index == 0 else 2 + check 
        zeroPresent = True if 0 in xs[index:index+solutionList[index]] else False
        changeList.append((index+defaultShift, solutionList[index], zeroPresent))
        index += solutionList[index]
        continue
    index += 1
#we need to check if different, how many of the previous ones are the same


#we want this to generate a list of moves
def genList(startIndex, count):
    if count == 1:
        return [(startIndex, startIndex)]
    actionList = []
    for i in range(count-1):
        actionList = actionList + genStart(startIndex+i, count-1-i)
    actionList.append((startIndex, startIndex+count-1))
    return actionList
#we want this to generate a list of moves 
def genStart(startIndex, num):
    if num == 1:
        return [(startIndex, startIndex)]
    actionList = []
    actionList = actionList + genList(startIndex, num)
    actionList.append((startIndex+1, startIndex+num-1))
    return actionList

movesList = []
if changeList:
    for change in changeList:
        movesList.append((change[0], change[0]+change[1]-1))
        if change[2]:
            movesList.append((change[0], change[0]+change[1]-1))
        movesList = movesList + genList(change[0], change[1])

#we still have to print correctly, and check for 0 in the sequence. 
print(str(solutionSum) + " " + str(len(movesList))) 

if movesList: 
    for move in movesList:
        print(str(move[0]) + " " + str(move[1]))
