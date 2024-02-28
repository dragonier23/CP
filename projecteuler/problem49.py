import math

def isprime(num):
    for i in range(2, int(math.sqrt(num))):
        if num%i == 0:
            return False
    return True

for i in range(1488, 3401):
    if isprime(i):
        print(i)
        b = i + 3330
        c = i + 6660
        if isprime(b) and isprime(c):
            #now we need to check if it is a palidrome
            adigits = {i // 1000, (i%1000) // 100, (i%100) // 10, i%10}
            bdigits = {b // 1000, (b%1000) // 100, (b%100) // 10, b%10}
            cdigits = {c // 1000, (c%1000) // 100, (c%100) // 10, c%10}
            print(adigits, bdigits, cdigits)
            if adigits == bdigits and bdigits == cdigits:
                print(i, b, c)
                break