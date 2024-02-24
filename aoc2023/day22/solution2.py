import re
from collections import deque

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

supporting = [] 
for index, block in enumerate(blockmap):
    supporting.append([set(), set()]) # supported by, supporting
    for indexBelow, below in enumerate(blockmap[:index]):
        if intersect(below, block) and below[5] == block[2]-1: #if the blocks lie on top of each other
            supporting[index][0].add(indexBelow) #this tells us for the nth index block, what it is being supported by
            supporting[indexBelow][1].add(index)

total = 0

#we basically move up, checking if we remove one block which of the blocks above it are no longer supported 
for i in range(len(supporting)):
    q = deque(supported for supported in supporting[i][1] if len(supporting[supported][0]) == 1)
    falling = set(q)
    falling.add(i)

    while q:
        supported = q.popleft()
        for j in supporting[supported][1] - falling:
            if supporting[j][0] <= falling:
                q.append(j)
                falling.add(j)
    total += len(falling) - 1
print(total)