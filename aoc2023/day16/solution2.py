import re
#should basically be another djiksta algo
#plan is to store a list of visited nodes, and the unvisited nodes
#so we will store it as such [(visited node), (direction of travel)] --> because if we can find this again
#we know we are in a loop, hence should escape --> we should move on to another node
#so lets assigned the direction of travel: 0 is right, 1 is down, 2 is left, 3 is up

def next(currNode, map):
    row, col, direction = currNode
    movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if map[row][col] == '.': #if its a dot, we move in the existing direction
        return [(row+movement[direction][0], col+movement[direction][1], direction)]
    if map[row][col] == '/':
        if direction == 0:
            return [(row+movement[3][0], col+movement[3][1], 3)]
        if direction == 1: 
            return [(row+movement[2][0], col+movement[2][1], 2)]
        if direction == 2: 
            return [(row+movement[1][0], col+movement[1][1], 1)]
        if direction == 3: 
            return [(row+movement[0][0], col+movement[0][1], 0)]
    if map[row][col] == '\\':
        if direction == 0:
            return [(row+movement[1][0], col+movement[1][1], 1)]
        if direction == 1: 
            return [(row+movement[0][0], col+movement[0][1], 0)]
        if direction == 2: 
            return [(row+movement[3][0], col+movement[3][1], 3)]
        if direction == 3: 
            return [(row+movement[2][0], col+movement[2][1], 2)]
    if map[row][col] == '|':
        if direction == 0 or direction == 2:
            return [(row+movement[1][0], col+movement[1][1], 1), (row+movement[3][0], col+movement[3][1], 3)]    
        return [(row+movement[direction][0], col+movement[direction][1], direction)]
    if map[row][col] == '-':
        if direction == 1 or direction == 3:
            return [(row+movement[0][0], col+movement[0][1], 0), (row+movement[2][0], col+movement[2][1], 2)]    
        return [(row+movement[direction][0], col+movement[direction][1], direction)]
    
def pathCount(start, map):
    toVisit = [start]
    visited = set()

    while toVisit: #while our to visit list is not empty, continue visiting
        curr = toVisit.pop(0)
        visited.add(curr)

        nextNodes = next(curr, map)
        for node in nextNodes:
            #check for validity of the next node
            if node[0] >= 0 and node[0] < HEIGHT and node[1] >= 0 and node[1] < WIDTH:
                #if it a valid list, we want to add it to the list of nodes to visit 
                #IF we havent already visited this node from this direction
                if not(node in visited):
                    toVisit.insert(0, node)

    energized = set()
    for node in visited:
        if not((node[0], node[1]) in energized):
            energized.add((node[0], node[1]))

    return len(energized)

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()
WIDTH = len(file[0]) - 1
HEIGHT = len(file)

mostEnergy = 0
for col in range(0, WIDTH):
    curr = pathCount((0, col, 1), file)
    if curr > mostEnergy:
        mostEnergy = curr
    curr = pathCount((HEIGHT-1, col, 3), file)
    if curr > mostEnergy:
        mostEnergy = curr

for row in range(0, HEIGHT):
    curr = pathCount((row, 0, 0), file)
    if curr > mostEnergy:
        mostEnergy = curr
    curr = pathCount((row, WIDTH-1, 2), file)
    if curr > mostEnergy:
        mostEnergy = curr

print(mostEnergy)
#print(visited)

