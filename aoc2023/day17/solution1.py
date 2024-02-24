from heapq import heappop, heappush

def checkValid(node, map): #checks if the node we are selecting is valid
    return node[0] in range(len(map)) and node[1] in range(len(map[0]))

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()
HEIGHT = len(file)
WIDTH = len(file[0]) - 1
MIN = 1
MAX = 3

heatmap = [[int(node) for node in row[:-1]] for row in file]
#we will let 0  be right, 1 be down, 2 for left and 3 for up
movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#we will basically have a list that keeps track of the nodes to be visited
#structure of stuff inside: x, y, distance, disalloweddirection
heapqueue = [(0, 0, 0, -1)]

#so here we have 3 data structures: 
#1. distance, which is a dictionary with the distance to each node
#2. the queue, which will hold the ranking of the distances
#3. the seen, which is visited nodes
#4. the heatmap
visited = set()
distance = {}

while heapqueue:#while the queue is not empty
    row, col, dist, disallowedDirection = heappop(heapqueue)
    if row == HEIGHT - 1 and col == WIDTH - 1:
        print(dist)
        break
    if (row, col, disallowedDirection) in visited:
        continue
    visited.add((row, col, disallowedDirection))

    #so now we need to consider the neighbours
    for direction in range(4):
        costIncrease = 0
        if direction == disallowedDirection or (direction+2) % 4 == disallowedDirection:
            continue
        
        for steps in range(1, MAX + 1):
            neighbourrow = row+(movement[direction][0]*steps)
            neighbourcol = col+(movement[direction][1]*steps)
            if checkValid((neighbourrow, neighbourcol), heatmap):
                #so if we have found a neighbour that is valid, we should check it
                costIncrease += heatmap[neighbourrow][neighbourcol]
                if steps < MIN:
                    continue
                tmpCost = costIncrease + dist
                if distance.get((neighbourrow, neighbourcol, direction), 1e100) <= tmpCost:
                    continue
                distance[(neighbourrow, neighbourcol, direction)] = tmpCost
                heappush(heapqueue, (neighbourrow, neighbourcol, tmpCost, direction))