import re

filename =   'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()
#print(file)

def withinrange(seed, dest, src, range):
    tmp = seed-src
    if tmp < range and tmp >= 0:
        #if this is the case, then the seed is within the range, hence, we should find this destination
        return dest + tmp
    return False

#first extract the seeds
seeds = re.findall(r'\d+', file.pop(0).split(": ")[1])
print(seeds)

completed = [False] * len(seeds) #array to compare against as we slowly through the numbers
skipNext = True
#we note that if we see a white line, we need to reset the false things and skip the next line, then start comparing again
for i in range(1, len(file)): #skip the first line
    line = file[i]
    if not(line.strip()): #if the line is an empty line
        print(seeds)
        for j in range(len(completed)):
            completed[j] = False
        skipNext = True # we reset the false things, and skip the next line
        print(completed)
    elif skipNext:
        skipNext = False # we no longer skip lines
    else: #otherwise we are at a range line
        map = re.findall(r'\d+', line) #we extract the 3 numbers from the line
        for j in range(len(seeds)): #we run through each number, checking if it is in range
            stored = withinrange(int(seeds[j]), int(map[0]), int(map[1]), int(map[2]))
            if stored and not(completed[j]): #if the number is mapped within this range and has not yet been converted, convert it
                seeds[j] = stored
                completed[j] = True

#here, we should be done with mapping, now to compare
closest = float("inf")
for location in seeds:
    if int(location) < closest:
        closest = int(location)

print(closest)
