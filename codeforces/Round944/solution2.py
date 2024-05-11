for i in range(int(input())):
    x = list(input())
    if len(set(x)) == 1: 
        print("NO")
    else:
        print("YES")
        for i in range(len(x) - 1):
            if x[i] != x[i+1]:
                tmp = x[i]
                x[i] = x[i+1]
                x[i+1] = tmp
                print(''.join(x))
                break
