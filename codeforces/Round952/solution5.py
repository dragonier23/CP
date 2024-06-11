for i in range(int(input())):
    xm, ym, zm, k = list(map(int, input().split(" ")))
    ans = 0
    for x in range(1, xm + 1):
        if k % x == 0:
            for y in range(1, ym + 1):
                if (k // x) % y == 0:
                    z = k // x // y
                    tmp = (xm - x + 1) * (ym - y + 1) * (zm - z + 1)
                    if tmp > ans:
                        ans = tmp
    print(ans)