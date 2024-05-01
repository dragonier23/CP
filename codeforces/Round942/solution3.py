testcases = int(input())

def minNo(xs):
    return sum([1 if xs[i] == min(xs) else 0 for i in range(len(xs))])

def exceedMininRow(xs):
    minimum = min(xs)
    inARow = 0
    tmp = 0
    for i in range(len(xs) * 2):
        if xs[i%len(xs)] > minimum:
           tmp += 1
           if tmp > inARow:
               inARow = tmp
        else: 
            tmp = 0     
    return inARow

def decideRemaining(start, k, xs):
    if k == 0:
        return exceedMininRow(xs)
    if minNo(xs[start:]) == k:
        tmp = xs.copy()
        for i in range(start, len(xs)):
            if tmp[i] == min(xs):
                tmp[i] += 1
        return exceedMininRow(tmp)
    tmp2 = xs.copy()
    for i in range(start, len(xs)):
        if tmp2[i] == min(xs):
            tmp2[i] += 1
            newStart = i + 1
            break
    return max(decideRemaining(newStart, k-1, tmp2), decideRemaining(newStart, k, xs))

for i in range(testcases):
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    while k > 0:
        minimum = min(a)
        minCount = minNo(a)
        if k >= minCount: 
        # if the number of cards we can buy exceeds that of the total number of minimuns, we can add one to all of them 
            for x in range(n):
                if a[x] == minimum:
                    a[x] += 1 
            k -= minCount
            additional = exceedMininRow(a) 
        else: 
            #here we need to decide which specific cards to purchase
            additional = decideRemaining(0, k, a)
            k = 0
    print((min(a)-1)*n + 1 + additional)

