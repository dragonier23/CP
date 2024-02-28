import math

def countDigit(n): 
    return math.floor(math.log10(n)+1) 

first = 1
second = 1
index = 2
while True:
    tmp = second
    second = first + second
    first = tmp
    index += 1
    if countDigit(second) >= 1000:
        break
    print(second)

print(index)
    