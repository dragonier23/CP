import re
from collections import deque

filename = 'problemstatement.txt' #  'test.txt' #
file = open(filename, 'r').readlines()
 
maze = [line.strip() for line in file]
HEIGHT = len(maze)
WIDTH = len(maze[0])

START = (0, 1, 0, []) #row, col, step, visited
END = (HEIGHT-1, WIDTH-2)

#we will implement a BFS to look for the end point
q = deque([START])

max = 0
while q:
    row, col, steps, visited = q.popleft()
    if (row, col) == END:
        if steps > max:
            max = steps
    newVisited = visited.copy()
    newVisited.append((row, col))
    if row-1 in range(0, HEIGHT):
        if not((row-1, col) in visited):
            if maze[row-1][col] == '.' or maze[row-1][col] == '^':
                q.appendleft((row-1, col, steps+1, newVisited))
    if row+1 in range(0, HEIGHT):
        if not((row+1, col) in visited):
            if maze[row+1][col] == '.' or maze[row+1][col] == 'v':
                q.appendleft((row+1, col, steps+1, newVisited))
    if col-1 in range(0, WIDTH):
        if not((row, col-1) in visited):
            if maze[row][col-1] == '.' or maze[row][col-1] == '<':
                q.appendleft((row, col-1, steps+1, newVisited))
    if col+1 in range(0, WIDTH):
        if not((row, col+1) in visited):
            if maze[row][col+1] == '.' or maze[row][col+1] == '>':
                q.appendleft((row, col+1, steps+1, newVisited))

print(max)