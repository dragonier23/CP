testcases = int(input())

for i in range(testcases):
    _, number = map(int, input().split(" "))
    minNumber = list(map(int, input().split(" ")))[0]
    solutions = []
    testcaseList = list(map(int, input().split(" ")))
    for testcase in testcaseList:
        if testcase < minNumber: 
            solutions.append(testcase)
        else: 
            solutions.append(minNumber-1)
    for case in solutions: 
        print(str(case) + " ", end='')
    print(" ")
