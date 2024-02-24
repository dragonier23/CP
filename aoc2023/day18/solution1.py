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
    direction = ((0, 1) if splitStep[0] == 'R' else  
                 (1, 0) if splitStep[0] == 'D' else 
                 (0, -1) if splitStep[0] == 'L' else
                 (-1, 0) )
    
    digPlan.append([direction, int(splitStep[1])])

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

interior = area + 1 - (boundaryLen / 2)

print(interior + boundaryLen)
