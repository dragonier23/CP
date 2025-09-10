for i in range(int(input())):
    n = int(input())
    a = list(map(lambda x: int(x), input().split(" ")))

    if n == 1: 
        print(a[0])
        continue 

    if n == 2: 
        if a[0] > a[1]: 
            print(a[0] - a[1]) 
            continue 
        else: 
            print(1 + a[1] - a[0])            
            continue 

    # else, we have a situation where we have 3 or more.
    # if alice is winning, swapping will boost her score as much as she wants. she will swap to maximise cost and difference. if swapping with bob dosent work, she will swap internally to increase, and bob will have to accept. 

    # if bob is winning, alice will still try to maximise, but bob shld always accept
    
    # res = 0
    # for i in range(n): 
    #     res += a[i] if i % 2 == 0 else 0-a[i]

    # maximum = 0 
    # for i in range(0, n, 2): 
    #     for j in range(1, n, 2): 
    #         curr = 2 * (a[j] - a[i]) + abs(i - j)
    #         if curr > maximum: 
    #             maximum = curr
    # if maximum < (n - 2 if n % 2 == 0 else n - 1): 
    #     maximum = n - 2 if n % 2 == 0 else n - 1

    # print(res + maximum)
    # # so alice, will always swap; that always adds to her score, unless swapping decreases her score. swap to 
    # if bob is winning, alice will always try to swap to maximise
    # 

    res = 0
    for i in range(n):
        res += a[i] if i % 2 == 0 else -a[i]

    # Precompute
    prefix_min = [float("inf")] * n
    suffix_max = [float("-inf")] * n

    cur_min = float("inf")
    for i in range(n):
        if i % 2 == 0:
            cur_min = min(cur_min, 2*a[i] + i)
        prefix_min[i] = cur_min

    cur_max = float("-inf")
    for i in range(n-1, -1, -1):
        if i % 2 == 0:
            cur_max = max(cur_max, -2*a[i] + i)
        suffix_max[i] = cur_max

    maximum = 0
    for j in range(n):
        if j % 2 == 1:  # odd index
            if prefix_min[j] != float("inf"):
                maximum = max(maximum, (2*a[j] + j) - prefix_min[j])
            if suffix_max[j] != float("-inf"):
                maximum = max(maximum, suffix_max[j] - (-2*a[j] + j))

    # Compare with baseline
    limit = n-2 if n % 2 == 0 else n-1
    maximum = max(maximum, limit)

    print(res + maximum)
