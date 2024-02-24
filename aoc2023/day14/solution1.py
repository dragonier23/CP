import re

filename = 'problemstatement.txt' #'test.txt' #

file = open(filename, 'r').readlines()

maximum = [len(file)] * (len(file[0]) - 1)

ans = 0
for i in range(0, len(file)):
    for j in range(0, len(file[0])-1):
        if file[i][j] == 'O':
            ans += maximum[j]
            maximum[j] -= 1
        if file[i][j] == '#':
            maximum[j] = len(file) - i - 1

print(ans)
