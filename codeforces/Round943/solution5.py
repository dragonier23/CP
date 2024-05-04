testcases = int(input())

for i in range(testcases):
    n = int(input())
    if n == 2:
        print("1 1")
        print("1 2")
        continue
    a = int((n/2) - 1 if n%2 == 0 else (n-1)/2)
    for i in range(a):
        print(*[1+i, 1])
        print(*[n-i, n-i])
    if n%2 == 0:
        print(*[a+1, 1])
        print(*[1, 2+a])
    else: 
        print(*[1, 1+a])