#things to do: 1. split by semicolon, split by space, then detect numbers


filename = 'problemstatement.txt' #'tests1.txt' #

file = open(filename, 'r').readlines()
print(file)

maximum = {'red': 12, 'green': 13, 'blue': 14}
sum = 0
lineno = 1
for line in file:
    lineDone = False
    game = line.split(": ")[1].split("; ")
    print(game)
    for instance in game:
        if lineDone:
            break
        case = instance.split(" ")
        print(case)
        for i in range(0, len(case), 2):
            if lineDone: 
                break
            if 'red' in case[i+1]:
                if int(case[i]) > 12:
                    sum += lineno
                    lineDone = True
                    print(lineno)
            if 'green' in case[i+1]:
                if int(case[i]) > 13:
                    sum += lineno
                    lineDone = True
            if 'blue' in case[i+1]:
                if int(case[i]) > 14:
                    sum += lineno
                    lineDone = True
    lineno += 1

print(sum)
        