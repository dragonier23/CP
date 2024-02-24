import re

def splitAction(action):
    if re.search(r":", action):
        print("reached")
        return action.split(":")
    return action

def result(attributes, workflow):
    key = 'in'
    while True:
        #let first check if the key is a defined answer
        if key == 'A':
            return True
        if key == 'R':
            return False
        #so the key is actually a key, so we need to work with it
        for step in workflow[key]:
            if len(step) == 1:
                key = step[0]
                break
            #so the step requires us to compare it
            if step[0][1] == '>':
                if attributes[step[0][0]] > int(step[0][2:]):
                    key = step[1]
                    break
            if step[0][1] == '<':
                if attributes[step[0][0]] < int(step[0][2:]):
                    key = step[1]
                    break


def main():
    filename = 'problemstatement.txt' #'test.txt' #

    file = open(filename, 'r').readlines()

    ans = 0
    workflow = dict()
    attributeStart= False
    for line in file:
        if attributeStart: 
            attributeList = line[1:-2].split(",")
            attributes = dict()
            for attribute in attributeList:
                attributes[attribute[0]] = int(attribute[2:])
            ans += sum(list(attributes[key] for key in attributes)) if result(attributes, workflow) else 0
            continue
        #we need to look for the blank line
        if not(line.strip()):
            attributeStart = True
            continue
        #so we want to break down each line
        breakDown = re.search(r"(\w+){(.+)}", line).groups()
        #print(breakDown[1].split(","))
        workflow[breakDown[0]] = [check.split(":") for check in breakDown[1].split(",")]
    print(ans)
    
if __name__ == '__main__':
    main()