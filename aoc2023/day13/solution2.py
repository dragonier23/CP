#should be quite similar to the individual one, but we should track the ranges and append it to the end of the list should we need
#solution 125742456
import re

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()

def searchCol(input):
    colCount = len(input[0]) - 1
    for col in range(1, colCount):
        diff = 0
        unsymmetrical = False
        for i in range(0, min(col, (colCount - col))):
            for j in range(0, len(input)):
                if input[j][col + i] != input[j][col - 1 - i]:
                    diff += 1
                if diff > 1:
                    unsymmetrical = True
                    break
                #print(input[j][col + i] + input[j][col - 1 - i])
            if unsymmetrical:
                break
        if diff == 1:
            return col
    return False

def searchRow(input):
    colCount = len(input[0]) - 1
    for row in range(1, len(input)):
        diff = 0
        unsymmetrical = False
        for i in range(0, min(row, (len(input) - row))):
            for j in range(0, colCount):
                if input[row + i][j] != input[row - 1 - i][j]:
                    diff += 1
                if diff > 1:
                    unsymmetrical = True
                    break
            if unsymmetrical:
                break
        if diff == 1:
            return row
    return False


input = []
ans = 0
for line in file:
    if not(line.strip()):
        row = searchRow(input)
        col = searchCol(input)
        print(str(row) + str(col))
        ans += (row*100) if (row) else col
        input = []            
    else: 
        input.append(line)
    
print(ans)