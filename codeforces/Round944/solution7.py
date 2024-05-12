def swapable(i, j):
    return i >> 2 == j >> 2

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    sortedArray = [-1] * n
    groups = {}
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
        tmp = {curr}
        toVisit = set(j for j in range(len(a)) if swapable(a[curr], a[j]))
        while toVisit:
            curr = toVisit.pop()
            tmp.add(curr)
            toVisit.union(set(j for j in range(len(a)) if swapable(a[curr], a[j] and not(j in tmp))))
        passed = passed.union(tmp)
        swapSets.append(tmp)
    swapSetElements = list(map(lambda x: sorted([a[e] for e in x]), swapSets))
    sortedArray = []
    for i in range(len(a)):
        for j in range(len(swapSets)):
            if i in swapSets[j]:
                sortedArray.append(swapSetElements[j][0])
                swapSetElements[j].pop(0)
                break
    print(*sortedArray)'''