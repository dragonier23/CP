for i in range(int(input())):
    n, m = input().split(" ")
    print("NO" if int(n) <= 2 or int(m) <= 2 else "YES")
