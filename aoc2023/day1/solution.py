#'[0-9]'

import re

filename = 'problemstatement.txt'

file = open(filename, 'r').readlines()
print(file)

total = 0
lineswithoutnumber = 0
for line in file:
    first = True
    last = 0
    entered = False
    for i in range(len(line)):
        if line[i].isdigit():
            entered = True
            if first:
                #print(int(line[i]) * 10)
                total += int(line[i]) * 10
                last = int(line[i])
                first = False
            else:
                last = int(line[i])
    if not(entered):
        lineswithoutnumber += 1
    total += last
    #print(last)
print(lineswithoutnumber)
print(total)


#total = 0
#counter = 0
#for i in range(len(file)):
#    if file[i].isdigit():
#        if counter == 0:
#            print(int(file[i]) * 10)
#            total += int(file[i]) * 10
#            counter = 1
#        elif counter == 1:
#            print(int(file[i]))
#            total += int(file[i])
#            counter = 0

#print(total)