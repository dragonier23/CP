import re

points = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()
print(file)

sum = 0
for line in file:
    #split the line
    match = 0
    numList = line.split(": ")[1].split(" | ")
    winNum = re.findall('\d+', numList[0])
    gotNum = re.findall('\d+', numList[1])
    for number in winNum:
        if number in gotNum:
            match += 1
    sum += points[match]

print(sum)

    