testcases = int(input())

for i in range(testcases):
    n = int(input())
    xs = list(map(int, input().split(" ")))
    a = [501]
    for x in xs:
        a.append((x % a[-1]) + a[-1])
    print(*a)
    #print(str(map(lambda x: str(x) + " ")), end="")
    
        
