import re

filename = 'problemstatement.txt' #'test.txt' #'

file = open(filename, 'r').readlines()

firstList = []
secondList = dict()

for line in file:
    nums = line.replace("\n", "").split("  ")
    firstList.append(nums[0])
    if not nums[1].strip() in secondList: 
        secondList[nums[1].strip()] = 0
    secondList[nums[1].strip()] += 1

#print(firstList)
#print(secondList)

sum = 0
for i in range(len(firstList)):
    if firstList[i] in secondList:
        sum += (int(firstList[i]) * secondList[firstList[i]])

print(sum)

    