testcases = int(input())

for i in range(testcases):
    n, k = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    a.sort()
    limit = len(a)
    if k > ((a[n-1] * n) - sum(a)):
        limit = n
    else: 
        start = 0
        end = n-1
        while True:
            mid = (start + end + 1) // 2
            if k == (a[mid] * (mid)) - sum(a[:mid]):
                limit = mid + 1
                break
            if k < (a[mid] * (mid)) - sum(a[:mid]) and k > (a[mid-1] * (mid-1)) - sum(a[:mid-1]):
                limit = mid
                break
            '''
            if end - start == 1: 
                limit = end
                additional = 0
                while a[limit] == a[limit + 1]:
                    additional += 1
                if additional:
                    limit += additional + 1
                break'''
            if k < (a[mid] * (mid)) - sum(a[:mid]):
                end = mid
            else: 
                start = mid            
    k -= (a[limit-1] * (limit-1)) - sum(a[:(limit-1)])
    toAdd = k // limit
    remainder = k % limit
    print((a[limit-1] + toAdd - 1) * n + 1 + n - limit + remainder)
