testcases = int(input())

for i in range(testcases):
    monsterCount = int(input())
    monsterEnergy = list(map(int, input().split(" ")))
    pastEnergy = monsterEnergy.copy()
    while True:
        for i in range(1, len(monsterEnergy)+1):
            monsterEnergy[i%monsterCount] = max(0, monsterEnergy[i%monsterCount] - monsterEnergy[(i-1) % monsterCount])
        if monsterEnergy == pastEnergy:
            break
        else: 
            pastEnergy = monsterEnergy.copy()
    print(len(list(filter(lambda x: x != 0 ,monsterEnergy))))
    for i in range(len(monsterEnergy)):
        if monsterEnergy[i] != 0:
            print(str(i+1) + " ", end="")
    print(" ")
        
