import math

testcases = int(input())

for i in range(testcases):
    x = int(input())
    maximum = 0
    y = 5
    for j in range(1, x):
        if math.gcd(x, j) + j > maximum:
            maximum = math.gcd(x, j) + j
            y = j
    print(y)