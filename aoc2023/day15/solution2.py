import re

filename = 'test.txt' #'problemstatement.txt' #

def hash(valList):
    if not(valList):
        return 0
    else:
        return ((ord(valList[-1]) + hash(valList[:-1])) * 17 ) % 256
    
file = (open(filename, 'r').readlines())[0].split(",")

boxes = dict() #initialise the box, which we will then edit

for step in file:
    try: 
        sign = step.index("=")
        label = step[:(sign)]
        box = str(hash(label))
        try: 
            present = False
            for lens in boxes[box]:
                if label == lens[0]:
                    lens[1] = step[len(step) - 1]
                    present = True
            if not(present):
               boxes[box].append([label, step[len(step) - 1]])
        except: 
            boxes[box] = []
            boxes[box].append([label, step[len(step) - 1]])
    except:
        sign = step.index("-")
        label = step[:(sign)]
        box = str(hash(label)) 
        index = 0
        try: 
            for lens in boxes[box]:
                if label == lens[0]:
                    boxes[box].pop(index)
                    break
                index += 1       
        except:
            continue

ans = 0
for box in boxes: #this box should be the key of each element
    boxno = int(box) + 1
    index = 1
    for lens in boxes[box]:
        ans += (boxno * index * int(lens[1]))
        index += 1

print(ans)
