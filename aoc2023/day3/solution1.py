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

symbolList = '!@#$%^&*()-=+_<>/?'

numstart = False
number = ""
sum = 0
addNum = False
#so we have to fistly find the numbers, then we have to search the surrounding elements to see if they lie in symbol list - if they do, we add the number to the sum
for row in range(len(engine)):
    for col in range(len(engine[0])):
        #we first have to detect a line of numbers
        if engine[row][col].isnumeric():
            if numstart: #if is not the start of a number (opposite)
                numlength += 1
                number = number + engine[row][col]
            else:
                colstart = col
                numlength = 1
                numstart = True
                number = number + engine[row][col]     
        if not(engine[row][col].isnumeric()) and numstart: #if we have found the end of a number
            #we should check the surrrounding elements for symbols
            if row > 0 and colstart > 0:
                if engine[row - 1][colstart - 1] in symbolList: #check top left
                    addNum = True
            if row > 0 and (colstart + numlength - 1) < len(engine[0]) - 1:
                if engine[row - 1][colstart + numlength] in symbolList: #check top right
                    addNum = True
            if row < len(engine) - 1 and (colstart + numlength - 1) < len(engine[0]) - 1: #check bottom left
                if engine[row + 1][colstart + numlength] in symbolList:
                    addNum = True
            if row < len(engine) - 1 and colstart > 0: #check bottom right
                if engine[row + 1][colstart - 1] in symbolList:
                    addNum = True
            if colstart > 0: #check left side
                if engine[row][colstart - 1] in symbolList:
                    addNum = True
            if (colstart + numlength - 1) < len(engine[0]) - 1: #check right side
                if engine[row][colstart + numlength] in symbolList:
                    addNum = True
            if row > 0:
                for i in range(colstart, colstart + numlength):
                    if engine[row - 1][i] in symbolList:
                        addNum = True
            if row < len(engine) - 1:
                for i in range(colstart, colstart + numlength):
                    if engine[row + 1][i] in symbolList:
                        addNum = True
            #this will be after we check the surrounding elements for symbols
            if addNum:
                sum += int(number)
                print(number)
                addNum = False
            number = ""
            numstart = False
            #print(sum)

print(sum)
