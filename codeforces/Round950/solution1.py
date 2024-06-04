for i in range(int(input())):
    n, m = list(map(int, input().split(" ")))
    x = input()
    present = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0}
    for letter in x:
        present[letter] += 1
    ans = 0
    for letter in present: 
        if present[letter] < m:
            ans += (m - present[letter])
    print(ans)