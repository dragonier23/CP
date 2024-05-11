for i in range(int(input())):
    a, b, c1, d1 = list(map(int, input().split(" ")))
    c = min(c1, d1)
    d = max(c1, d1)
    if a > c and a < d and (b > d or b < c):
        print("YES")
    elif b > c and b < d and (a > d or a < c):
        print("YES")   
    else:
        print("NO")