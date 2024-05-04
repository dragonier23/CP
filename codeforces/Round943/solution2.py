testcases = int(input())

for i in range(testcases):
    n, m = map(int, input().split(" "))
    a = list(map(int, input()))
    b = list(map(int, input()))
    k = 0
    for letter in b:
        if k >= len(a):
            break
        if letter == a[k]:
            k += 1
    print(k)
