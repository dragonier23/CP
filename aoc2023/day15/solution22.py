import re

filename = 'problemstatement.txt' #'test.txt' #

def hash(valList):
    if not(valList):
        return 0
    else:
        return ((ord(valList[-1]) + hash(valList[:-1])) * 17 ) % 256
    
file = (open(filename, 'r').readlines())[0].split(",")

boxes = []
for i in range(256):
    boxes.append([])

for step in file:
    try: 
        label = step[:step.index("=")]
        box = hash(label)
        present = False
        for item in boxes[box]: 
            if label == item[0]:
                item[1] = step[len(step) - 1]
                present = True
        if not(present):
            boxes[box].append([label, step[len(step) - 1]])
    except:
        label = step[:step.index("-")]
        box = hash(label)
        index = 0
        for lens in boxes[box]:
            if label == lens[0]:
                boxes[box].pop(index)
                break
            index += 1   

print(boxes)    

ans = 0
for i in range(256):
    index = 1
    for lens in boxes[i]:
        ans += ((i+1) * index * int(lens[1]))
        index += 1

print(ans)
