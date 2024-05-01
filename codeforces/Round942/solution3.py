testcases = int(input())

for i in range(testcases):
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    a.sort()
    limit = len(a)
    for i in range(1, len(a)):
        if k < (a[i] * (i)) - sum(a[:i]):
            limit = i
            break
    k -= (a[limit-1] * (limit-1)) - sum(a[:(limit-1)])
    toAdd = k // limit
    remainder = k % limit
    print((a[limit-1] + toAdd - 1) * n + 1 + n - limit + remainder)
