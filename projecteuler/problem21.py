def divisorsum(num):
    sum = 0
    for i in range(1, num-1):
        if num%i == 0:
            sum += i
    return sum

total = 0
for i in range(1, 10000):
    tmp = divisorsum(i)
    if divisorsum(tmp) == i and tmp != i:
        total += i
        print(i)

print(total)