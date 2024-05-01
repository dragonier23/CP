testcases = int(input())

for i in range(testcases):
    length = int(input())
    As = list(map(int, input().split(" ")))
    Bs = list(map(int, input().split(" ")))
    answer = []
    for j in range(length):
        check = False
        for k in range(j, length):
            if As[j] <= Bs[k]:
                answer.append((k-j))
                check = True
                break
        if not check: 
            answer.append(length - j)
    print(max(answer))
