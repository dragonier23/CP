for i in range(int(input())):
    n = int(input())

    res = 0 
    
    segments = []
    for j in range(n): 
        segment = list(map(lambda x: int(x), input().split(" ")))
        start, end = segment[0], segment[1]

        segments.append([start, end, False])
        res += end - start 

    byStart = sorted(segments, key=lambda x: x[0])    
    byEnd = sorted(segments, key=lambda x: x[1])

    start, end = 0, n-1

    passed = 0 
    while passed < (n // 2): 
        if byStart[start][2]: 
            start += 1

        if byEnd[end][2]: 
            end -=1 
        
        passed += byEnd[end][1] - byStart[start][0]
        
        



