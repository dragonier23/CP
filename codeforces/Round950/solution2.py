for i in range(int(input())):
    n, f, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    f = a[f-1]
    newA = dict()
    for num in a:
        if not (num in newA):
            newA[num] = 0
        newA[num] += 1
    newA = list(map(lambda x: (x, newA[x]), newA))
    lowerBound = 0
    upperBound = 0
    for num in newA: 
        number, count = num
        if number > f:
            lowerBound += count
        if number == f:
            upperBound += count
    upperBound += lowerBound
    if k >= upperBound: 
        print("YES")
    elif k <= lowerBound:
        print("NO")
    else: 
        print("Maybe")