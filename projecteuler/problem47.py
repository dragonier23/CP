#we can attempt to do some sort of sieving to find

potentialnumber = [0] * 200000

longestrun = 0
for i in range(2, 200000):
    if potentialnumber[i] == 0: #this number is a prime
        for j in range(2*i, 200000, i):
            potentialnumber[j] += 1
    elif potentialnumber[i] == 4:
        longestrun += 1
    else:
        longestrun = 0
    
    if longestrun == 4:
        print(potentialnumber)
        print(i - 3)
        break

