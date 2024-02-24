import re
import math

#so we have a few assumptions: start row and col, first row and col, last row and col are empty
#hence the shortest path to reach an adjacent block will be the manhattan distance to get to that
#particular corner / side thing
# assumption 2: reaches the end

#so now we need to calculate the number of odd / even squares, and the corner things

def visitSquare(row, col, steps):    
    # 2 sets here: one for curr locations, one of loct to visit
    curr = set()
    toVisit = set()
    curr.add((row, col))

    #so now we need to visit
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(steps):
        for location in curr:
            row, col = location
            for movement in directions:
                #if the next space is within the boundaries
                if row+movement[0] >= 0 and row+movement[0] < len(gardenMap) and col+movement[1] >= 0 and col+movement[1] < len(gardenMap[0]): 
                    if gardenMap[row+movement[0]][col+movement[1]] != '#':
                        toVisit.add((row+movement[0], col+movement[1]))
        curr = toVisit
        toVisit = set()
    return len(curr)


filename = 'problemstatement.txt' #'test.txt' #
file = open(filename, 'r').readlines()  
gardenMap = [line.strip() for line in file]
    
WIDTH = len(gardenMap[0])
HEIGHT = len(gardenMap)
    
# we need to identify the start point
for i in range(HEIGHT):
    for j in range(WIDTH):
        if gardenMap[i][j] == 'S':
            start = (i, j)
            break
row, col = start

STEPS = 26501365
#number of odd squares: 
oddSquare = visitSquare(row, col, ((HEIGHT+WIDTH+1)//2*2)+1)
evenSquare = visitSquare(row, col, ((HEIGHT+WIDTH+1)//2*2)+2)

reach = math.floor(((STEPS-65) / WIDTH)) - 1
oddCount = reach**2 if reach%2 else (reach+1)**2
evenCount = (reach+1)**2 if reach%2 else reach**2

top = visitSquare(HEIGHT-1, col, HEIGHT-1)
bottom = visitSquare(0, col, HEIGHT-1)
left = visitSquare(row, 0, HEIGHT-1)
right = visitSquare(row, WIDTH-1, HEIGHT-1)

smallTopRight = visitSquare(HEIGHT-1, 0, HEIGHT-67)
largeTopRight = visitSquare(HEIGHT-1, 0, (HEIGHT*2)-67)
smallTopLeft = visitSquare(HEIGHT-1, WIDTH-1, HEIGHT-67)
largeTopLeft = visitSquare(HEIGHT-1, WIDTH-1, (HEIGHT*2)-67)
smallBottomRight = visitSquare(0, 0, HEIGHT-67)
largeBottomRight = visitSquare(0, 0, (HEIGHT*2)-67)
smallBottomLeft = visitSquare(0, WIDTH-1, HEIGHT-67)
largeBottomLeft = visitSquare(0, WIDTH-1, (HEIGHT*2)-67)

print((oddCount*oddSquare) + (evenCount*evenSquare)
      + bottom + top + left + right
      + (reach+1) * (smallBottomLeft + smallBottomRight + smallTopLeft + smallTopRight)
      + reach * (largeBottomLeft + largeBottomRight + largeTopLeft + largeTopRight))

# version 1 that didnt work: still too much calculations
'''
#alot more to consider here, but what we can do is to consider 2 steps at a time
#because the tiles already visit will basically alternate, so what we need to do is visit 26502365 / 2
#times. To cut the nummber of plots we need to check, we should only look for the neighbours of newly 
#visited plots

#i think we need to have 2 sets:
#one already visited
#one newly visited
#one to be visited
#psuedocode for this: 1. newly visited should be at the borders, which mean the nodes visited from there
#should be unvisited previously. Hence, visit the new nodes, adding them to a new set --> this is the 
#next newly visited, we should also add this to the already visited list, to check if we have visited
#this node before

CYCLES = 5000

def main():
    filename = 'test.txt' #'problemstatement.txt' #
    file = open(filename, 'r').readlines()
    gardenMap = [line.strip() for line in file]
    
    WIDTH = len(gardenMap[0])
    HEIGHT = len(gardenMap)
    
    # we need to identify the start point
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if gardenMap[i][j] == 'S':
                start = (i, j)
                break
    

    # 2 sets here: one for curr locations, one of loct to visit
    visited = set()
    newlyVisited = set()
    tmp = set()
    newlyVisited.add(start)
    visited.add(start)

    #so now we need to visit
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if CYCLES%2: #if no of cycles is odd
        row, col = start
        for direction in directions:
            if gardenMap[row+direction[0]][col+direction[1]] != '#':
                tmp.add((row+direction[0], col+direction[1]))
        visited = tmp
        newlyVisited = tmp
        tmp = set()

    directions = [(2, 0), (0, 2), (-2, 0), (0, -2), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for i in range(math.floor(CYCLES/2)):
        for location in newlyVisited:
            row, col = location
            for movement in directions:
                if gardenMap[(row+movement[0])%HEIGHT][(col+movement[1])%WIDTH] != '#' and not((row+movement[0], col+movement[1]) in visited): 
                    tmp.add((row+movement[0], col+movement[1]))
                    visited.add((row+movement[0], col+movement[1]))
        newlyVisited = tmp
        tmp = set()

    print(len(visited))


if __name__ == '__main__':
    main()

    '''