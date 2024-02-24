import re
#cycle a few times until we hit some sort of stability 
#the answer asks for 10^9 cycles, we can kind of guess it will hit some sort of stability point and cycle
#so we decide to loop to an arbitary point, where we then find the loop cycle
#after finding the loop length, we can find how much we need to go up by to find the same pattern as at 10^9 
#so basically a Recurrance relation thing

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()

def tiltVertical(map, reverse):    
    maximum = [HEIGHT] * WIDTH
    for i in range(0, HEIGHT) if not(reverse) else reversed(range(0, HEIGHT)):
        for j in range(0, WIDTH):
            if map[i][j] == 'O':
                if (reverse):
                    if ((maximum[j] - 1) != i):
                        map[(maximum[j] - 1)][j] = 'O'
                        map[i][j] = '.'
                    maximum[j] -= 1
                else:
                    if ((HEIGHT - maximum[j]) != i):
                        map[(HEIGHT - maximum[j])][j] = 'O'
                        map[i][j] = '.'
                    maximum[j] -= 1
            if map[i][j] == '#':
                maximum[j] = i if reverse else len(file) - i - 1

def tiltHorizontal(map, reverse):    
    maximum = [WIDTH] * HEIGHT
    for i in range(0, WIDTH) if not(reverse) else reversed(range(0, WIDTH)):
        for j in range(0, HEIGHT):
            if map[j][i] == 'O':
                if (reverse):
                    if ((maximum[j] - 1) != i):
                        map[j][(maximum[j] - 1)] = 'O'
                        map[j][i] = '.'
                    maximum[j] -= 1
                else:
                    if ((WIDTH - maximum[j]) != i):
                        map[j][(WIDTH - maximum[j])] = 'O'
                        map[j][i] = '.'
                    maximum[j] -= 1
            if map[j][i] == '#':
                maximum[j] = i if reverse else len(file) - i - 1

def cycle(map):
    tiltVertical(map, False)
    tiltHorizontal(map, False)
    tiltVertical(map, True)
    tiltHorizontal(map, True)

def checkSame(map, tmp):
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if map[i][j] != tmp[i][j]:
                return False
    return True

WIDTH = len(file[0])-1
HEIGHT = len(file)

#storing the system in a 2d array
map = []
for i in range(0, HEIGHT):
    line = []
    for j in range(0, WIDTH):
        line.append(file[i][j])
    map.append(line)

for i in range(1000):
    cycle(map)

tmp = []
for line in map:
    linecopy = []
    for item in line:
        linecopy.append(item)
    tmp.append(linecopy)

cycle(map)

index = 1
while(not(checkSame(map, tmp))):
    index+=1
    cycle(map)
print(index)

equivalent = (1000000000 - 1000)%index
print(equivalent)

for i in range(equivalent):
    cycle(map)

ans = 0
for row in range(HEIGHT):
    for col in range(WIDTH):
        if map[row][col] == 'O':
            ans += (HEIGHT - row)
print(ans)
