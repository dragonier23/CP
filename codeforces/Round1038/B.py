# clearly if the larger than 3x3 its not possible, if its <2 x y or y x < 2 then it will fail 

for i in range(int(input())):
    sum = 0
    for j in range(int(input())):
        a, b, c, d = list(map(int, input().split(" ")))
        sum += max(0, a - c)
        toShift = max(0, b - d) 
        sum += toShift + min(a, c) if toShift > 0 else 0

    print(sum)