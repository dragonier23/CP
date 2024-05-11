import math

for _ in range(int(input())):
    n, k, q = list(map(int, input().split(" ")))
    a = (list(map(int, input().split(" "))))
    b = (list(map(int, input().split(" "))))
    a.insert(0, 0)
    b.insert(0, 0)
    answer = []
    for _ in range(q):
        d = int(input())
        lower, upper = (0, k)
        mid = 0
        if d == 0:
            answer.append(0)
            continue
        if d == n:
            answer.append(b[k])
            continue
        while True:
            mid = math.floor((upper+lower) / 2)
            if a[mid] == d:
                answer.append(b[mid])
                break
            if a[mid] < d and a[mid+1] > d:
                counter = mid
                break
            if a[mid] > d:
                upper = mid
            else:
                lower = mid            
        if a[mid] == d:
            continue
        ans = b[counter]
        x = d - a[counter]
        ans += ((b[counter + 1] - b[counter]) * x // (a[counter + 1] - a[counter]))
        answer.append(ans)
    print(*answer)