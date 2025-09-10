for i in range(int(input())):
    d = input()
    s = list(map(lambda x: int(x), input()))

    zero = 0 
    for tmp in s: 
        if tmp == 0: 
            zero += 1
    res = 0
    for i in range(zero): 
        if s[i] == 1: 
            res += 1
    print(res)