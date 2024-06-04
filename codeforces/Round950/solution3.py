for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    bs = list(map(int, input().split(" ")))
    m = int(input())
    ds = list(map(int, input().split(" ")))
    #print(n)
    consider = False 
    diffs = dict()
    for i in range(n):
        if a[i] != bs[i]:
            if not bs[i] in diffs:
                diffs[bs[i]] = 0
            diffs[bs[i]] += 1
    davailable = dict()
    for d in ds:
        if not d in davailable:
            davailable[d] = 0
        davailable[d] += 1
    for diff in diffs:
        if not diff in davailable:
            print("NO")
            consider = True
            break
        if davailable[diff] < diffs[diff]:
            print("NO")
            consider = True
            break
    if consider:
        continue
    if ds[-1] in bs:
        print("YES")
    else:
        print("NO")
        '''

    breakPoint = m
    for i in range(m):
        if ds[i] in diffs:
            diffs[ds[i]] -= 1
        if diffs:
            if min(list(map(lambda x: True if diffs[x] == 0 else False, diffs))):
                breakPoint = i            
                break
    for i in ds[breakPoint+1:m]:
        if not i in bs:
            print("NO")
            consider = True
            break
    if not consider:
        print("YES")'''