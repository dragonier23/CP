import re
#alot more to consider here, but what we can do is to consider 2 steps at a time

def main():
    filename = 'problemstatement.txt' #'test.txt' #
    file = open(filename, 'r').readlines()
    gardenMap = [line.strip() for line in file]
    
    # we need to identify the start point
    for i in range(len(gardenMap)):
        for j in range(len(gardenMap[0])):
            if gardenMap[i][j] == 'S':
                start = (i, j)
                break

    # 2 sets here: one for curr locations, one of loct to visit
    curr = set()
    toVisit = set()
    curr.add(start)

    #so now we need to visit
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(202):
        for location in curr:
            row, col = location
            for movement in directions:
                #if the next space is within the boundaries
                if row+movement[0] >= 0 and row+movement[0] < len(gardenMap) and col+movement[1] >= 0 and col+movement[1] < len(gardenMap[0]): 
                    if gardenMap[row+movement[0]][col+movement[1]] != '#':
                        toVisit.add((row+movement[0], col+movement[1]))
        curr = toVisit
        toVisit = set()

    print(len(curr))


if __name__ == '__main__':
    main()