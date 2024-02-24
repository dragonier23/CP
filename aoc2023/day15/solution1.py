import re

filename = 'test.txt' #'problemstatement.txt' #

def hash(valList):
    if not(valList):
        return 0
    else:
        return ((ord(valList[-1]) + hash(valList[:-1])) * 17 ) % 256


ans = sum(map(hash, (open(filename, 'r').readlines())[0].split(",")))

print(ans)
