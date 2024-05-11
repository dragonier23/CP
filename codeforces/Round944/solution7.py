def swapable(i, j):
    return i >> 2 == j >> 2

def search(mapping, curr):
    if mapping[curr] == []:
        return [curr]
    ans = []
    for x in mapping[curr]:
        ans = ans + search(mapping, x)
    return [curr] + ans

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    potentialSwaps = [list(j for j in range(i+1, len(a)) if i != j and swapable(a[i], a[j]))for i in range(len(a))]
    #this feels like some sort of graph traversal: lets do a bfs
    swapSets = []
    passed = set()
    for c in range(len(a)):
        if not(c in passed):
            tmp = set(search(potentialSwaps, c))
            swapSets.append(tmp)
            passed = passed.union(tmp)
    #we now have the sets of swappables, and their indices
    #for each element, we need to find the smallest in the set, and then 
    swapSetElements = list(map(lambda x: sorted([a[e] for e in x]), swapSets))
    sortedArray = []
    for i in range(len(a)):
        for j in range(len(swapSets)):
            if i in swapSets[j]:
                sortedArray.append(swapSetElements[j][0])
                swapSetElements[j].pop(0)
    print(*sortedArray)