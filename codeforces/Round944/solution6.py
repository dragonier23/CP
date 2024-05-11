import math

def intPoints(r):
    quadrant = 0
    for x in range(1, r):
        y = math.sqrt(r**2 - x**2)
        yint = math.floor(y)
        quadrant += (yint if y-yint else yint - 1)  
    return (quadrant+(r-1))*4 + 1

for _ in range(int(input())):
    r = int(input())
    print(intPoints(r+1) - intPoints(r))