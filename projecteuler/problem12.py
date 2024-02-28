#we need a total of 502 divisors for (n)(n+1)

def divisorno(num):
    tmp = 0
    for i in range(1, num+1):
        if num % i == 0:
            tmp += 1
    return tmp

answer = None
divisors = 0    
for i in range(1, 20000):
    if i%2 == 0:
        divisors = divisorno(i // 2) * divisorno(i+1)
    else:
        divisors = divisorno((i+1) // 2) * divisorno(i)
    print(i)
    if divisors > 500:
        answer = (i * (i+1)) // 2
        break

print(answer)

'''
first = 1
second = 2
firstdivisor = 1
seconddivisors = 2
while firstdivisor * seconddivisors <= 501: #while the no of divisors is less than 502
    first += 1
    second += 1
    if first%2 == 0: #if first is a even number
        firstdivisor = divisorno(first // 2)
        seconddivisor = divisorno(second)
    else:
        firstdivisor = divisorno(first)
        seconddivisor = divisorno(second // 2)
    #print(first, second)

print((first * second) / 2)
'''






