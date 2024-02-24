filename = 'problemstatement.txt' #'test1.txt' #

file = open(filename, 'r').readlines()

#easiest way is to store it in a large mxn array and then try to find them
engine = []
lineno = 0
for line in file:
    engine.append([])
    for element in line:
        engine[lineno].append(element)
    lineno += 1

ROWNO = len(engine)
COLNO = len(engine[0])

sum = 0
#so we have to fistly find the numbers, then we have to search the surrounding elements to see if they lie in symbol list - if they do, we add the number to the sum
for row in range(ROWNO):
    for col in range(COLNO):
        if engine[row][col] == '*': # if it is a star, we should check the surroundings for numbers
            adjNums = []
            adjacentNums = 0
            if col > 0:
                if engine[row][col - 1].isnumeric():
                    adjNums.append("")
                    adjacentNums += 1
                    tmp = col - 1
                    while engine[row][tmp].isnumeric() and tmp >= 0:
                        adjNums[-1] = engine[row][tmp] + adjNums[-1]
                        tmp -= 1
            if col < COLNO - 1:
                if engine[row][col + 1].isnumeric():
                    adjNums.append("")
                    adjacentNums += 1
                    tmp = col + 1
                    while engine[row][tmp].isnumeric() and tmp < COLNO:
                        adjNums[-1] = adjNums[-1] + engine[row][tmp] 
                        tmp += 1
            #so now we need to check the top row
            if row > 0 and col > 0:
                if engine[row-1][col-1].isnumeric():
                    adjNums.append("")
                    adjacentNums += 1
                    tmp = col - 1
                    while engine[row-1][tmp].isnumeric() and tmp >= 0:
                        adjNums[-1] = engine[row-1][tmp] + adjNums[-1]
                        tmp -= 1
                    if engine[row-1][col].isnumeric():
                        adjNums[-1] = adjNums[-1] + engine[row - 1][col]
                        if col < COLNO - 1:
                            if engine[row-1][col + 1].isnumeric():
                                adjNums[-1] = adjNums[-1] + engine[row - 1][col + 1]
                                tmp = col + 2
                                while engine[row-1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row-1][tmp] 
                                    tmp += 1
                    else:
                        if col < COLNO - 1:
                            if engine[row-1][col + 1].isnumeric():
                                adjNums.append("")
                                adjacentNums += 1
                                tmp = col + 1
                                while engine[row-1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row-1][tmp] 
                                    tmp += 1
                else:
                    if engine[row-1][col].isnumeric():
                        adjNums.append("")
                        adjacentNums += 1
                        adjNums[-1] = adjNums[-1] + engine[row - 1][col]
                        if col < COLNO - 1:
                            if engine[row-1][col + 1].isnumeric():
                                adjNums[-1] = adjNums[-1] + engine[row - 1][col + 1]
                                tmp = col + 2
                                while engine[row-1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row-1][tmp] 
                                    tmp += 1
                    else:
                        if col < COLNO - 1:
                            if engine[row-1][col + 1].isnumeric():
                                adjNums.append("")
                                adjacentNums += 1
                                tmp = col + 1
                                while engine[row-1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row-1][tmp] 
                                    tmp += 1
            #checking bottom row
            if row < (ROWNO - 1) and col > 0:
                if engine[row+1][col-1].isnumeric():
                    adjNums.append("")
                    adjacentNums += 1
                    tmp = col - 1
                    while engine[row+1][tmp].isnumeric() and tmp >= 0:
                        adjNums[-1] = engine[row+1][tmp] + adjNums[-1]
                        tmp -= 1
                    if engine[row+1][col].isnumeric():
                        adjNums[-1] = adjNums[-1] + engine[row+1][col]
                        if col < COLNO - 1:
                            if engine[row+1][col+1].isnumeric():
                                adjNums[-1] = adjNums[-1] + engine[row+1][col+1]
                                tmp = col + 2
                                while engine[row+1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row+1][tmp] 
                                    tmp += 1
                    else:
                        if col < COLNO - 1:
                            if engine[row+1][col + 1].isnumeric():
                                adjNums.append("")
                                adjacentNums += 1
                                tmp = col + 1
                                while engine[row+1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row+1][tmp] 
                                    tmp += 1
                else:
                    if engine[row+1][col].isnumeric():
                        adjNums.append("")
                        adjacentNums += 1
                        adjNums[-1] = adjNums[-1] + engine[row + 1][col]
                        if col < COLNO - 1:
                            if engine[row+1][col + 1].isnumeric():
                                adjNums[-1] = adjNums[-1] + engine[row + 1][col + 1]
                                tmp = col + 2
                                while engine[row+1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row+1][tmp] 
                                    tmp += 1
                    else:
                        if col < COLNO - 1:
                            if engine[row+1][col + 1].isnumeric():
                                adjNums.append("")
                                adjacentNums += 1
                                tmp = col + 1
                                while engine[row+1][tmp].isnumeric() and tmp < COLNO:
                                    adjNums[-1] = adjNums[-1] + engine[row+1][tmp] 
                                    tmp += 1
            if adjacentNums == 2:
                print(adjNums)
                sum += (int(adjNums[0]) * int(adjNums[1]))

print(sum)
