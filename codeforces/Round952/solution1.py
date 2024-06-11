for i in range(int(input())):
    n, m = input().split(" ")
    print(m[0] + n[1:] + ' ' + n[0] + m[1:])