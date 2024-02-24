import re
from collections import deque

filename = 'problemstatement.txt' # 'test.txt' # 
file = open(filename, 'r').readlines()
 
maze = [line.strip() for line in file]
HEIGHT = len(maze)
WIDTH = len(maze[0])

# we need to create a graph, probably with a hashmap: 
# we find the intersections, finding the distance to the adjacent intersections
# we then run a DFS on the graph

#each path in the intersection will lead to either: 1. a dead end or 2. another intersection
#lets first find the intersections
START = (0, 1)
END = (HEIGHT-1, WIDTH-2)

intersections = [START, END]
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
acceptable = ['.', '<', '>', '^', "v"]
for row in range(1, HEIGHT-1):
    for col in range(1, WIDTH-1):
        if maze[row][col] in acceptable:
            paths = 0
            for direction in directions:
                drow, dcol = direction
                if maze[row+drow][col+dcol] in acceptable:
                    paths += 1
            if paths >= 3:
                intersections.append((row, col))

path = dict() #key: [adjacent nodes, in shape: (row, col), steps]
# we now need to find the paths between 
for intersection in intersections:
    #we want to search the avaliable directions, to find the path
    path[intersection] = set()
    q = [(intersection[0], intersection[1], 0)]
    visited = set()
    while q:
        q.sort(key=lambda x: x[1])
        curr = q.pop(0)
        row, col, steps = curr
        if (row, col) in intersections and (row, col) != intersection:
            path[intersection].add(((row, col), steps))
            continue
        visited.add((row, col))
        for direction in directions:
            drow, dcol = direction
            if row+drow in range(HEIGHT) and col+dcol in range(WIDTH):
                if maze[row+drow][col+dcol] in acceptable and not((row+drow, col+dcol) in visited):
                    q.append((row+drow, col+dcol, steps+1))


#so now, we can do a bfs on this
q = deque([((0, 1), 0, [])]) #queue has structure: coordinates, steps, visited
max = 0
while q:
    curr, steps, visited = q.popleft()
    if curr == END:
        if steps > max:
            max = steps
            continue
    newVisited = visited.copy()
    newVisited.append(curr)
    for neighbour in path[curr]:
        next, Nsteps = neighbour
        if not(next in newVisited):
            q.appendleft((next, steps+Nsteps, newVisited))

print(max)