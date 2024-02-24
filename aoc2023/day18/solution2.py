import re

def findArea(boundary):
    corners = len(boundary)
    area = 0
    for i in range(corners):
        area += 0.5 * (boundary[i%corners][0]) * (boundary[(i+1)%corners][1] - boundary[(i-1)%corners][1]) 
    return area

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()

# this will be the digging plan
digPlan = []
for step in file:
    splitStep = step.split(' ')
    direction = ((0, 1) if splitStep[2][-3] == '0' else  
                 (1, 0) if splitStep[2][-3] == '1' else 
                 (0, -1) if splitStep[2][-3] == '2' else
                 (-1, 0))

    distance = int(("0x" + str(splitStep[2][2:-3])), 16)
    digPlan.append([direction, distance])

print(digPlan)
#so now we have to figure out the parameter
boundary = []
curr = (0, 0)
boundaryLen = 0
for step in digPlan:
    boundaryLen += step[1]
    curr = (curr[0]+(step[0][0]*step[1]), curr[1]+(step[0][1]*step[1]))
    boundary.append(curr)

area = abs(findArea(boundary))
print(boundary)
print(area)
# A = i + b/2 - 1

interior = area + 1 - int(boundaryLen / 2)

print(interior + boundaryLen)
