
def swapable(i, j):
    return i >> 2 == j >> 2

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    sortedArray = [-1] * n
    groups = {}
    #this method of using the dictionary is way faster than the set method: time complexity O(n)
    for i in range(n):
        key = a[i] >> 2 << 2
        if not key in groups:
            groups[key] = {}
        groups[key][i] = a[i]
    for key in groups:
        swapSetElements = sorted(list(groups[key].values()))
        i = 0
        for index in groups[key]:
            sortedArray[index] = swapSetElements[i]
            i += 1
            #this is much faster than pop(0) and creating a new list to replace the old list
    print(*sortedArray)
'''
def swapable(i, j):
    return i >> 2 == j >> 2
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    passed = set()
    swapSets = []
    while len(passed) < n:
        curr = set(i for i in range(n)).difference(passed).pop()
        group = set(j for j in range(len(a)) if swapable(a[curr], a[j]))
        group.add(curr)
        passed = passed.union(group)
        swapSets.append(group)
    swapSetElements = list(map(lambda x: sorted([a[e] for e in x]), swapSets))
    swapSets = list(map(list, swapSets))
    sortedArray = [-1] * n
    for i in range(len(swapSets)):
        for j in range(len(swapSets[i])):
            sortedArray[swapSets[i][j]] = swapSetElements[i][j]
    print(*sortedArray)'''