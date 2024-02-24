import re

tmp = [1] * 10
filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()
print(file)

sum = 0
for line in file:
    #split the line
    match = 0
    count = tmp.pop(0)
    tmp.append(1)
    numList = line.split(": ")[1].split(" | ")
    winNum = re.findall('\d+', numList[0])
    gotNum = re.findall('\d+', numList[1])
    for number in winNum:
        if number in gotNum:
            match += 1
    for i in range(match):
        tmp[i]+= count
    sum += count

print(sum)

    