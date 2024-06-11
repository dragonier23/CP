for i in range(int(input())):
    n = int(input())
    ans = 0
    sol = 1
    for x in range(2, n + 1):
        k = n // x
        tmp = k * (k + 1) * x / 2 
        if tmp > ans:
            ans = tmp
            sol = x
    print(sol)