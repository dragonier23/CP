for i in range(int(input())):
    n, m = list(map(int, input().split(" ")))
    stored = []
    maximum = 0
    row = 0
    for i in range(n):
        string = list(input())
        hashCount = sum(map(lambda x: 1 if x == "#" else 0, string))
        if hashCount > maximum:
            maximum = hashCount
            stored = string
            row = i
        if hashCount < maximum:
            for _ in range(n - i - 1):
                input()
            break
    col = 0
    for j in range(m):
        if stored[j] == ".":
            col += 1
        if stored[j] == "#":
            print(str(row + 1) + " " + str((maximum // 2) + col + 1))
            break
    