testcases = int(input())

for i in range(testcases):
    x = list(map(int, input().split(" ")))
    x = sorted(x)
    print(*x)