testcases = int(input())

def maxScore(a, p, moves, start):
    n = min(len(a), moves)
    tmp = [(a[start-1], a[start-1] * moves)]
    start = p[start-1]
    for i in range(1, n):
        previous, _ = tmp[-1]
        tmp.append((previous + a[start-1], previous + a[start-1] * (moves - i)))
        start = p[start-1]
    return max(list(map(lambda x: x[1], tmp)))

for i in range(testcases):
    n, k, pb, ps = map(int, input().split(" "))
    p = list(map(int, input().split(" ")))
    a = list(map(int, input().split(" ")))
    sb = maxScore(a, p, k, pb)
    ss = maxScore(a, p, k, ps)
    if sb > ss:
        print("Bodya")
    elif sb == ss:
        print("Draw")
    else:
        print("Sasha")