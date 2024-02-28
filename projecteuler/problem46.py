import math

def isprime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True

def oddlist(num):
    list = [[],[]]
    for i in range(1, num, 2):
        if isprime(i):
            list[0].append(i)
        else:
            list[1].append(i)
    return list


numbersforconsideration = oddlist(10000)
#print(numbersforconsideration)
for oddcomposite in numbersforconsideration[1]:
    works = False
    for prime in numbersforconsideration[0]:
        if prime > oddcomposite:
            break
        squareornot = (oddcomposite - prime) / 2
        if not(math.sqrt(squareornot)%1):
            #print(oddcomposite, prime)
            works = True 
            break
    if not(works):
        print(oddcomposite)
        break


