import re

filename = 'problemstatement.txt' # 'test.txt' #
file = open(filename, 'r').readlines()

blockmap = [list(map(int, block.strip().replace("~", ",").split(","))) for block in file]
blockmap.sort(key=lambda x: x[2])

def intersect(one, two):
    return min(one[3], two[3]) >= max(one[0], two[0]) and min(one[4], two[4]) >= max(one[1], two[1])

for index, block in enumerate(blockmap):
    maxZ = 1
    for below in blockmap[:index]:
        if intersect(below, block):
            maxZ = max(maxZ, below[5] + 1)
    block[5] = maxZ + (block[5] - block[2])
    block[2] = maxZ
    
blockmap.sort(key=lambda x: x[2])

#so now we have to determine how many blocks we are supporting
#basic idea: for each block, if 2 or more blocks support it, then the blocks below it can be deleted
#so for each block, we know it is supporting n blocks. Each of these n blocks are supported by x 
#blocks, and we want to find the min x of this n blocks. if min x == 1, we cannot delete

supporting = [] 
#this supporting follows the index of the block map, and each entry has 2 things: 1. who it is supported by, and 2. who it is supporting
for index, block in enumerate(blockmap):
    #for a block, we first identify how many blocks support it, and which blocks they are
    # after we figure this out, we can then, for each block, identify the blocks it is supporting, and 
    #whether it is the lone block supporting it
    supporting.append([[], []]) 
    for indexBelow, below in enumerate(blockmap[:index]):
        if intersect(below, block) and below[5] == block[2]-1: #if the blocks lie on top of each other
            supporting[index][0].append(indexBelow) #this tells us for the nth index block, what it is being supported by
            supporting[indexBelow][1].append(index)
print(supporting)

ans = 0
for block in supporting:
    loneSupporter = False
    for blockSupported in block[1]:
        if len(supporting[blockSupported][0]) == 1:
            loneSupporter = True
            break
    if not(loneSupporter):
        ans += 1

print(ans)
'''
PROBLEM: we arent able to drop the bricks in this case, and we wont be able to accurately determine
the structure of the tower
#basic idea: for each block, if 2 or more blocks support it, then the blocks below it can be deleted
#so for each block, we know it is supporting n blocks. Each of these n blocks are supported by x 
#blocks, and we want to find the min x of this n blocks. if min x == 1, we cannot delete

#so how do we read this? we first note the x y is only limited from 0 - 9 
#so we will have 2 data strcutures. 
#1. a hashmap, with (x, y) as the key, and element being a list [(block no, height)]
#2. another hashmap, with block no as the key, and the element being: [blocks, [blocks being supported], supported by]
#3. running through each block, we will need to basically look the z's below it, and identify the distance, choosing shortest 

#first we initialise
blockmap = dict()
blockDetails = dict()
blockno = 0
for block in file:
    start, end = block.strip().split("~")
    sx, sy, sz = map(int, start.split(","))
    ex, ey, ez = map(int, end.split(","))
    #so for a range, we want to find which is the values differ?
    blockDetails[blockno] = [[], [], 0]
    if ex != sx: #if the start not equal to the end, we need to iterate this
        for x in range(sx, ex+1):
            if (x, sy) in blockmap:
                blockmap[(x, sy)].append((blockno, sz))
            else: 
                blockmap[(x, sy)] = [(blockno, sz)]
            blockDetails[blockno][0].append((x, sy, sz))
    elif ey != sy: #if the start not equal to the end, we need to iterate this
        for y in range(sy, ey+1):
            if (sx, y) in blockmap:
                blockmap[(sx, y)].append((blockno, sz))
            else: 
                blockmap[(sx, y)] = [(blockno, sz)]
            blockDetails[blockno][0].append((sx, y, sz))
    else:
        for z in range(sz, ez+1):
            if (sx, sy) in blockmap:
                blockmap[(sx, sy)].append((blockno, z))
            else:
                blockmap[(sx, sy)] = [(blockno, z)]
            blockDetails[blockno][0].append((sx, sy, z))
    blockno += 1

for xy in blockmap:
    blockmap[xy].sort(key=lambda block: block[1])

#so now we have loaded all the data, so now we need to run through each block in the list
for block in blockDetails:
    #so for each block, we have the start and end points. we need to iterate through the points of
    #each block, to find the distance to the block below it. For each point, there is a point below
    #and we want to find for its min
    #so we will keep track of the things below, and then add it to the respective stuff after
    #data structure: [(blockno, distance below)]
    below = []
    for point in blockDetails[block][0]:
        x, y, z = point
        #we should find the index of (blockno, z) in (x, y): if the index is 0, we know its the
        #ground, else, there is something below it
        pos = blockmap[(x, y)].index((block, z))
        if pos: #if it is not the first block, we need to find the distance to the block below
            below.append((blockmap[(x,y)][pos-1][0], z-blockmap[(x,y)][pos-1][1]))
    print(block, below)

print(blockmap)
'''