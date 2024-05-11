for i in range(int(input())):
    x = list(map(int, input()))
    ans = 0
    counter = 0
    increment = False
    while counter < (len(x) - 1):
        if x[counter] == x[counter+1]:
            counter += 1
        elif x[counter] == 1:
            ans += 1
            counter += 1
        elif x[counter] == 0 and not(increment):
            counter += 1
            increment = True
        else: 
            ans += 1
            counter += 1
    print(ans+1)