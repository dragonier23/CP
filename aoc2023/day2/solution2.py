#things to do: 1. split by semicolon, split by space, then detect numbers


filename = 'problemstatement.txt'  #'test2.txt' #

file = open(filename, 'r').readlines()
print(file)

sum = 0
for line in file:
    maximum = {'red': 0, 'green': 0, 'blue': 0}
    game = line.split(": ")[1].split("; ")
    print(game)
    for instance in game:
        case = instance.split(" ")
        for i in range(0, len(case), 2):
            if 'red' in case[i+1]:
                if int(case[i]) > maximum['red']:
                    maximum['red'] = int(case[i])
            if 'green' in case[i+1]:
                if int(case[i]) > maximum['green']:
                    maximum['green'] = int(case[i])
            if 'blue' in case[i+1]:
                if int(case[i]) > maximum['blue']:
                    maximum['blue'] = int(case[i])
    sum += (maximum['red'] * maximum['green'] * maximum['blue'])

print(sum)
        