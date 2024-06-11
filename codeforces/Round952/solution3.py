for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split(" ")))
    ans = 0
    total = 0
    inSet = set()
    for i in range(n):
        inSet.add(a[i])
        total += a[i]
        if total % 2 == 0:
            check = total / 2
            if check in inSet:
                ans += 1
    print(ans)