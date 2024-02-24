#should be quite similar to the individual one, but we should track the ranges and append it to the end of the list should we need
#solution 125742456
import re

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()
#print(file)

def withinrange(seed, seedRange, dest, src, range): # 5 cases: no within range, exceed top, exceed bottom, exceed both, completely within
    #if the range exceeds, we want to split the ranges
    if seed + seedRange < src or seed > src+range:
        return (False, False)
    tmp = seed-src
    #now we need to identify if it is totally within the range
    if tmp < range and tmp >= 0: #the seed range starts within the src range
        if seed+seedRange-src-range < 0: # if it lies totally within the range
            return (1, [dest+tmp, seedRange])
        else: #otherwise, it exceeds via the top, so we split the range
            return (2, [dest+tmp, src+range-seed, src+range, seedRange+seed-src-range])
    else:
        if seed+seedRange-src-range > 0: #if it exceeds on both ends
            return (3, [dest, range, seed, src-seed,  src+range, seed+seedRange-src-range])
        else:
            return (2, [dest, seed+seedRange-src, seed, src-seed])
    
seedVal = re.findall(r'\d+', file.pop(0).split(": ")[1])
seeds = []
for i in range(0, len(seedVal), 2):
    seeds.append([int(seedVal[i]), int(seedVal[i+1])]) #seed structure will look like array of [seed, range]
print(seeds)

completed = [False] * len(seeds) #array to compare against as we slowly through the numbers
skipNext = True
mapList = []
#we note that if we see a white line, we need to reset the false things and skip the next line, then start comparing again
for i in range(1, len(file)): #skip the first line
    line = file[i]
    if not(line.strip()): #if the line is an empty line, then we know we got to the end of the map, hence we should start finding the ranges
        mapList.sort(key=lambda x: int(x[1])) #this sorts the list according to the sources ranges
        #we can then run through the list, checking for matching ranges
        print(mapList)
        for mapRange in mapList:
            for i in range(len(seeds.copy())):
                rangeCount, rangeVal = withinrange(int(seeds[i][0]), int(seeds[i][1]), int(mapRange[0]), int(mapRange[1]), int(mapRange[2]))
                if rangeCount and not(completed[i]): #i.e. we found something to split,
                    seeds[i][0] = rangeVal[0]
                    seeds[i][1] = rangeVal[1]
                    completed[i] = True
                    if rangeCount > 1:
                        for j in range(2, rangeCount*2, 2):
                            if rangeVal[j+1] > 0:
                                seeds.append([rangeVal[j], rangeVal[j+1]])
                                completed.append(False)
        print(seeds)
        for j in range(len(completed)): 
            completed[j] = False
        skipNext = True # we reset the false things, and skip the next line
        mapList = []
        #print(completed)
    elif skipNext:
        skipNext = False # we no longer skip lines  
    else: #otherwise we are at a range line
        map = re.findall(r'\d+', line) #we extract the 3 numbers from the line
        mapList.append(map) #appended to the mapList

#here, we should be done with mapping, now to compare
seeds.sort(key=lambda x: x[0])
print(seeds)
print(seeds[0])