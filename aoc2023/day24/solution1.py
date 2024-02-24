import re
from collections import deque

filename = 'problemstatement.txt' # 'test.txt' # 
file = open(filename, 'r').readlines()

#lines are either: parallel, skew, or intersecting

paths = [list(map(int, line.strip().replace(" @ ", ", ").split(", "))) for line in file]

LOWER = 200000000000000
UPPER = 400000000000000

#essentially solving 2 lines
ans = 0
for i in range(len(paths)):
    Ax, Ay, Az, Adx, Ady, Adz = paths[i]
    for j in range(i):
        Bx, By, Bz, Bdx, Bdy, Bdz = paths[j]
        if Adx / Bdx == Ady / Bdy: #and Adx / Bdx == Adz / Bdz:
            continue #if parallel, we dont consider it anymore
        # ax + tadx = bx + sbdx
        # ay + tady = by + sbdy
        # az + tadz = bz + sbdz
        s = (Ay - By + ((Ady*Bx) / Adx) - ((Ax * Ady) / Adx))  / ( Bdy - ((Ady * Bdx) / Adx))
        t = (Bx + (Bdx * s) - Ax) / Adx
        # so now we need to check if the results are consistent
        if (Ax + t*Adx) >= LOWER and (Ax + t*Adx) <= UPPER and (Ay + t *Ady) >= LOWER and (Ay + t *Ady) <= UPPER and t >= 0 and s >= 0:
            ans += 1
        #if (Az + t * Adz) == (Bz + s * Bdz): 
            #ans += 1

print(ans)