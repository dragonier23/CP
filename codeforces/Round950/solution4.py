import math

for i in range(int(input())):
    x = int(input())
    xs = list(map(int, input().split(" ")))
    gcds = [math.gcd(xs[0], xs[1])]
    removed = False
    ans = False
    skipNext = False 
    for i in range(1, x-1):
        if skipNext:
            if i == x-2:
                ans = True
            skipNext = False
            continue
        if math.gcd(xs[i], xs[i+1]) < gcds[-1]:
            if i == x-2:
                if not removed:
                    ans = True
                    break
                else: 
                    break
            if math.gcd(xs[i], xs[i+2]) >= gcds[-1]:
                if removed: 
                    break
                else: 
                    gcds.append(math.gcd(xs[i], xs[i+2]))
                    skipNext = True
                    removed = True
            else:
                break
        else:
            gcds.append(math.gcd(xs[i], xs[i+1]))
        if i == x-2:
            ans = True
    if ans:
        print("YES")
        continue
    gcds = [math.gcd(xs[-1], xs[-2])]
    removed = False
    ans = False
    skipNext = False 
    for i in range(x-2, 0, -1):
        if skipNext:
            if i == 1:
                ans = True
            skipNext = False
            continue    
        if math.gcd(xs[i], xs[i-1]) > gcds[-1]:
            if i == 1:
                if not removed:
                    ans = True
                    break
                else: 
                    break
            if math.gcd(xs[i], xs[i-2]) <= gcds[-1]:
                if removed: 
                    break
                else: 
                    gcds.append(math.gcd(xs[i-2], xs[i]))
                    removed = True
                    skipNext = True
            else:
                break
        else:
            gcds.append(math.gcd(xs[i], xs[i-1]))
        if i == 1:
            ans = True
    if ans:
        print("YES")
    else: 
        print("NO")
#edge case where first is too high only and last is too low only 