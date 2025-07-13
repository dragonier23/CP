import re

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()

firstList = []
secondList = []

for line in file:
    nums= line.split("  ")
    firstList.append(int(nums[0]))
    secondList.append(int(nums[1]))

firstList = sorted(firstList)
secondList = sorted(secondList)

sum = 0
for i in range(len(firstList)):
    sum += (abs(firstList[i] - secondList[i]))

print(sum)

    