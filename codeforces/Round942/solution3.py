testcases = int(input())

for i in range(testcases):
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    a.sort()
    limit = len(a)
    start, end = (0, len(a))
    while True:
        if k < (a[end] * (end)) - sum(a[:end]) and k > (a[start] * (start)) - sum(a[:start]) and end - start == -1:
            limit = end
            break
        middle = (start + end) // 2
        
    k -= (a[limit-1] * (limit-1)) - sum(a[:(limit-1)])
    toAdd = k // limit
    remainder = k % limit
    print((a[limit-1] + toAdd - 1) * n + 1 + n - limit + remainder)
