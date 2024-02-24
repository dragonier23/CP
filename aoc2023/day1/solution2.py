words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
#mapped = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# things to do: check the line for numeric and word numbers 
#we can do this with re, to check the index of the word + if they are first or last --> from there we can find out which is the first and which is the last

import re

filename = 'problemstatement.txt'

file = open(filename, 'r').readlines()
print(file)

total = 0
for line in file: #for line in the file
    first = 0
    firstindex = float('inf')
    last = 0
    lastindex = -1
    firstnum = True
    for i in range(len(line)): #running through the line to check for the number 
        if line[i].isdigit():
            if firstnum:
                first = int(line[i])
                firstindex = i
                last = int(line[i])
                lastindex = i
                firstnum = False
            else:
                last = int(line[i])
                lastindex = i

    #by this point we wld have checked the line for the numbers --> identifying which was the first and which was the last numbers 
    #now we need to search the string for the corresponding alphafirst and alphalast
    for i in range(len(words)):
        tmp = line.find(words[i]) #tempoarily set an index for the start of the string to compare with the current lowest
        if tmp != -1: #tmp return -1 if the number is not found, so here, we would have found the word
            if tmp < firstindex:
                first = int(i+1)
                firstindex = tmp
            if tmp > lastindex:
                last = int(i+1)
                lastindex = tmp

    #by here, we should have recorded the first and the last numbers, so now is to add it to the total
    print(first)
    print(last)
    total += ((first * 10) + last)

print(total)
