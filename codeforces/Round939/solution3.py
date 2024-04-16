testcases = int(input())

for i in range(testcases):
    rowCount = int(input())
    if rowCount == 1:
        print("1 1\n1 1 1")
        continue
    if rowCount == 2:
        print("7 3\n1 1 1 2\n1 2 1 2\n2 1 1 2")
        continue
    maximalSum = 0
    numCount = 1
    for i in range(1, rowCount + 1):
        maximalSum += i * numCount
        numCount += 2
    print(str(maximalSum) + " " + str(rowCount*2))
    permutation = ''.join(list(map((lambda x: str(x) + " "), range(1, rowCount + 1))))
    for i in range(rowCount, 0, -1):
        print("1 " + str(i) + " " + permutation)
        print("2 " + str(i) + " " + permutation)