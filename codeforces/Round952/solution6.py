import math

for i in range(int(input())):
    h, n = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    c = list(map(int, input().split(" ")))
    lcm = 1
    for i in range(n):
        lcm = math.lcm(lcm, c[i])
    lcmTotal = sum([a[i] * (lcm // c[i]) for i in range(n)])
    if h % lcmTotal == 0:
        ans = lcm * ((h // lcmTotal) - 1)
        left = h - (((h // lcmTotal) - 1)* lcmTotal)
    else:
        ans = lcm * (h // lcmTotal)
        left = h - ((h // lcmTotal) * lcmTotal)
    
    print(ans)
